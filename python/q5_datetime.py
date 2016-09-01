from datetime import datetime as dt

date_dict = {
        'a' : ['01-02-2013','07-28-2015','%m-%d-%Y'],
        'b' : ['12312013','05282015','%m%d%Y'],
        'c' : ['15-Jan-1994','14-Jul-2015','%d-%b-%Y']
        }

def diffsolve(dateinfo):
    sol = dt.strptime(dateinfo[1], dateinfo[2]) - dt.strptime(dateinfo[0],dateinfo[2])
    print sol




for date in date_dict:
    print date
    diffsolve(date_dict[date])
