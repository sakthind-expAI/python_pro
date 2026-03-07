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

import urllib.request
import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup
import ssl

def get_xml_counts(url):
    """Retrieve and parse XML to get count of numbers and their sum."""
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    nums = [int(result.text) for result in counts]
    for result in counts:
        print(result.text)
    return len(nums), sum(nums)

def regex_examples():
    """Demonstrate regular expression usage."""
    x = 'My 2 favorite nos are 19 and 42'
    y = re.findall(r'[0-9]+', x)
    print(y)
    y = re.findall(r'[AEIOU]+', x)
    print(y)
    # Greedy extraction
    x = 'From: using the :character'
    y = re.findall(r'^F.+:', x)
    print(y)
    # Non-greedy extraction
    y = re.findall(r'^F.+?:', x)
    print(y)
    # Fine-tuning extraction
    x = 'From stephend@cuz.ac,za sat jan 05 23:12:59'
    y = re.findall(r'\S+@\S+', x)
    print(y)

def scrape_website(url):
    """Scrape anchor tags from a website."""
    # Ignore SSL/TLS certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))

if __name__ == "__main__":
    print('Hello World')

    # XML parsing
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    count, total = get_xml_counts(url)
    print('Count:', count)
    print('Sum:', total)

    # Regex examples
    regex_examples()

    # Web scraping - using a default URL for demo
    url = 'http://www.dr-chuck.com'
    scrape_website(url)

    # Second XML parsing
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    count, total = get_xml_counts(url)
    print('Count:', count)
    print('Sum:', total)