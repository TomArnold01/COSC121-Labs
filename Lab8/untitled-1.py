"""A program to read a CSV file of rainfalls and print the totals
   for each month.
"""

from os.path import isfile as is_valid_file

def main():
    """Prompt the user to provide a csv file of rainfall data, process the 
       given file's data, and print the monthly rainfall totals. 
       The file is assumed to have the month number in column 1, the number 
       of days in the month in column 2, and the floating point rainfalls 
       (in mm) for that month in the remaining columns of the row.
    """
    filename = input('Input csv file name? ')
    while not is_valid_file(filename):
        print('File does not exist.')
        filename = input('Input csv file name? ') 
    datafile = open(filename) 
    data = datafile.read().splitlines()
    datafile.close()
    results = [] # 1 A list of (month, rainfall) tuples

    for line in data:                # 2 for each line in data speerated by a , 
        
        columns = line.split(',')    # 3 splits everything to single numbers
        
        month = int(columns[0])      # 4 sets months as the first element of each list 
        
        num_days = int(columns[1])   # 5 sets num_days as the second element of each list 
        
        total_rainfall = 0           # 6 sets total_rainfall to 0 
        
        for col in columns[2:2 + num_days]:   # 7 for every num in the list called colunms
            
            total_rainfall += float(col)      # 8 total_rainfall plus each col as a float 
            
        results.append((month, total_rainfall)) # 9 for each line appends month and total rainfall to results 

    print('Total rainfalls for each month')
    for (month, total_rainfall) in results:
        print('Month {:2}: {:.1f}'.format(month, total_rainfall))


main()

