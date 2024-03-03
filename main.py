from main_ui import Main_UI
import tkinter as tk
import smtplib

# * <- Main Variables -> * #
MY_EMAIL = "YOUR EMAIL ACCOUNT HERE"
MY_PASSWORD = "YOUR EMAIL APP PASWORD HERE"


def send_mail(email, subject, content):
    save_email(email)
    with smtplib.SMTP("YOUR HOST HERE") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:{subject}\n\n{content}"
        )


def save_email(email):
    try:
        email_txt = open("saved_email.txt", "r+")
    except FileNotFoundError:
        email_txt = open("saved_email.txt", "w")
        email_txt.write(email)
    except Exception as e:
        print(e)
    else:
        saved_email = email_txt.readlines()
        saved_email = [value.strip() for value in saved_email]
        if email in saved_email:
            return
        email_txt.write(email + "\n")


app_main_ui = Main_UI(send_mail)
