def create_palindrome(word):
    characters = []
    character_count = {}

    for char in word:
        if char in characters:
            character_count[char] += 1
        else:
            characters.append(char)
            character_count[char] = 1

    palindrome = ""
    center_character = ""

    for char in characters:
        count = character_count[char]
        if count % 2 == 0:
            palindrome += char * (count // 2)
            character_count[char] = 0
        elif center_character == "":
            center_character = char * count
        else:
            return False

    palindrome += center_character + palindrome[::-1]
    return palindrome

word = input("Введите слово: ")

if word == word[::-1]:
    print('Слово "' + word + '" уже является палиндромом')
elif create_palindrome(word) == False:
    print('Нельзя сделать палиндром')
else:
    print('Полученный палиндром: ', create_palindrome(word))
