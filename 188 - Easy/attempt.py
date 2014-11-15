with open('dates.txt', 'r') as dates_file:
    input_dates = dates_file.readlines()

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
def getYear(yy):
    if len(yy) == 2:
        if int(yy) < 50:
            this_year = '20' + yy
        else:
            this_year = '19' + yy
    else:
        this_year = yy
    return this_year

def getDate(date):
    date = date.strip()
    if '-' in date:
        [year, month, day] = date.split('-')
    elif '/' in date:
        [month, day, year] = date.split('/')
    elif '#' in date:
        [month, year, day] = date.split('#')
    elif '*' in date:
        [day, month, year] = date.split('*')
    elif date[0:3] in MONTHS:
        month = '{0:02d}'.format(MONTHS.index(date[0:3]))
        [day, year] = date[4:].split(', ')
    new_year = getYear(year)
    new_date = new_year + '-' + month + '-' + day
    return new_date

def getAllDates(input_dates):
    new_dates = []
    for date in input_dates:
        new_dates.append(getDate(date))
    return new_dates

reformatted_dates = getAllDates(input_dates)

with open('new_dates.txt', 'w') as new_dates_file:
    for date in reformatted_dates:
        new_dates_file.write(date + '\n')