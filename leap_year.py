#Gregorian calendar, the years 2000 and 2400 are leap years,
#while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.


def leap_year():
    year = int(input("Enter year to check if is a leap year or enter 0 to quit: "))
    while year != 0:
        
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("{0} is a leap year".format(year))
                    year = int(input("Enter year to check if is a leap year or enter 0 to quit: "))
                else:
                    print("{0} is not a leap year".format(year))
                    year = int(input("Enter year to check if is a leap year or enter 0 to quit: "))

if __name__ == "__main__":

    leap_year()