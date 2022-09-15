def check_year(year):
    if not year % 4:
        return True
    elif not year % 100:
        return True
    elif year % 400:
        return False
    return True
