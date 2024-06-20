def days_in_years(number_of_years):
    """ Return the number of days in the given number of years, assuming
        exactly 365 days in all years"""
    days_in_years = number_of_years * 365
    return days_in_years

print(number_of_years(2))
print(number_of_years(15))