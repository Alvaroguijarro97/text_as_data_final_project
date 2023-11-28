#Sentiment Analysis: Biden Statements on Climate Change
#Gathering and storing the statements in a database

#Importing relevant packages
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from biden_speech_links import climate_biden_links
import re

#Bringing in the driver we'll need for Selenium to function properly
webdriver_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(webdriver_path)
#driver.get("https://techwithtim.net")

def getHTMLdocument(url):
    driver.get(url)
    
    # Wait for the content to be loaded (adjust the timeout as needed)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'div')))
    
    # Retrieve the HTML content after it has been rendered
    html_doc = driver.page_source
    
    return html_doc

data = []

for link in climate_biden_links:
    driver.get(link)
    
    # Extract the title element
    title_element = driver.find_element(By.CSS_SELECTOR, "div h1")
    
    # Extract the date element
    date_element = driver.find_element(By.CSS_SELECTOR, "span.date-display-single[property='dc:date']")
    
    # Extract the text element
    text_elements = driver.find_elements(By.CSS_SELECTOR, "div p")
    text = " ".join(element.text for element in text_elements)
    
    data.append({
        "Title": title_element.text,
        "Date": date_element.text,
        "URL": link,
        "Text": text
    })
    
 
driver.quit()  # Close the browser when finished

biden_climate_statements = pd.DataFrame(data)

#Cleaning up the "Text" column of the dataframe

biden_climate_statements['Text'] = biden_climate_statements['Text'].str.replace('ABOUT SEARCH', '')

biden_climate_statements['Text'] = biden_climate_statements['Text'].str.replace('Online by Gerhard Peters and John T. Woolley.', '')

biden_climate_statements['Text'] = biden_climate_statements['Text'].str.replace('John Woolley and Gerhard Peters', '')

biden_climate_statements['Text'] = biden_climate_statements['Text'].str.replace('Contact Twitter', '')

biden_climate_statements['Text'] = biden_climate_statements['Text'].str.replace('Terms of Service | Privacy | Accessibility.', '')

biden_climate_statements['Text'] = biden_climate_statements['Text'].str.replace('Facebook Copyright ©.', '')

biden_climate_statements['Text'] = biden_climate_statements['Text'].str.replace('The American Presidency Project', '')












