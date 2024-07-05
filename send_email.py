import smtplib, ssl 




def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "viktor.petrovvt@gmail.com"
    password = "llznvnbfuxdagnqj" 

    context = ssl.create_default_context()
    receiver = "victor.data.host@gmail.com"

    message = """ 
    Hi
    How are you
    Bye !
    """

    with smtplib.SMTP_SSL(host, port , context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)