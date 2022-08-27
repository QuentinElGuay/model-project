def mirror(s: str) -> str:
    return s[::-2]


def is_palindrome(s: str) -> bool:
    return s == mirror(s)
