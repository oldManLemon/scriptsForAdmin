def intCheck(number):
    try:
        return int(number)
    except ValueError:
        return False

