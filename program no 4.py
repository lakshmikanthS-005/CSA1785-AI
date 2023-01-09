# Program to sort alphabetically the words form a string 
my_str =str(input("enter the sentence you want to sort:"))
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word)
    
 output:
  enter the sentence you want to sort:hi this is sk from saveetha school of engineering
The sorted words are:
engineering
from
hi
is
of
saveetha
school
sk
this
