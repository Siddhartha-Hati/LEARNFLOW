import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, message.as_string())

    print(f"Email sent to {to_email} successfully.")

def compose_and_send_email():
    
    
    
    send_email(email_subject, email_body, recipient_email, smtp_server, smtp_port, smtp_username, smtp_password)


scheduled_date = input('Enter the date to schedule the email (YYYY-MM-DD format): ')
scheduled_time = input('Enter the time to schedule the email (HH:MM format): ')


scheduled_datetime = datetime.datetime.strptime(f'{scheduled_date} {scheduled_time}', '%Y-%m-%d %H:%M')


scheduler = BlockingScheduler()


scheduler.add_job(compose_and_send_email, 'date', run_date=scheduled_datetime)

email_subject = input('Enter email subject: ')
email_body = input('Enter email body: ')
recipient_email = input('Enter recipient email address: ')
smtp_server = input('Enter SMTP server name: ')
smtp_port = int(input('Enter SMTP port number: '))
smtp_username = input('Enter sender\'s email address: ')
smtp_password = input('Enter sender\'s app password: ')
scheduler.start()
