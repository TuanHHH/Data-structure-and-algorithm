def is_palindrome(first_word:str,second_word:str):
    return first_word == second_word[::-1]
print(is_palindrome("Hello I'm Tuan","nauT m'I olleH"))