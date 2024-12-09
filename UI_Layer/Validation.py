import re

def validate_email(email):
    if len(email) > 100:
        return False
    if '@' not in email or '.' not in email:
        return False
    return True

def validate_ssn(ssn):
    return bool(re.match(r'^\d{10}$', ssn))

def validate_full_name(full_name):
    return len(full_name) <= 100