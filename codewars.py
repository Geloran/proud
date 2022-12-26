#Given a month as an integer from 1 to 12, return to which quarter of 
#the year it belongs as an integer number.
#For example: month 2 (February), is part of the first quarter; month 6 (June), 
#is part of the second quarter; and month 11 (November), is part of the fourth quarter.

def quarter_of(month):
    q = {1: (1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    return [k for k,v in q.items() if v[0] <= month <= v[1]][0]
