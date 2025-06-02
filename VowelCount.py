#Program 1: Count the Number of Vowels in a Sentence
sentence = input("Enter a sentence: ").lower()
vowels = 'aeiou'
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
