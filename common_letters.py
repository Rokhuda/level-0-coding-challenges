def common_letters(word1, word2):
    common = ""
    for letter in word1:
        if letter in word2:
            common += letter + ', ' 
    return "Common letters: " + common

print(common_letters("house","computers"))