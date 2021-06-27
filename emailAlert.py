import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = "Your loving husband"
    # TODO: Put the email you would like to send the notifications here
    # Need to use Google 2-step verification to get the password
    user = "YourEmail@gmail.com"
    password = "YouPassword" 

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
    
# TODO: Put the email you would like to get the test notifications here
if __name__ == "__main__":
    email_alert("test subject", "test body", "YourTestMail@gmail.com")


