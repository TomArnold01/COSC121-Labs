def days_in_years(number_of_years):
    """ Return the number of days in the given number of years, assuming
        exactly 365 days in all years.
    """
    days = (number_of_years * 365)
    return days

print(days_in_years(1))
print(days_in_years(15))
      