from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np


overview_url = "https://www.zomato.com/mumbai/hnh-salad-co-7-bungalow"
review_url = "https://www.zomato.com/mumbai/ettarra-1-juhu/reviews"
indiv_review = []
driver = webdriver.Chrome()
driver.get(review_url)
# elements = driver.find_elements(By.CSS_SELECTOR, '.sc-1hez2tp-0.sc-ibxvc.IrFyy')
overall_review = [4.2,4.5,4.3,4.1,4.0,3.9,4.4,4.4,4.2,4.5,4.0,4.0]




review_url_list = [
    "https://www.zomato.com/mumbai/hnh-salad-co-7-bungalows/reviews",
    "https://www.zomato.com/mumbai/govindas-bistro-1-juhu/reviews",
    "https://www.zomato.com/mumbai/august-cafe-deli-bakery-patisserie-andheri-lokhandwala/reviews",
    "https://www.zomato.com/mumbai/gourmet-house-by-minis-kitchen-veera-desai-area/reviews",
    "https://www.zomato.com/mumbai/grandmamas-cafe-juhu/reviews",
    "https://www.zomato.com/mumbai/the-barn-@-food-square-santacruz-west/reviews",
    "https://www.zomato.com/mumbai/the-homemade-cafe-bar-juhu/reviews",
    "https://www.zomato.com/mumbai/zoca-cafe-veera-desai-area/reviews",
    "https://www.zomato.com/mumbai/bayleaf-cafe-juhu/reviews",
    "https://www.zomato.com/mumbai/toco-andheri-lokhandwala/reviews",
    "https://www.zomato.com/mumbai/prithvi-cafe-juhu/reviews",
    "https://www.zomato.com/mumbai/coco-cafe-oshiwara/reviews"
]
dining_rating = []
elements = [] # define elements as an empty list
restaurant_names = ["HnH Salad Co.", "Govinda's Bistro", "Blabber All Day", "Grandmama's Cafe","The Barn @ Food Square","The Homemade Cafe & Bar","Zoca Cafe","Bayleaf Cafe","Toco","Prithvi Cafe"
                        "Coco Cafe"]
comments = []
for  i in review_url_list:
    driver.get(i)
    
    elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.sc-1q7bklc-1.cILgox')))
    temp =[]
    for i in elements:
        if i !="":
            temp.append(i.text)
    indiv_review.append(temp)
    
    try:  
        elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/div/section[4]/div/div/section/div[2]/p'))
            )
    except:
        elements.extend(["not found"]) # append "not found" to a list, not to a string

    finally:    
        for element in elements:
            comments.append(element.get_attribute("innerHTML").encode('utf-8'))


# elements = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/div/section[4]/div/div/section/div[2]/p'))
#     )

driver.get(review_url)
print(indiv_review)


restaurant_names = ["HnH Salad Co.", "Govinda's Bistro", "Blabber All Day", "Grandmama's Cafe","The Barn @ Food Square","The Homemade Cafe & Bar","Zoca Cafe","Bayleaf Cafe","Toco","Prithvi Cafe"
                        "Coco Cafe"]
dict = {"Names": restaurant_names, "overall rating": overall_review, "individual review": indiv_review, "comments": comments}

# create a Pandas DataFrame from the dictionary
max_len = max(len(v) for v in dict.values())
# save the DataFrame as a CSV file
dict = {k: np.pad(v, (0, max_len - len(v)), mode="constant") for k, v in dict.items()}

# create a Pandas DataFrame from the padded dictionary
df = pd.DataFrame(dict)

# save the DataFrame as a CSV file
df.to_csv("output.csv", header=True, index=False)