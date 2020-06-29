from string import ascii_letters

vowels = ["a", "e", "i", "o", "u"]

phase = "weusedtowritewithnospaces"

for char in phase:
    if char not in ascii_letters:
        break
    if char in vowels:
        print("vowel")
    else:
        print("consonant")
