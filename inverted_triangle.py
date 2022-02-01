def verify_leap_year(year):
    try:
        year = int(year)
        if year % 4 == 0 or year % 400 == 0:
            return True
        return False
    except :
        return f'{year} is not a valide, expected number'


