#This is a template code. Please change to applicable command, email, etc base on what user needs.
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import subprocess

command = "s3cmd sync -v -r /Users/anh.phan/Documents/concur s3://it.config.backups"
process = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
data,error = process.communicate()[0]
to_user = "anh.phan@chartboost.com"
from_user = "sa_s3backupalert@chartboost.com"
smtpconnect = smtplib.SMTP("aspmx.l.google.com",25)
'''smtpconnect.ehlo()
smtpconnect.starttls()
smtpconnect.ehlo()
smtpconnect.login(from_user,password)
'''
message = MIMEMultipart()
message['From'] = from_user
message['To'] = to_user

if error is None and "ERROR" in data:
    message['Subject'] = "Backup is completed successfully!"
else:
    message['Subject'] = "Backup is not completed successfully!"

bodyEmail = "Here is the log:\n\n"+data
message.attach(MIMEText(bodyEmail,'plain'))
text = message.as_string()
smtpconnect.sendmail(from_user,to_user,text)
smtpconnect.quit()
