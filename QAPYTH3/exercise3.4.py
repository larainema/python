#!/usr/bin/python3

def checkleap(year):
#year = int(input ('Please enter a year :')) 

    if year % 400 == 0:
        print(year, ' is a leap year')
        return True
    else:
        if year % 4 == 0 and year % 100 != 0 :
            print(year, ' is a leap year')
            return True
        else:
            print(year, ' is not a leap year')
            return False

weeklist = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def weekday(day):
    dmy = day.split('/')
    print(dmy)
    d = int(dmy[0])
    m = int(dmy[1])
    y = int(dmy[2])
    if ( m == 1 or m == 2 ):
        m = m + 12
        if ( checkleap(y) ):
            d = d - 2
        else:
            d = d - 1
    z=(1+d+(m*2)+(3*(m+1)/5)+y+y/4-y/100+y/400) % 7
    print(weeklist[int(z)])


if __name__ == '__main__':
    #checkleap(1984)
    #checkleap(1981)
    #checkleap(1904)
    #checkleap(1900)
    #checkleap(2000)
    #checkleap(2010)
    weekday('1/1/1980')
    weekday('9/8/1982')
    weekday('25/12/1983')
    weekday('31/5/1989')
    weekday('2/2/1990')
    weekday('29/2/1992')
