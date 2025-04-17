from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

URL = "https://www.ruthtrumpold.id.au/destech/?page_id=162"

head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

webpage = requests.get(URL, headers=head)
soup = BeautifulSoup(webpage.content, "html.parser")
chapter = soup.find("article", attrs = {"class" : 'post-162 page type-page status-publish hentry'}).text.strip()
all_list_items = []
print(chapter)

with open("destech.txt", 'a', encoding="utf-8") as f:
    f.write(chapter)

# output_file = "bullet_points.csv"

# with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
#     csv_writer = csv.writer(csvfile)
#         # Write header (optional)
#     csv_writer.writerow(['Bullet_Points'])
        
#         # Write each list item as a new row
#     for item in all_list_items:
#         csv_writer.writerow([item])
    
#     print(f"Successfully scraped {len(all_list_items)} bullet points to {output_file}")





# user agent list 
# {
#   "result": [
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
#     "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
#     "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"
#   ]
# }
