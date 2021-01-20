def check_vowels(str):
    vowels =""
    for letter in str:
        if letter in "aeiouAEIOU":
            vowels += letter
    return vowels


print(check_vowels("humanIng"))