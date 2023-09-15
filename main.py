import tkinter
import tkmacosx
import password
import pyperclip

BACKGROUND = '#FEF0F0'
FONT_NAME = 'Futura Std'
LABEL_FONT_COLOR = '#100809'
WARNING_COLOR = '#D2546F'
PLACEHOLDER_COLOR = '#888888'
GENERATE_NORMAL_BG = '#B8B5B6'
GENERATE_ACTIVE_BG = "#B8B5B6"
GENERATE_NORMAL_FG = '#482B2F'
GENERATE_ACTIVE_FG = "#ffffff"
SAVE_NORMAL_BG = '#B8B5B6'
SAVE_ACTIVE_BG = "#B8B5B6"
SAVE_NORMAL_FG = '#482B2F'
SAVE_ACTIVE_FG = "#ffffff"
SAVE_DISABLED_BG = "#FEF0F0"
SAVE_DISABLED_FG = "#B8B5B6"
input_txt = ""
DEFAULT_WEB_STR = "Type the Website URL Here"
DEFAULT_USERNAME_STR = "Type your Email/Username Here"
DEFAULT_PASSWORD_STR = "Your Password"
# ---------------------------- UI SETUP ------------------------------- #

# Window --------------------------------

root = tkinter.Tk()
root.title("Password Manager")
root.config(padx=75, pady=25, bg=BACKGROUND)

# Title --------------------------------

title_label = tkinter.Label(text="The Favorite", bg=BACKGROUND, fg=LABEL_FONT_COLOR,
                            font=(FONT_NAME, 32, ""), pady=25)
title_label.grid(column=0, columnspan=4, row=0)

# Canvas/Image --------------------------------

canvas = tkinter.Canvas(width=256, height=230, highlightthickness=0, bg=BACKGROUND)
lock_img = tkinter.PhotoImage(file='img/logo without anything.png')
canvas.create_image(128, 115, image=lock_img)
canvas.grid(column=0, columnspan=4, row=1)

# Website Row + Entry commands before first Entry --------------------------------

url_label = tkinter.Label(text="Website:", font=(FONT_NAME, 16, ""), foreground=LABEL_FONT_COLOR, background=BACKGROUND)
url_label.config(pady=20, justify="left")
url_label.grid(column=0, row=2)

default_text_web = tkinter.StringVar()
default_text_web.set(DEFAULT_WEB_STR)
default_text_username = tkinter.StringVar()
default_text_username.set(DEFAULT_USERNAME_STR)
default_text_password = tkinter.StringVar()
default_text_password.set(DEFAULT_PASSWORD_STR)


def on_click(event):
    if event.widget == entry_website:
        default_text = DEFAULT_WEB_STR
        placeholder_label["text"] = ""
    elif event.widget == entry_username:
        default_text = DEFAULT_USERNAME_STR
        placeholder_label["text"] = ""
    elif event.widget == entry_password:
        default_text = DEFAULT_PASSWORD_STR
        placeholder_label["text"] = ""
    else:
        return
    if event.widget.get() == default_text:
        event.widget.delete(0, tkinter.END)
        event.widget.config(foreground=orig_text_color)


entry_website = tkinter.Entry(textvariable=default_text_web)
orig_text_color = entry_website.cget("foreground")
entry_website.config(foreground=PLACEHOLDER_COLOR, width=48, font=(FONT_NAME, 16, ""), justify="left")
entry_website.bind("<Button-1>", on_click)
entry_website.grid(column=1, columnspan=3, row=2)

# Username Row --------------------------------

username_label = tkinter.Label(text="Email/Username:", font=(FONT_NAME, 16, ""), foreground=LABEL_FONT_COLOR,
                               background=BACKGROUND)
username_label.config(pady=20, justify="left")
username_label.grid(column=0, row=3)

entry_username = tkinter.Entry(textvariable=default_text_username)
entry_username.config(foreground=PLACEHOLDER_COLOR, width=48, font=(FONT_NAME, 16, ""), justify="left")
entry_username.bind("<Button-1>", on_click)
entry_username.grid(column=1, columnspan=3, row=3)

# Password Row --------------------------------

password_label = tkinter.Label(text="Password:", font=(FONT_NAME, 16, ""), foreground=LABEL_FONT_COLOR,
                               background=BACKGROUND)
password_label.config(pady=20, justify="left")
password_label.grid(column=0, row=4)

entry_password = tkinter.Entry(textvariable=default_text_password)
entry_password.config(foreground=PLACEHOLDER_COLOR, width=48, font=(FONT_NAME, 16, ""), justify="left",
                      state="disabled")
entry_password.bind("<Button-1>", on_click)
entry_password.grid(column=1, columnspan=3, row=4)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def own_pass():
    entry_password.config(state="normal")
    default_text_password.set(DEFAULT_PASSWORD_STR)
    save_button.configure(state="normal", fg=SAVE_NORMAL_FG, bg=SAVE_NORMAL_BG)
    placeholder_label["text"] += "Be aware that you're an adult, \nthere's no validation! (yet)'\n"


def random_pass():
    entry_password.config(state="disabled")
    save_button.configure(state="normal", fg=SAVE_NORMAL_FG, bg=SAVE_NORMAL_BG)
    randompass = tkinter.StringVar()
    randompass.set(password.random_pass())
    entry_password["textvariable"] = randompass
    entry_password.config(fg=orig_text_color)
    placeholder_label["text"] = ""


def memorable():
    entry_password.config(state="disabled")
    save_button.configure(state="normal", fg=SAVE_NORMAL_FG, bg=SAVE_NORMAL_BG)
    memorablepass = tkinter.StringVar()
    memorablepass.set(password.memorable())
    entry_password["textvariable"] = memorablepass
    entry_password.config(fg=orig_text_color)
    placeholder_label["text"] = ""


own_button = tkmacosx.Button(root, text="Choose \nmy Own", font=(FONT_NAME, 16, ""), command=own_pass,
                             padx=15, pady=4, bg=GENERATE_NORMAL_BG, fg=GENERATE_NORMAL_FG, justify="left",
                             activebackground=GENERATE_ACTIVE_BG, activeforeground=GENERATE_ACTIVE_FG, borderless=1,
                             focuscolor='', width=140)
own_button.grid(column=1, row=5)

random_button = tkmacosx.Button(root, text="Generate \nRandom", font=(FONT_NAME, 16, ""), command=random_pass, padx=10,
                                pady=4, bg=GENERATE_NORMAL_BG, fg=GENERATE_NORMAL_FG, justify="left",
                                activebackground=GENERATE_ACTIVE_BG, activeforeground=GENERATE_ACTIVE_FG,
                                borderless=1, focuscolor='', width=140)
random_button.grid(column=2, row=5)

memorable_button = tkmacosx.Button(root, text="Generate \nMemorable", font=(FONT_NAME, 16, ""), padx=10, pady=4,
                                   command=memorable, bg=GENERATE_NORMAL_BG, fg=GENERATE_NORMAL_FG,
                                   activebackground=GENERATE_ACTIVE_BG, activeforeground=GENERATE_ACTIVE_FG,
                                   borderless=1, focuscolor='', justify="left", width=140)
memorable_button.grid(column=3, row=5)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# Checking conditions for saving --------------------------------


def is_copy_checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state_copy.get())
    global is_copy_checked
    is_copy_checked = checked_state_copy.get()
    if is_copy_checked == 1:
        print("copy, pls")


def exit_checkbutton_used():
    global is_exit_checked
    is_exit_checked = checked_state_exit.get()
    if is_exit_checked == 1:
        print("exit, pls")


# Copy to Clipboard Checkbox --------------------------------

is_copy_checked = 0
checked_state_copy = tkinter.IntVar()
is_copy = tkinter.Checkbutton(text="Copy to the Clipboard", variable=checked_state_copy,
                              command=is_copy_checkbutton_used, bg=BACKGROUND, fg=LABEL_FONT_COLOR, pady=20,
                              font=(FONT_NAME, 16, ""), justify="left")
checked_state_copy.get()
is_copy.grid(column=2, row=6)

# Exit on Save Checkbox --------------------------------

is_exit_checked = 0
checked_state_exit = tkinter.IntVar()
is_exit = tkinter.Checkbutton(text="Exit on Save", variable=checked_state_exit, command=exit_checkbutton_used,
                              bg=BACKGROUND, fg=LABEL_FONT_COLOR, pady=20, font=(FONT_NAME, 16, ""), justify="left")
checked_state_exit.get()
is_exit.grid(column=3, row=6)


# Methods before Save --------------------------------


def set_placeholders_text():
    print("I'am here - resetting text")
    default_text_web.set("Type the Website URL Here")
    default_text_username.set("Type your Email/Username Here")
    default_text_password.set("Your Password")
    entry_password["textvariable"] = default_text_password


def set_placeholders_color():
    print("I'am here - set placeholder color")
    entry_website.config(fg=PLACEHOLDER_COLOR)
    entry_username.config(fg=PLACEHOLDER_COLOR)
    entry_password.config(fg=PLACEHOLDER_COLOR)


# Save --------------------------------

def save_pw():
    if entry_website.get() == DEFAULT_WEB_STR or entry_website.get() == "":
        # print(entry_website.get())
        # print(default_text_web.get())
        placeholder_label["text"] += "You'll forget the URL!'\n"
        default_text_web.set("Type the Website URL Here")
        entry_website.config(fg=PLACEHOLDER_COLOR)
        return
    if entry_username.get() == DEFAULT_USERNAME_STR or entry_username.get() == "":
        placeholder_label["text"] += "You won't remember your own name!'\n"
        default_text_username.set("Type your Email/Username Here")
        entry_username.config(fg=PLACEHOLDER_COLOR)
        return
    if entry_password.get() == DEFAULT_PASSWORD_STR or entry_password.get() == "":
        placeholder_label["text"] += "You didn't even set the password!\n"
        entry_password.config(fg=PLACEHOLDER_COLOR)
        entry_password.config(fg=PLACEHOLDER_COLOR)
        return

    if is_copy_checked == 1:
        # print("I'll copy")
        pyperclip.copy(entry_password.get())

    new_entry = '{"URL": ' + entry_website.get() + ',\n"username": ' + entry_username.get() + ',\n"password": ' + entry_password.get() + '},\n'

    with open("save/save.txt", 'a') as save_file:
        save_file.write(new_entry)
        placeholder_label["text"] = ""
    save_button.configure(state="disabled", fg=SAVE_DISABLED_FG, bg=SAVE_DISABLED_BG)

    set_placeholders_text()
    set_placeholders_color()
    root.update()

    if is_exit_checked == 1:
        root.destroy()


# Save Button --------------------------------

save_button = tkmacosx.Button(root, text="Save", font=(FONT_NAME, 16, ""), command=save_pw, padx=50, pady=4,
                              width=365, bg=SAVE_DISABLED_BG, fg=SAVE_NORMAL_FG, disabledforeground=SAVE_NORMAL_FG,
                              disabledbackground=SAVE_DISABLED_BG, activebackground=SAVE_ACTIVE_BG,
                              activeforeground=SAVE_ACTIVE_FG,
                              borderless=1, focuscolor='', justify='left', state="disabled")
save_button.grid(column=2, columnspan=2, row=7)

# Placeholder Label for validation --------------------------------

placeholder_label = tkinter.Label(text="", font=(FONT_NAME, 20, ""), background=BACKGROUND, pady=10,
                                  foreground=WARNING_COLOR, justify="left")
placeholder_label.grid(column=2, columnspan=2, row=8)

root.mainloop()
