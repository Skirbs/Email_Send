import tkinter as tk
import re
from threading import Timer

from saved_email_ui import Saved_Email

FONT = "Calibri"
EMAIL_REGEX = re.compile("[^@]+@[^@]+\.[^@]+")
# EMAIL_REGEX = re.compile("")


class Main_UI(tk.Tk):
    def __init__(self, send_mail):  # * args refer to functions thats been passed down
        super().__init__()

        self.send_mail = send_mail

        self.email_menu = None  # refers to email list menu

        self.title("Mail Send")
        self.config(padx=20, pady=20)
        self.logo_photoimage = tk.PhotoImage(file="./gmail_icon.png")

        self.email_address = tk.StringVar(self)
        self.subject = tk.StringVar(self)
        self.content = tk.StringVar(self)

        self.create_ui()
        self.mainloop()

    def send_mail_ui(self):
        def send_mail_main():
            self.send_mail(
                self.email_address.get(), self.subject.get(), self.content.get()
            )
            self.feedback_msg.config(text="Mail Sent", fg="green")
            self.email_address_entry.delete(0, "end")
            self.subject_entry.delete(0, "end")
            self.content_entry.delete(0, "end")

        if not EMAIL_REGEX.match(self.email_address.get()):
            self.feedback_msg.config(text="Email Entry Not Valid", fg="red")
            return
        self.feedback_msg.config(text="Sending Mail...", fg="gray")
        Timer(0.1, send_mail_main).start()  # ! DOCUMENT THIS BOI

    def open_address_menu(self):
        if self.email_menu != None:
            return
        self.email_menu = Saved_Email(self)

    def create_ui(self):
        # Header
        header_frame = tk.Frame(self)
        header_frame.pack()
        logo_frame = tk.Canvas(header_frame, width=130, height=96)
        logo_frame.grid(column=0, row=0)
        logo_frame.create_image(66, 50, image=self.logo_photoimage)

        header_text = tk.Label(header_frame, text="Mail Send", font=f"{FONT} 50 bold")
        header_text.grid(column=1, row=0)

        # Send To Label
        send_label = tk.Label(self, text="Send To", font=f"{FONT} 30")
        send_label.pack()

        # Main Entries
        entries_frame = tk.Frame(self)
        entries_frame.pack()

        email_address_label = tk.Label(
            entries_frame, text="Email Address", font=f"{FONT} 20"
        )
        email_address_label.grid(column=0, row=0, ipadx=5, ipady=5)

        self.email_address_entry = tk.Entry(
            entries_frame, font=f"{FONT} 20", textvariable=self.email_address
        )
        self.email_address_entry.grid(column=1, row=0)

        email_address_menu = tk.Button(
            entries_frame,
            text="Email List",
            font=f"{FONT} 12",
            command=self.open_address_menu,
        )
        email_address_menu.grid(column=2, row=0, ipadx=5)

        subject_label = tk.Label(entries_frame, text="Subject", font=f"{FONT} 20")
        subject_label.grid(column=0, row=1, ipadx=5, ipady=5)

        self.subject_entry = tk.Entry(
            entries_frame, font=f"{FONT} 20", textvariable=self.subject
        )
        self.subject_entry.grid(column=1, row=1)

        content_label = tk.Label(entries_frame, text="Content", font=f"{FONT} 20")
        content_label.grid(column=0, row=2, ipadx=5, ipady=5)

        self.content_entry = tk.Entry(
            entries_frame, font=f"{FONT} 20", textvariable=self.content
        )
        self.content_entry.grid(column=1, row=2)

        # Submit Button
        submit_button = tk.Button(
            self, text="Send", font=f"{FONT} 20", command=self.send_mail_ui
        )
        submit_button.pack()

        # Error Message
        self.feedback_msg = tk.Label(self, font=f"{FONT} 12 bold", fg="red")
        self.feedback_msg.pack()

    def insert_email(self, value):
        self.email_address_entry.delete(0, "end")
        self.email_address_entry.insert(0, value)
