"""
Python 3.7.6
Yagmail is used to send emails.
It can send mails ONLY from Gmail account to any other email provider.
Tested and working example.

"""



import yagmail

yag = yagmail.SMTP(user='your_email@gmail.com',password='your_email_password')
content = ['hello']
yag.send(to='whateveremail@hotmail.com', subject='Hey there', contents=content)
