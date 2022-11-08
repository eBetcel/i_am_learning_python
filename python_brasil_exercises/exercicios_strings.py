def is_palindrome(palavra: str) -> bool:

    if palavra == palavra[::-1]:
        return True
    else: 
        return False
