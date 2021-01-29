def check_vowels(string):
    vowels =""
    for letter in string:
        if letter in "aeiouAEIOU":
            vowels += letter
    return vowels


print(check_vowels("humanIng"))