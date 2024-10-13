def check_sdt(sdt):
    if not sdt:
        return False
    else:
        if sdt.isdigit():
            if len(sdt) == 10:
                return True
            else:
                return False
        else:
            return False

def check_email(email):
    return email.endswith('@gmail.com')
