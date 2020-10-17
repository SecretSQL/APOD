# APOD_image_scraper.py
# APOD "NASA Astronomy Picture of the Day" Web Scraping basic case
# 20201017 dgt aka secretsql 
# Based on "Intermediate Python" O'Reilly lab by Jessica McKellar
# Working version
# Could use enhancement to follow additional links
# or to limit the number of images downloaded
# Useful as a learning exercise. 
# Use other web scraping utilities for production purposes
#
# Flow
# 0. Setup local download directory
# 1. Connect to the APOD Archive Index  "https://apod.nasa.gov/apod/archivepix.html"
# 2. Follow each link and pull down the image associated
# 3. Find the Image on the linked page
# 4. Download the linked image

# Concepts
# 1. Downloading    => urllib.urlopen
# 2. Parsing        => BeautifulSoup
# 3. Parsing html   => Beautiful Soup
import os
import datetime
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from os.path import expanduser
# Create the Download Directory
# Get user home directory
home = expanduser("~")
# Get Current Date
date_time = datetime.datetime.now()
now = date_time.strftime("%Y-%m-%d")

# Create the download_directory name =[$HOME]/pictures/apod_[date]
# (Assumes a pictures directory exists)
download_directory =home+"/Pictures/apod_"+now+"/"
print ("Download directory is: "+download_directory)
# Create the Download directory
os.makedirs(download_directory)

# Read the APODS index page
base_url = "https://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(base_url).read()
# For each link on the index page:
for link in  BeautifulSoup(content, "lxml").findAll("a"):
    # Construct an absolute URL
    href = urljoin(base_url, link["href"])
    print ("Following the Absolute link: ", link)

    # Follow the absolute URL link and pull down the image on the linked page
    content = urllib.request.urlopen(href).read()
    # Find all images on the newly referrenced content page
    for img in BeautifulSoup(content, "lxml").findAll("img"):
            print ("Following the Image link: ", href)
            # Construct an absolute URL to the image
            img_href = urljoin(href, img["src"])
            # Get the image name
            img_name = img_href.split("/")[-1]
            print ("Downloading the image source: ", img_href," as file: " , img_name)
            # Follow the absolute image URL and download the image
            urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
 