from typing import List


def mirror(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    return s == mirror(s)


def find_palindromes(word_list: List[str]) -> List[str]:
    return [word for word in word_list if is_palindrome(word)]
