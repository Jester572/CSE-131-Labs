# 1. Name:
#      Jesse Earley 
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program creates a calendar month for the specified month and year
# 4. What was the hardest part? Be as specific as possible.
#      Remembering how to handle errors.
# 5. How long did it take for you to complete the assignment?
#      4 Hours

def main():
    
    month = get_month()
    year = get_year()
    
    # Output
    display(month, year)
    
def get_month():
    while True:
        
        try:
            month = int(input('Provide the numerical month you would like to view. ie 1-Jan, 2-Feb, ... 12-Dec: '))
            if isinstance(month, int) and month > 0 and month < 13:
                return False
            else:
                print('chose a number between 1 and 12')
        except:
            print('Please chose an integer')
    return month
def get_year():
    while True:
        try:
            year = int(input('Provide the four digit Year you would like to use: '))
            if isinstance(year, int) and year >= 1753:
                return False
            else:
                 print('Chose a year equal to or greater than 1753')
        except:
            print('Chose a year equal to or greater than 1753')
    return year
def display(month, year):
    offset = compute_offset(month, year)
    num_days = days_month(month, year)
    display_table(offset, num_days)

def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline

def compute_offset(month, year):
    num_days = 0
    
    for i in range(1753, year):
        num_days += days_year(i)
    
    for i in range(1, month):
        num_days += days_month(i, year)
    
    return (num_days + 1) % 7

def days_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365

def days_month(month, year):
    #if it is a leap year and February 
    if is_leap_year(year) and month == 2:
        return 29
    
    # long_month = [1,3,5,7,8,10,12]
    
    #short months are months that have 30 days
    short_month = [4,6,9,11]
    
    # If month is not a short month and is not february returns 31 day.
    if month in short_month:
        return 30
    elif month == 2:
        return 28
    return 31

def is_leap_year(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()

