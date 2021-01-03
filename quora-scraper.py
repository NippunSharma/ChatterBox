import urllib
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
df = pd.DataFrame({"question": [],"answers":[]})
urls=['https://www.quora.com/Is-IIT-Mandi-safe-from-avalanche-and-other-natural-calamities-Are-the-mountain-roads-easy-to-travel-or-is-there-any-danger','https://www.quora.com/Is-the-Uhl-river-near-IIT-Mandi-dangerous','https://www.quora.com/How-is-the-road-in-hilly-areas-connecting-Delhi-to-IIT-Mandi','https://www.quora.com/How-do-I-reach-IIT-Mandi-from-Chandigarh-in-the-safest-way-possible','https://www.quora.com/What-are-the-bus-timings-from-Chandigarh-to-Mandi-When-are-the-first-and-last-buses-to-Mandi-from-Chandigarh','https://www.quora.com/Which-is-better-chemical-at-IIT-Kharagpur-or-CS-at-IIT-Mandi','https://www.quora.com/Is-IIT-Mandi-or-Bits-Pilani-better-for-studying-Computer-Science','https://www.quora.com/How-is-IIT-Mandi-CS-in-terms-of-campus-placement-and-college-life']
for i in urls:
	url =i
	page = driver.get(url)
	content = driver.page_source
	soup = BeautifulSoup(content)
	question = soup.find("div", attrs={'class':"q-text puppeteer_test_question_title"})
	answers = soup.find_all("div", attrs={"class": "q-relative spacing_log_answer_content puppeteer_test_answer_content"})
	for answer in answers:
	     df = df.append({"question": question.text,
		 "answers": answer.text
		  }, ignore_index=True)
	df
df.to_csv("One_URLs.csv")

