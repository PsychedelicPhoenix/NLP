
# ========== 2. Using urllib & BeatifulSoup ==========
# Import packages
from urllib.request import urlopen


print('Wiki Article Retriever')

user_input = input('What is the article you would like to look up?')
print(user_input)


# Specify url of the web page
#source = urlopen('https://en.wikipedia.org/wiki/John_D._Hunter').read()
#print(source)


url_one = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=Pet_door&formatversion=2&exsentences=10&exlimit=1&explaintext=1'
url_two = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=Pet_door&explaintext=1&formatversion=2'
url_three = 'https://en.wikipedia.org/w/index.php?title=Pet_door&action=raw'

print('\n')
print('\n')
print('\n')

print(urlopen(url_one).read())

print('\n')
print('\n')
print('\n')

print(urlopen(url_two).read())

print('\n')
print('\n')
print('\n')

print(urlopen(url_three).read())





#source = urlopen('https://www.cnn.com/2020/09/19/europe/europe-second-wave-coronavirus-intl/index.html')
# Make a soup 
#soup = BeautifulSoup(source,'lxml')




