# Import library
from textblob import TextBlob

# Input word
words = ["Data Scence", "Mahine learnin"]

# Corrected word
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))

# Display output
print("Worng Words : ", words)
print("corrected Words are : ")

for i in corrected_words:
    print(i.correct(), end=" ")
