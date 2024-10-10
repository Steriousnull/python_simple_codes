from email.message import EmailMessage
import ssl
import smtplib

#your email id and app password
email_sender = ""
email_password = ""

#your reciever mail id
email_reciever = "c24a10.ethical@gmail.com"
subject = "Don't forget to Review"

body = """
Welcome to the world of Python!
"""

# Create the email message object
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject

# Set the body of the email
em.set_content(body)

# Create SSL context for secure connection
context = ssl.create_default_context()

# Establish a connection to the SMTP server and send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
