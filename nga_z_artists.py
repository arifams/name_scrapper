# Import libraries
import requests
import csv

from bs4 import BeautifulSoup

# Collect first page of artists list
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_ = 'AlphaNav')
last_links.decompose()

# Create a file to write to and add headers row
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

# Pull all text from BodyText div
artist_name_list = soup.find(class_= 'BodyText')

#Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

# Create for loop to print out all artis name
# for artist_name in artist_name_list_items:
# 	print(artist_name.prettify)

# Create for loop to print out all artis name
# and use .contents to pull out the tag </a> children
for artist_name in artist_name_list_items:
	names = artist_name.contents[0]
	links = 'https://web.archive.org' + artist_name.get('href')
	print(names)
	print(links)

	# add each artist's name and associated info to the row
	f.writerow([names, links])
