import smtplib
import random
from email.message import EmailMessage

# Generate a 6-digit OTP
otp = "".join([str(random.randint(0, 9)) for _ in range(6)])

# Set up SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_email = "balvantkushwaha09@gmail.com"
app_password = "boso zohq qvpp vtmu"               #  Use App Password instead of actual password

server.login(from_email, app_password)

# Get recipient email
to_mail = input("Enter your email: ")   


# Create email message
msg = EmailMessage()
msg['Subject'] = "OTP Verification"
msg['From'] = from_email
msg['To'] = to_mail
msg.set_content(f"Your OTP (One Time Password) is: {otp}")

# Send email
server.send_message(msg)
server.quit()

# OTP Verification
input_otp = input("Enter OTP: ")
if input_otp == otp:
    print(" OTP verified successfully!")
else:
    print("Invalid OTP!")