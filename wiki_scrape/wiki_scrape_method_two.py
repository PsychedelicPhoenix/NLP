
# ========== 2. Using urllib & BeatifulSoup ==========
# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


print()

# Specify url of the web page
source = urlopen('https://en.wikipedia.org/wiki/John_D._Hunter').read()

# Make a soup 
soup = BeautifulSoup(source,'lxml')
print('\nsoup\n')
print(soup)

# Extract the plain text content from paragraphs
paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))

# Extract text from paragraph headers
heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))

# Interleave paragraphs & headers
text = [val for pair in zip(paras, heads) for val in pair]
text = ' '.join(text)

# Drop footnote superscripts in brackets
text = re.sub(r"\[.*?\]+", '', text)

# Replace '\n' (a new line) with '' and end the string at $1000.
text = text.replace('\n', '')[:-11]
print(text)






for s in soup.find_all(text=True):
    # Check out the parent name
    print(f'Parent name: {s.parent.name}')
    # Check the text
    print(s)



for s in soup.find_all('span'):
    # Check out the parent name
    print(f'Parent name: {s.parent.name}')
    # Check the text
    print(s)



