### Age Calculator ###

from datetime import date, datetime

today = date.today()  # Storing todays date

userinput = input('Enter your birth date (ex. 2021-04-24): ')  # Collecting the birth date of the user

birthdate = datetime.strptime(userinput, '%Y-%m-%d')  # Cleaning the user inputed date

daydelta = today - birthdate.date()  # Calculating the time difference in days

age = int(daydelta.days / 365.25)  # Converting to age in years

print('You are ' + str(age) + ' years old.')  # Printing the users age
