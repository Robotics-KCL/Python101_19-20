import smtplib, ssl
from templates import get_templates
from multiprocessing import Pool, cpu_count

processes = cpu_count() - 1

templates = get_templates()
port = 587  # For starttls
smtp_server = "smtp.gmail.com"

login = open('login.txt')

sender_email = login.readline()
password = login.readline()
login.close()

lst = open('test.csv').readlines()
lst = [x.strip().split(',') for x in lst]
context = ssl.create_default_context()

def send_emails(rec):
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.login(sender_email, password)
        cnt = 1
        first = rec[0]
        last = rec[1]
        email = rec[2]
        for template in templates:
            print('Sending email no. {} to {}!'.format(cnt, email))
            server.sendmail(sender_email, email, template.format(first, last))
            cnt += 1
    return 0

with Pool(processes=processes) as pool:
    print('Starting work!')
    pool.map(send_emails, lst)
    print('Done')
