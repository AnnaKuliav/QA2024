def is_palindrome_method2(s):
    s = s.strip().lower()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Examples
print(is_palindrome_method2("    aBC cba "))  # True
print(is_palindrome_method2("a BCQcb a    "))  # True
print(is_palindrome_method2(" ab bca"))  # False
print(is_palindrome_method2("ab b a"))  # False
