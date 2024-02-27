import pyshorteners
import pyperclip
from tkinter import *

def shorten_url():
    long_url = long_url_entry.get()
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    short_entry.insert(0, string=f"{short_url}")
    pyperclip.copy(short_url)


window = Tk()
window.title("URL Shortener")
window.config(pady=20, padx=20, bg="white")

canvas = Canvas(height=200, width=700, highlightthickness=0, bg="white")
url_image = PhotoImage(file="images/img.png")
canvas.create_image(350, 100, image=url_image)
canvas.grid(row=0, column=0, columnspan=2)

long_label = Label(text="Enter URL: ", width=30, anchor="e", bg="white")
long_label.grid(row=1, column=0)
long_url_entry = Entry(width=50, takefocus=1, justify="left", highlightthickness=2)
long_url_entry.grid(row=1, column=1)

short_label = Label(text="Shortened URL: ", width=30, anchor="e", bg="white", pady=10)
short_label.grid(row=2, column=0)
short_entry = Entry(width=50, justify="left", highlightthickness=2)
short_entry.grid(row=2, column=1)

shorten_button = Button(text="Shorten URL", command=shorten_url, bg="white", highlightthickness=0)
shorten_button.grid(row=3, column=0, columnspan=2)


window.mainloop()