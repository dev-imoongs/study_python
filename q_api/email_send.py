# https://hyunmin1906.tistory.com/276
import smtplib, ssl
def email_send(send_email_text: str = ''):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "help1234.im@gmail.com"
    receiver_email = "help1234.im@gmail.com"
    password = "eceyjkzlglfkhzfp"
    message = send_email_text

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

