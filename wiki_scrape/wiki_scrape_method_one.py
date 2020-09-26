

# ========== 1. Using wikipedia ==========
# Import packages
import wikipedia

# Specify the title of the Wikipedia page
wiki = wikipedia.page('John D. Hunter')

# Extract the plain text content of the page, excluding images, tables, and other data.
text = wiki.content
print(text)

# Replace '==' with '' (an empty string)
text = text.replace('==', '')

# Replace '\n' (a new line) with '' & end the string at $1000.
text = text.replace('\n', '')[:-12]
print(text)


'''
# Import package
import re
# Clean text
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')
text
'''


print('\n')
print('Wiki Article Retriever')
user_input = input('What is the article you would like to look up?')
print(user_input)
wiki = wikipedia.page(user_input)
text = wiki.content
print(text)