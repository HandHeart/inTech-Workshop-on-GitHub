#pip install termcolor
from termcolor import colored
# define  punctuation
punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''



#Program to sort alphabetically the words froma a string provied by the user
my_str = 'hello, world. how are you?'


#remove punctuation
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

#breakdown the string int a lsit of words

words = (word.lower() for word in no_punct.split())

#sort the list

words.sort()

#Display the sorted words
print("the sorted words are: ")

for word in words:
    print(colored(word, 'blue'))