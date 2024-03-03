import tkinter as tk

FONT = "Calibri"


def get_saved_emails():
    try:
        with open("saved_email.txt") as file:
            email_list = [value.strip() for value in file.readlines()]
            if len(email_list) == 0:
                return ["None"]
            return email_list
    except:
        return ["None"]


class Saved_Email(tk.Toplevel):
    def __init__(self, window):
        super().__init__(window)
        self.window = window  # this refers to the main ui
        self.title("Saved Emails")
        self.config(padx=20, pady=20)

        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.email_list = get_saved_emails()
        self.selected_email = tk.StringVar(value=self.email_list[0])

        self.create_ui()

    def close_window(self):
        self.window.email_menu = None
        self.destroy()

    def enter_email(self):
        if self.selected_email.get() == "None":
            self.close_window()
            return
        self.window.insert_email(self.selected_email.get())
        self.close_window()

    def create_ui(self):
        # Header
        header_text = tk.Label(self, text="Email List", font=f"{FONT} 30 bold")
        header_text.pack()

        # OptionMenu
        email_options = tk.OptionMenu(self, self.selected_email, *self.email_list)
        email_options.pack()

        # Enter
        enter_button = tk.Button(
            self, text="enter", font=f"{FONT} 16", command=self.enter_email
        )
        enter_button.pack()
