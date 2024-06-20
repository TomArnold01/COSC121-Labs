def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    discount = drinks_cost / 100 * 30
    gst = (meal_cost + drinks_cost - discount) / 100 *15 
    total_cost = (drinks_cost - discount) + meal_cost + gst
    return(total_cost)

total_cost = dinner_calculator(12, 4)
# We round your answer to 2 decimal places before printing.
# Don't worry about why.
print(round(total_cost, 2)) 

total_cost = dinner_calculator(10, 0)
# We round your answer to 2 decimal places before printing.
# Don't worry about why.
print(round(total_cost, 2)) 