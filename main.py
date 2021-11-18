import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)
print(today)
MY_EMAIL = "tejashwinim132@gmail.com"
MY_PASSWORD = " "

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}letter")


