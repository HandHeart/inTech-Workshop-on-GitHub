#Program to sort alphabetically the words froma a string provied by the user
my_str = input ('Enter a string: ')

#breakdown the string int a lsit of words

words = (word.lower() for word in my_str.split())

#sort the list

words.sort()

#Display the sorted words
print("the sorted words are: ")

for word in words:
    print(word)