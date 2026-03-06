word=input("Enter a word: ").lower().replace(" "," ")
reversed_word=word[::-1]
if word==reversed_word:
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))