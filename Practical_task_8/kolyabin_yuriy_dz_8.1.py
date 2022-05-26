import re


def email_parse(email):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    email_is_valid = pattern.match(email)
    if email_is_valid is None:
        msg = f'wrong email: {email}'
        raise ValueError(msg)
    return email_is_valid.groupdict()


email_address = input('enter your email address: ')
print(email_parse(email_address))
