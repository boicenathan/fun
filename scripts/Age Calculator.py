# Age Calculator #

from datetime import date
from datetime import datetime

today = date.today()

userinput = input('Enter your birth year (ex. 2021-04-24): ')

birthdate = datetime.strptime(userinput, '%Y-%m-%d')

daydelta = today - birthdate.date()

age = int(daydelta.days / 365.25)

print('You are ' + str(age) + ' years old.')
