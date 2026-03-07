"""
Python Code Examples

This script demonstrates various Python programming concepts including:
- Basic output and imports
- Web data retrieval and XML parsing
- Regular expressions for text processing
- Web scraping with BeautifulSoup

Examples are based on introductory Python tutorials.
Sakthi Narayanan D
"""

print ('Hello World')

#json and xml parsing/extraction
import urllib.request
import xml.etree.ElementTree as ET

#url = input('Enter location: ')
#if len(url) < 1 : 
#    url = 'https://docs.python.org/3/tutorial/index.html'

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    print(result.text)
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))

import re
x = 'My 2 favorite nos are 19 and 42'
y = re.findall('[0-9]+',x)
print (y)
y = re.findall('[AEIOU]+',x)
print (y)
#greedy extraction
x = 'From: using the :character'
y = re.findall('^F.+:',x)
print (y)

#non-greedy extraction
y = re.findall('^F.+?:',x)
print (y)

#fine-tuning extraction
x = 'From stephend@cuz.ac,za sat jan 05 23:12:59'
y = re.findall('\S+@\S+',x)
print (y)

#web scraping
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#xml extraction
import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    print(result.text)
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))