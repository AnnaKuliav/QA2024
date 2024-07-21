def is_valid_email(email):
    if email.count('@') != 1 or email.count('.') != 1:
        return False

    at = email.index('@')
    dot  = email.index('.')

    if at > dot :
        return False

    if email.startswith('@') or email.endswith('.'):
        return False

    for i in email:
        if i != '@' and i != '.' and not i.isalnum():
            return False

    return True


# Examples
email1 = "aaa@bbb.ccc"
email2 = "@aaa.bbb"
email3 = "aaa@bbb."
email4 = "aaa@bbb.ccc."
email5 = "aaa@@bbb.ccc"
email6 = "aaa.bbb@ccc"
email7 = "aaa@bbb.ccc@ddd"
email8 = "aaa@bbb"
email9 = "aaa.bbb.ccc"
email10 = "aaa@bbb..ccc"

print(is_valid_email(email1))
print(is_valid_email(email2))
print(is_valid_email(email3))
print(is_valid_email(email4))
print(is_valid_email(email5))
print(is_valid_email(email6))
print(is_valid_email(email7))
print(is_valid_email(email8))
print(is_valid_email(email9))
print(is_valid_email(email10))




