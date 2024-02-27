import smtplib
import tkinter as tk
import random

MY_MAIL = "Your email id"
PASSWORD = "Your email app-password"
OTP = ""

def generate_otp() -> str:
    global OTP
    OTP = ""
    for x in range(6):
        OTP += f"{random.randint(0, 9)}"
    return OTP


def send_otp():
    verify_status.config(text="Verification status: None")
    otp_entry.delete(0, "end")
    otp = generate_otp()
    receiver = email_entry.get()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(MY_MAIL, PASSWORD)
            server.sendmail(from_addr=MY_MAIL, to_addrs=receiver,
                            msg=f"Subject:OTP Verification code \n\n"
                                f"Your OTP for verification is: {otp}. Do not share this code."
                            )
            otp_status.config(text="OTP status: OTP sent!")
            send_otp_button.config(state="disabled")
            window.after(2000, countdown, 30)
    except Exception:
        otp_status.config(text="Error: Please check for typo in the email.")

def countdown(count):
    if count > 0:
        otp_status.config(text=f"Please wait: {count}s")
        window.after(1000, countdown, count-1)
    else:
        otp_status.config(text="OTP status: None")
        send_otp_button.config(state="active")

def verify_otp():
    user_input = otp_entry.get()
    if user_input == OTP:
        verify_status.config(text="OTP verified!")
    else:
        verify_status.config(text="Verification Failed!")


window = tk.Tk()
window.title("OTP Verification application")
window.config(width=500, height=500, padx=20, pady=20, bg="white")

canvas = tk.Canvas(width=300, height=300, highlightthickness=0, bg="white")
logo_img = tk.PhotoImage(file="images/logo.png")
canvas.create_image(180, 150, image=logo_img)
canvas.grid(row=0, column=1)

email_label = tk.Label(text="Enter E-Mail for OTP verification: ", bg="white")
email_label.grid(row=0+1, column=0)

email_entry = tk.Entry(width=30, takefocus=True)
email_entry.grid(row=0+1, column=1)

send_otp_button = tk.Button(text="Send OTP", width=10, command=send_otp)
send_otp_button.grid(row=0+1, column=2, columnspan=1, padx=10, pady=5)

otp_label = tk.Label(text="Enter OTP for verification: ", width=25, anchor="w", bg="white")
otp_label.grid(row=1+1, column=0)

otp_entry = tk.Entry(width=30)
otp_entry.grid(row=1+1, column=1)

verify_button = tk.Button(text="Verify OTP", width=10, command=verify_otp)
verify_button.grid(row=1+1, column=2)

otp_status = tk.Label(text="OTP status: None", anchor="w", width=20, bg="white")
otp_status.grid(row=0+1, column=3, columnspan=1)

verify_status = tk.Label(text="Verification status: None", anchor="w", width=20, bg="white")
verify_status.grid(row=1+1, column=3, columnspan=1)

window.mainloop()
