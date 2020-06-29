import smtplib

def send_alert(text, weblink, change):
    
    user = 'tedudevelop@gmail.com'
    password = $APP_SECRET
    
    sent_from = 'tedudevelop@gmail.com'
    to = ['tedudevelop@gmail.com', 'tdu@planning.nyc.gov', 'NMOORE@planning.nyc.gov', 'DSandler@planning.nyc.gov']
    subject = text.split('.')[0] + ' Reopen Page Updated'
    body = 'the item {0} has been modified.\n\n check {1} for detail'.format(change, weblink)
    
    msg = EmailMessage()

    msg['Subject'] = subject
    msg['From'] = sent_from
    msg['To'] = ", ".join(to)
    msg.set_content(body)


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo() 
    server.login(user, password)
    server.send_message(msg)
    server.close()
    
    print('email sent!')