from colorama import *
def validate_email_simple(email):
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if domain and '.' in domain:
            return True
    return False

email_to_validate = input("Put your email:")
if validate_email_simple(email_to_validate):
    print(Fore.GREEN+f"{email_to_validate} is a valid email address.")
else:
    print(Fore.RED+f"{email_to_validate} is not a valid email address.Please write valid email")