#Sentiment Analysis: Biden Statements on Climate Change
#Biden Speech gathering

#Importing relevant packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Setting up Selenium for webscraping
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

#Creating a list of climate change keywords to help us indentify relevant statements
climate_keywords = ["climate change", "global warming", "greenhouse effect", "carbon emissions", "renewable energy", "fossil fuels", "sustainability", "climate crisis", "environmental impact", "paris agreement", "clean energy", "carbon footprint", "deforestation", "ocean acidification", "extreme weather", "climate action", "adaptation", "mitigation", "conservation", "emissions reduction"]


#Gathering the links that need to be scraped
base_url_biden = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200320&category2%5B0%5D=68&items_per_page=25&page="

start_page = 1
end_page = 31

links_to_scrape_biden = []

for page in range(start_page, end_page + 1):
    url = f"{base_url_biden}{page}"
    links_to_scrape_biden.append(url)
    

#Adding the first search URL that follows a different format from the rest
additional_url_biden = 'https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200320&category2%5B%5D=68&items_per_page=25'
links_to_scrape_biden.append(additional_url_biden)

#This will pull all links available on each webpage - this will be narrowed shortly
all_biden_links = []

for link in links_to_scrape_biden:
    driver.get(link)
    
    # Find all link elements using CSS selector
    link_elements = driver.find_elements(By.CSS_SELECTOR, "a")
    
    # Extract href attribute from each link element
    links = [link.get_attribute("href") for link in link_elements]
    
    all_biden_links.extend(links)

#This line will help us get rid of extra URLs initially captured above
filtered_biden_links = [link for link in all_biden_links if link and "https://www.presidency.ucsb.edu/documents/statement" in link]

#Now, we can filter specifically for climate-related statements from Biden
climate_biden_links = []

for link in filtered_biden_links:
    driver.get(link)
    div_elements = driver.find_elements(By.CSS_SELECTOR, "div p")
    text = [div.text for div in div_elements]
    if any(word.lower() in " ".join(text).lower() for word in climate_keywords):
        climate_biden_links.append(link)

driver.quit()  # Close the browser when finished
