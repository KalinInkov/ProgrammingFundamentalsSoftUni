import re

text = input()
word = input()

pattern = f"\\b{word}\\b" # или използваме  rf"\b{word}\b" без да escape-ваме "\"
count_words = re.findall(pattern,text,re.IGNORECASE)

print(len(count_words))
