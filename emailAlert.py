import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = "Your loving husband"
    user = "YourEmail@gmail.com"
    password = "YouPassword" #need to use Google 2-step verification

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    email_alert("test subject", "test body", "YourTestMail@gmail.com")


