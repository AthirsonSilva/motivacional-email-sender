import smtplib as smtp
from random import choice
from datetime import datetime as dt

now = dt.now()
weekday = now.weekday()
MY_EMAIL = 'botpythonmain@gmail.com'
MY_PASSWORD = 'python310'


def send_email(quote):
    '''
    Email sender

        After getting the random quote
    this function sends a email containing it
    to the destination

    Args:
        quote (str): The quote to be sent
    '''

    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='athirsonarceus@gmail.com',
                            msg='Subject:Motivacional quote\n\n'
                            f'{quote}')


if weekday == 2:
    with open('./quotes.txt') as quotes:
        all_quotes = quotes.readlines()
        quote = choice(all_quotes)
        print(quote)

    send_email(quote)
