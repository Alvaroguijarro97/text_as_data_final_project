#US Presidential Speeches on Climate Change since 2000

#Importing relevant packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from urllib.parse import urljoin


#First, we need to gather the URL's for all speeches given by U.S. presidents since 2000. We will break up the speech URLs by president.

#George W. Bush (2000 - 2008)

#Spoken Addresses and Remarks
bush_speech_links = []
link_number = 1
while link_number <= 173:
    new_url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200299&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A8&page=" + str(link_number)
    bush_speech_links.append(new_url)
    link_number += 1

bush_speech_links.append("https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200299&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A8")


#Statements
link_number = 1
while link_number <= 47:
    new_url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200301&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A68&page=" + str(link_number)
    bush_speech_links.append(new_url)
    link_number += 1

bush_speech_links.append("https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200301&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A68")


#Barack Obama (2008 - 2016)

#Spoken Addresses and Remarks
obama_speech_links = []
link_number = 1
while link_number <= 153:
    new_url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200300&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A8&page=" + str(link_number)
    obama_speech_links.append(new_url)
    link_number += 1

obama_speech_links.append("https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200300&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A8")


#Statements
link_number = 0
while link_number <= 57:
    new_url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200300&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A68&page=" + str(link_number)
    obama_speech_links.append(new_url)
    link_number += 1

obama_speech_links.append("https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200300&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A68")


#Donald Trump (2016 - 2020)

#Spoken Addresses and Remarks
trump_speech_links = []
link_number = 1
while link_number <= 70:
    new_url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200301&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A8&page=" + str(link_number)
    trump_speech_links.append(new_url)
    link_number += 1

trump_speech_links.append("https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200301&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A8")


#Statements
link_number = 0
while link_number <= 13:
    new_url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200301&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A68&page=" + str(link_number)
    trump_speech_links.append(new_url)
    link_number += 1

trump_speech_links.append("https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200301&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A68")

#Joe Biden (2020 - Present)

#Spoken Addresses and Remarks
biden_speech_links = []
link_number = 1
while link_number <= 47:
    new_url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200320&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A8&page=" + str(link_number)
    biden_speech_links.append(new_url)
    link_number += 1

biden_speech_links.append("https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200320&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A8")


#Statements
link_number = 0
while link_number <= 36:
    new_url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200320&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A68&page=" + str(link_number)
    biden_speech_links.append(new_url)
    link_number += 1

biden_speech_links.append("https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200320&category2%5B0%5D=406&items_per_page=25&f%5B0%5D=field_docs_category%3A68")


#Bush
all_bush_links = []

base_url = "https://www.presidency.ucsb.edu"  # Set the base URL

for link in bush_speech_links:
    response = requests.get(link)
    
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Find all link elements using BeautifulSoup
        link_elements = soup.find_all('a', href=True)
        
        # Extract href attribute from each link element and convert to absolute URL
        links = [urljoin(base_url, link['href']) for link in link_elements]
        
        all_bush_links.extend(links)
    else:
        print(f"Failed to retrieve content for URL: {link}. Status Code: {response.status_code}")


# List of strings to filter links
filter_strings = ["https://www.presidency.ucsb.edu/documents/", "statement", "remarks"]
filter_strings_2 = ["statement", "remarks"] 
# Filter the links based on the filter_strings
filtered_bush_links = [link for link in all_bush_links if any(s in link for s in filter_strings)]
filtered_bush_links_2 = [link for link in filtered_bush_links if any(s in link for s in filter_strings_2)]


#Obama
all_obama_links = []

base_url = "https://www.presidency.ucsb.edu"  # Set the base URL

for link in obama_speech_links:
    response = requests.get(link)
    
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Find all link elements using BeautifulSoup
        link_elements = soup.find_all('a', href=True)
        
        # Extract href attribute from each link element and convert to absolute URL
        links = [urljoin(base_url, link['href']) for link in link_elements]
        
        all_obama_links.extend(links)
    else:
        print(f"Failed to retrieve content for URL: {link}. Status Code: {response.status_code}")


# Filter the links based on the filter_strings
filtered_obama_links = [link for link in all_obama_links if any(s in link for s in filter_strings)]
filtered_obama_links_2 = [link for link in filtered_obama_links if any(s in link for s in filter_strings_2)]


#Trump
all_trump_links = []

base_url = "https://www.presidency.ucsb.edu"  # Set the base URL

for link in trump_speech_links:
    response = requests.get(link)
    
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Find all link elements using BeautifulSoup
        link_elements = soup.find_all('a', href=True)
        
        # Extract href attribute from each link element and convert to absolute URL
        links = [urljoin(base_url, link['href']) for link in link_elements]
        
        all_trump_links.extend(links)
    else:
        print(f"Failed to retrieve content for URL: {link}. Status Code: {response.status_code}")

# Filter the links based on the filter_strings
filtered_trump_links = [link for link in all_trump_links if any(s in link for s in filter_strings)]
filtered_trump_links_2 = [link for link in filtered_trump_links if any(s in link for s in filter_strings_2)]



#Biden
all_biden_links = []

base_url = "https://www.presidency.ucsb.edu"  # Set the base URL

for link in biden_speech_links:
    response = requests.get(link)
    
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Find all link elements using BeautifulSoup
        link_elements = soup.find_all('a', href=True)
        
        # Extract href attribute from each link element and convert to absolute URL
        links = [urljoin(base_url, link['href']) for link in link_elements]
        
        all_biden_links.extend(links)
    else:
        print(f"Failed to retrieve content for URL: {link}. Status Code: {response.status_code}")

# Filter the links based on the filter_strings
filtered_biden_links = [link for link in all_biden_links if any(s in link for s in filter_strings)]
filtered_biden_links_2 = [link for link in filtered_biden_links if any(s in link for s in filter_strings_2)]


#Now we create a giant list of climate related key words to identify climate speeches
climate_keywords = [
    "climate change", "global warming", "greenhouse effect", "carbon emissions", 
    "renewable energy", "fossil fuels", "sustainability", "climate crisis", 
    "environmental impact", "paris agreement", "clean energy", "carbon footprint", 
    "deforestation", "ocean acidification", "extreme weather", "climate action", 
    "adaptation", "mitigation", "conservation", "emissions reduction",
    "biofuels", "solar power", "wind energy", "sea level rise", "ecosystem",
    "biodiversity loss", "recycling", "sustainable development", "energy efficiency", 
    "air pollution", "water scarcity", "green technology", "carbon neutral", 
    "geothermal energy", "hydroelectric power", "climate policy", "environmental sustainability", 
    "natural resources", "urban sprawl", "climate finance",
    "carbon tax", "green jobs", "climate legislation", "energy policy", "environmental justice",
    "green economy", "sustainable agriculture", "climate resilience", "environmental regulation", 
    "clean air", "clean water", "green infrastructure", "climate adaptation", "energy transition", 
    "greenhouse gas inventory", "net zero emissions", "climate risk", "environmental stewardship", 
    "sustainable cities", "climate finance", "energy conservation", "green building", "climate negotiation", 
    "sustainable transport", "renewable portfolio standard", "climate diplomacy", "environmental governance", 
    "public transport", "climate education", "environmental advocacy"
]


# Creating a list of Bush climate links
bush_climate_links = []

for link in filtered_bush_links_2:
    response = requests.get(link)
    
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        text = " ".join([p.get_text() for p in soup.find_all('p')])
        
        if any(word.lower() in text.lower() for word in climate_keywords):
            bush_climate_links.append(link)
    else:
        print(f"Failed to retrieve content for URL: {link}. Status Code: {response.status_code}")


# Creating a list of Obama climate links
obama_climate_links = []

for link in filtered_obama_links_2:
    response = requests.get(link)
    
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        text = " ".join([p.get_text() for p in soup.find_all('p')])
        
        if any(word.lower() in text.lower() for word in climate_keywords):
            obama_climate_links.append(link)
    else:
        print(f"Failed to retrieve content for URL: {link}. Status Code: {response.status_code}")
        
        
# Creating a list of Trump climate links
trump_climate_links = []

for link in filtered_trump_links_2:
    response = requests.get(link)
    
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        text = " ".join([p.get_text() for p in soup.find_all('p')])
        
        if any(word.lower() in text.lower() for word in climate_keywords):
            trump_climate_links.append(link)
    else:
        print(f"Failed to retrieve content for URL: {link}. Status Code: {response.status_code}")
        
        
# Creating a list of Biden climate links
biden_climate_links = []

for link in filtered_biden_links_2:
    response = requests.get(link)
    
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        text = " ".join([p.get_text() for p in soup.find_all('p')])
        
        if any(word.lower() in text.lower() for word in climate_keywords):
            biden_climate_links.append(link)
    else:
        print(f"Failed to retrieve content for URL: {link}. Status Code: {response.status_code}")
        
        
#Actually scraping speeches with BeautifulSoup

api_key = 'TBD'

def getHTMLdocument(url):
    # Construct the API URL with your API key and the target URL
    api_url = f'http://api.scraperapi.com/?api_key={api_key}&url={url}'
    
    try:
        # Make the request to ScraperAPI
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve content for URL: {url}. Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
      

# let's build our dataframes

#Bush
bush_data = []

for link in bush_climate_links:
    # Make the request with ScraperAPI
    html_doc = getHTMLdocument(link)
    
    if html_doc is not None:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Extract the title element
        try:
            title_element = soup.find("h1")
            if title_element:
                title = title_element.get_text(strip=True)
            else:
                title = "N/A"
        except:
            title = "N/A"
        
        # Extract the date element
        try:
            date_element = soup.select_one("span.date-display-single[property='dc:date']")
            date_string = date_element["content"]
            date = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%d/%m/%Y")
        except (AttributeError, KeyError):
            date = "N/A"
        
        p_blocks = soup.find_all('p')
        last_speaker = "N/A"  # Initialize last_speaker
        
        # Check if there's a specific speaker indicated on the page
        speakers = [block.find('i') for block in p_blocks]
        if any(speaker for speaker in speakers if speaker):
            for block in p_blocks:
                italic_text = block.find('i')
                if italic_text:
                    last_speaker = italic_text.get_text(strip=True)  # Update the last speaker
                text = block.get_text(strip=True)
                bush_data.append({
                    "Title": title,
                    "URL": link,
                    "Date": date,
                    "Speaker": last_speaker,
                    "Text": text
                })
        else:
            # No specific speaker indicated, use "The President." for all text
            all_text = " ".join(block.get_text(strip=True) for block in p_blocks)
            bush_data.append({
                "Title": title,
                "URL": link,
                "Date": date,
                "Speaker": "The President.",
                "Text": all_text
            })

bush_climate_speeches = pd.DataFrame(bush_data)



#Obama
obama_data = []

for link in obama_climate_links:
    # Make the request with ScraperAPI
    html_doc = getHTMLdocument(link)
    
    if html_doc is not None:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Extract the title element
        try:
            title_element = soup.find("h1")
            if title_element:
                title = title_element.get_text(strip=True)
            else:
                title = "N/A"
        except:
            title = "N/A"
        
        # Extract the date element
        try:
            date_element = soup.select_one("span.date-display-single[property='dc:date']")
            date_string = date_element["content"]
            date = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%d/%m/%Y")
        except (AttributeError, KeyError):
            date = "N/A"
        
        p_blocks = soup.find_all('p')
        last_speaker = "N/A"  # Initialize last_speaker
        
        # Check if there's a specific speaker indicated on the page
        speakers = [block.find('i') for block in p_blocks]
        if any(speaker for speaker in speakers if speaker):
            for block in p_blocks:
                italic_text = block.find('i')
                if italic_text:
                    last_speaker = italic_text.get_text(strip=True)  # Update the last speaker
                text = block.get_text(strip=True)
                obama_data.append({
                    "Title": title,
                    "URL": link,
                    "Date": date,
                    "Speaker": last_speaker,
                    "Text": text
                })
        else:
            # No specific speaker indicated, use "The President." for all text
            all_text = " ".join(block.get_text(strip=True) for block in p_blocks)
            obama_data.append({
                "Title": title,
                "URL": link,
                "Date": date,
                "Speaker": "The President.",
                "Text": all_text
            })

obama_climate_speeches = pd.DataFrame(obama_data)


#Trump
trump_data = []

for link in trump_climate_links:
    # Make the request with ScraperAPI
    html_doc = getHTMLdocument(link)
    
    if html_doc is not None:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Extract the title element
        try:
            title_element = soup.find("h1")
            if title_element:
                title = title_element.get_text(strip=True)
            else:
                title = "N/A"
        except:
            title = "N/A"
        
        # Extract the date element
        try:
            date_element = soup.select_one("span.date-display-single[property='dc:date']")
            date_string = date_element["content"]
            date = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%d/%m/%Y")
        except (AttributeError, KeyError):
            date = "N/A"
        
        p_blocks = soup.find_all('p')
        last_speaker = "N/A"  # Initialize last_speaker
        
        # Check if there's a specific speaker indicated on the page
        speakers = [block.find('i') for block in p_blocks]
        if any(speaker for speaker in speakers if speaker):
            for block in p_blocks:
                italic_text = block.find('i')
                if italic_text:
                    last_speaker = italic_text.get_text(strip=True)  # Update the last speaker
                text = block.get_text(strip=True)
                trump_data.append({
                    "Title": title,
                    "URL": link,
                    "Date": date,
                    "Speaker": last_speaker,
                    "Text": text
                })
        else:
            # No specific speaker indicated, use "The President." for all text
            all_text = " ".join(block.get_text(strip=True) for block in p_blocks)
            trump_data.append({
                "Title": title,
                "URL": link,
                "Date": date,
                "Speaker": "The President.",
                "Text": all_text
            })

trump_climate_speeches = pd.DataFrame(trump_data)


#Biden
biden_data = []

for link in biden_climate_links:
    # Make the request with ScraperAPI
    html_doc = getHTMLdocument(link)
    
    if html_doc is not None:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Extract the title element
        try:
            title_element = soup.find("h1")
            if title_element:
                title = title_element.get_text(strip=True)
            else:
                title = "N/A"
        except:
            title = "N/A"
        
        # Extract the date element
        try:
            date_element = soup.select_one("span.date-display-single[property='dc:date']")
            date_string = date_element["content"]
            date = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%d/%m/%Y")
        except (AttributeError, KeyError):
            date = "N/A"
        
        p_blocks = soup.find_all('p')
        last_speaker = "N/A"  # Initialize last_speaker
        
        # Check if there's a specific speaker indicated on the page
        speakers = [block.find('i') for block in p_blocks]
        if any(speaker for speaker in speakers if speaker):
            for block in p_blocks:
                italic_text = block.find('i')
                if italic_text:
                    last_speaker = italic_text.get_text(strip=True)  # Update the last speaker
                text = block.get_text(strip=True)
                biden_data.append({
                    "Title": title,
                    "URL": link,
                    "Date": date,
                    "Speaker": last_speaker,
                    "Text": text
                })
        else:
            # No specific speaker indicated, use "The President." for all text
            all_text = " ".join(block.get_text(strip=True) for block in p_blocks)
            biden_data.append({
                "Title": title,
                "URL": link,
                "Date": date,
                "Speaker": "The President.",
                "Text": all_text
            })

biden_climate_speeches = pd.DataFrame(biden_data)

# List of desired speakers
desired_speakers = [
    "The President."
]

# Filter the DataFrames based on the desired speakers
bush_climate_speeches_final = bush_climate_speeches[
    bush_climate_speeches["Speaker"].isin(desired_speakers)
]

obama_climate_speeches_final = obama_climate_speeches[
    obama_climate_speeches["Speaker"].isin(desired_speakers)
]

trump_climate_speeches_final = trump_climate_speeches[
    trump_climate_speeches["Speaker"].isin(desired_speakers)
]

biden_climate_speeches_final = biden_climate_speeches[
    biden_climate_speeches["Speaker"].isin(desired_speakers)
]

# Before merging these dataframes, we need to rename the values in the "Speaker" column to be their actual names instead of just "The President.". 
bush_climate_speeches_final['Speaker'] = "George W. Bush"
obama_climate_speeches_final['Speaker'] = "Barack Obama"
trump_climate_speeches_final['Speaker'] = "Donald Trump"
biden_climate_speeches_final['Speaker'] = "Joe Biden"


# Merging all these dataframes into one final dataframe consisting of all climate speeches
us_pres_climate_speeches = pd.concat([bush_climate_speeches_final, obama_climate_speeches_final, trump_climate_speeches_final, biden_climate_speeches_final])

# Reset the index if needed (this will remove the old index and replace it with a new one)
us_pres_climate_speeches.reset_index(drop=True, inplace=True)

#Cleaning up the "Text" column of the dataframe

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('ABOUT SEARCH', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('AboutSearch', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('The President.', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('ABOUT SEARCH', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('Online by Gerhard Peters and John T. Woolley.', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('John Woolley and Gerhard Peters', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('Contact Twitter', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('Terms of Service | Privacy | Accessibility.', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('Facebook Copyright ©.', '')

us_pres_climate_speeches['Text'] = us_pres_climate_speeches['Text'].str.replace('The American Presidency Project', '')


# Some rows are individual sentences, let's merge those into one row where applicable so each row is an entire "Speech"
us_pres_climate_speeches_final = us_pres_climate_speeches.groupby(['Title', 'Date']).agg({'Text': ' '.join}).reset_index()


# let's save this as a CSV and SQLite database so we don't lose it

us_pres_climate_speeches_final.to_csv('us_pres_climate_speeches.csv', index=False)  

import sqlite3

# Connect to the SQLite database
# If the database does not exist, it will be created
conn = sqlite3.connect('us_pres_climate_speeches.db')

us_pres_climate_speeches_final.to_sql('us_pres_climate_speeches', conn, if_exists='replace', index=False)

conn.close()




