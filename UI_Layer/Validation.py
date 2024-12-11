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

def validate_property(property):
    return len(property) > 0 and len(property) <= 100

def validate_work_done(work_done):
    return len(work_done) > 0

def validate_upkeep_status(upkeep_status):
    return upkeep_status in ["Regular Maintenance", "Emergency Repair"]

def validate_employee(employee):
    return len(employee) > 0 and len(employee) <= 100

def validate_total_costs(total_costs):
    try:
        cost = int(total_costs)
        return cost >= 0
    except ValueError:
        return False

def validate_boolean(value):
    return value.lower() in ["true", "false"]

def validate_contractors_used(contractors_used):
    return all(len(contractor.strip()) > 0 for contractor in contractors_used.split(','))