import pandas
import datetime as dt
from random import randint
import smtplib

# Creates a datetime object with today's date and time as the value
now = dt.datetime.now()

# Reads the csv file and stores it in a variable as a DataFrame object
birthdays = pandas.read_csv("birthdays.csv")

# Sets the email to send from and the app password previously configured
from_email = 'YOUR_EMAIL'
password = 'YOUR_PASSWORD'

# Starts a counter for iterating through the DataFrame
n = 0

for person in birthdays.name:
    # Checks to see if each person's month and day match today's month and day. If it does, it's their birthday and
    # Saves their info to variables
    if birthdays.iloc[n, 3] == now.month and birthdays.iloc[n, 4] == now.day:
        name = birthdays.iloc[n, 0]
        to_email = birthdays.iloc[n, 1]

        # Opens a random letter from the letter folder and replaces [NAME] with the person's name
        with open(f"letter_templates/letter_{randint(1, 3)}.txt", "r") as file:
            file_content = file.read()
            modified_content = file_content.replace('[NAME]', name)

        # Sends an email from the email specified above to the person's email whose birthday it is
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email, to_addrs=to_email,
                                msg="Subject: Happy Birthday!\n\n{}".format(modified_content))
            print("Email sent to {}.".format(name))
    n += 1
