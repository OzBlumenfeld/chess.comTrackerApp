import smtplib
import os



def send_email_to_user(to, subject, body):
    user = os.environ['USER']
    password = os.environ['PASSWORD']

    sent_from = user
    # to = [user]
    # subject = 'OMG Super Important Message'
    # body = 'Hey, what\'s up?\n\n- You'

    email_text = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()  # optional
        server_ssl.login(user, password)
        server_ssl.sendmail(sent_from, to, email_text)
        server_ssl.close()
        # ...send emails

    except:
        print('Something went wrong...')
        raise
