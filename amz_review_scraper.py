import requests
from bs4 import BeautifulSoup
import re
import random

def amazon_scraper():
    URL='https://www.amazon.com/s?k=tws+earbuds&crid=3TYABZ2EEKLG4&sprefix=TWS+%2Caps%2C443&ref=nb_sb_ss_ts-doa-p_1_4'
    HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    webpage=requests.get(URL, headers=HEADERS)

    global product_reviews
    product_reviews = {}

    for i in range(5,8):
        if webpage.status_code == 200:
            soup = BeautifulSoup(webpage.content, 'html.parser')
            try:
                links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
                href = links[i].get('href')
                product_link = "https://amazon.com"+href
                print("...processing product",'[',i,']')
                new_webpage = requests.get(product_link, headers=HEADERS)
                print("Response for product link: ",new_webpage.status_code)

                if new_webpage.status_code == 200:
                    new_soup = BeautifulSoup(new_webpage.content,'html.parser')
                    '''product_name = new_soup.find("span",attrs={"id":"productTitle"}).text.strip()
                    print("Product name: ",product_name)'''

                    more_reviews_button = new_soup.find("a",attrs={"data-hook":"see-all-reviews-link-foot"})
                    more_reviews_button_href = more_reviews_button.get('href')
                    more_reviews_button_link = "https://amazon.com"+more_reviews_button_href
                    print(more_reviews_button_link)
                    print()
                    product_name_pattern = r"https://amazon\.com/([a-zA-Z0-9-]+)/product-reviews/[a-zA-Z0-9]+/ref=cm_cr_dp_d_show_all_btm\?ie=UTF8&reviewerType=all_reviews"
                    match = re.search(product_name_pattern, more_reviews_button_link)

                    if match:
                        product_name = match.group(1)
                        print("Product name: ",product_name)

                    more_reviews_button_webpage = requests.get(more_reviews_button_link, headers=HEADERS)

                    if more_reviews_button_webpage.status_code == 200:
                        more_reviews_button_webpage_soup = BeautifulSoup(more_reviews_button_webpage.content,'html.parser')

                        review_ele = more_reviews_button_webpage_soup.find_all("a",attrs={'class':'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold','data-hook':'review-title'})
                        review_text = more_reviews_button_webpage_soup.find_all("span",attrs={'data-hook':'review-body','class':'a-size-base review-text review-text-content'})

                        review_count=0
                        review_list = []

                        for body in review_text:
                            text = body.get_text().strip()
                            #print(text)
                            print()
                            review_list.append(text)

                        for a_ele in review_ele:
                            span_ele = a_ele.find_all('span')

                            if span_ele:
                                last_span = span_ele[-1]
                                review_count+=1
                                span = last_span.get_text().strip()
                                #print(span)
                                print()
                                review_list.append(span)

                            else:
                                print("No matching 'a' element found.")

                        print()
                        random.shuffle(review_list)
                        #print(review_list)
                        product_reviews[product_name] = review_list

            except Exception as e:
                print("Error processing product","[",i,"]",str(e))
                continue

        else:
            print("Failed to retieve webpage")

    print()
    print("RESULTS:-")
    print(product_reviews)
    print("====================================================================================================================================================================================================")

amazon_scraper()


#next review page:-
'''replacement = "ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&pageNumber=2&reviewerType=all_reviews"
ref_index = more_reviews_button_link.find("ref=")

if ref_index != -1:
    new_url = more_reviews_button_link[:ref_index] + replacement
    print("New URL:", new_url)

    next_page_webpage = requests.get(new_url, headers=HEADERS)
    next_page_soup = BeautifulSoup(next_page_webpage.content, 'html.parser')

    print(next_page_webpage.status_code)

    next_page_reviews = next_page_soup.find_all("span",attrs={'data-hook':'review-body','class':'a-size-base review-text review-text-content'})
    print("here")
    print(next_page_reviews)
    for review in next_page_reviews:
        span = review.find_all("span")
        if span:
            print("here2")
            last = span[-1]
            print("Next page user review: ",last.get_text())
            print()

        else:
            print("no matching 'a' element found")'''