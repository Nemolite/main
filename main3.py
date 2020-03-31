# -*- coding: utf-8 -*-
import smtplib
def mail(sender, subject, message, to):
    smtp_server = 'smtp.mail.ru'
    sender = 'g30032020@mail.ru'
    smtp_port = 25
    smtp_pasword = 'QAZwsx!@#456'
    mail_lib = smtplib.SMTP(smtp_server, smtp_port)
    mail_lib.login(sender, smtp_pasword)
    # В случае если функции передан не список с получателями
    # а обычную строку
    if isinstance(to, str):
        to = ','.join(to)
    msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/html; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (sender, to, subject)
    msg += message
    mail_lib.sendmail(sender, to, msg)
# отправляем письмо
message = """
Привет из Python!
"""
mail('g30032020@mail.ru', 'Yeah Bitch! Magnets!', message, 'g30032020@mail.ru')