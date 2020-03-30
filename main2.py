import email

import imaplib

mail = imaplib.IMAP4_SSL('imap.mail.ru')
mail.login('g30032020@mail.ru', 'QAZwsx!@#456')
mail.list()

print(mail.list())

mail.select("inbox")
print(mail.select("inbox"))


