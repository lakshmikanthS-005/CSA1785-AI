Input:

import string
def remove_punctuations(text):
    for c in string.punctuation:
        text = text.replace(c,"")
    return text
text =input("Enter the String: ")
print("Original text:")
print(text)
result = remove_punctuations(text)
print("After removing Punctuations from the said string:")
print(result)

Output:
  
Enter the String: "lakshm.ikan.th,s"
Original text:
"lakshm.ikan.th,s"
After removing Punctuations from the said string:
lakshmikanths
