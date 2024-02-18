from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np

driver = webdriver.Chrome()


url_list = [
    "https://www.zomato.com/mumbai/hnh-salad-co-7-bungalows",
    "https://www.zomato.com/mumbai/govindas-bistro-1-juhu/info",
    "https://www.zomato.com/mumbai/august-cafe-deli-bakery-patisserie-andheri-lokhandwala",
    "https://www.zomato.com/mumbai/gourmet-house-by-minis-kitchen-veera-desai-area",
    "https://www.zomato.com/mumbai/grandmamas-cafe-juhu",
    "https://www.zomato.com/mumbai/the-barn-@-food-square-santacruz-west",
    "https://www.zomato.com/mumbai/the-homemade-cafe-bar-juhu",
    "https://www.zomato.com/mumbai/zoca-cafe-veera-desai-area",
    "https://www.zomato.com/mumbai/bayleaf-cafe-juhu",
    "https://www.zomato.com/mumbai/toco-andheri-lokhandwala",
    "https://www.zomato.com/mumbai/prithvi-cafe-juhu",
    "https://www.zomato.com/mumbai/coco-cafe-oshiwara",
    ]
avg_cost = []
for i in url_list:
    driver.get(i)


    cost = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[4]/section/section/article[1]/section[1]/p[3]')
    avg_cost.append(cost.text.encode('utf-8'))
print(avg_cost)




driver.get("https://www.zomato.com/mumbai/govindas-bistro-1-juhu/reviews")
elements = driver.find_elements(By.XPATH, '//*[@color="#9C9C9C"]')
d = []
# Print the text of each element
for date in elements:
    d.append(date.text)
print(d)

import re

# Your list
lst = ['', '10 hours ago', '0 Votes for helpful, 0 Comments', '8 days ago', '0 Votes for helpful, 0 Comments', '15 days ago', '0 Votes for helpful, 0 Comments', '21 days ago', '0 Votes for helpful, 0 Comments', '23 days ago', '0 Votes for helpful, 0 Comments']

# Regex pattern
pattern = r'\d+\s+(hours|days)\s+ago'

# Filter the list
filtered_lst = [s for s in lst if re.search(pattern, s)]

print(filtered_lst)//['10 hours ago', '8 days ago', '15 days ago', '21 days ago', '23 days ago']
