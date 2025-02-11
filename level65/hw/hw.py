def validate_pin(pin):
    # return true or false
    if not pin.isdigit():
        return False
    elif len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
     