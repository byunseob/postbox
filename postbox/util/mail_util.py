import logging
import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

logger = logging.getLogger("mail")


def send_mail(from_email, to_email, subject, content, content_type, alias, file=None, cc=None):
    smtp = smtplib.SMTP_SSL(os.environ.get('SMTP', None))
    try:
        smtp.ehlo()
        password = os.environ.get('PASSWORD', None)
        account = os.environ.get('ACCOUNT', None)
        smtp.login(account, password)

        msg = MIMEBase('multipart', 'mixed')
        content = MIMEText(content, content_type, _charset="utf-8")
        msg['Subject'] = subject
        msg['From'] = f'{alias} <{from_email}>'
        if isinstance(to_email, list):
            msg['To'] = ','.join(to_email)
        else:
            msg['To'] = to_email

        if cc:
            if isinstance(cc, list):
                msg['Cc'] = ','.join(cc)
            else:
                msg['Cc'] = cc

        msg.attach(content)

        if file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            f'attachment;filename={file.filename}')
            msg.attach(part)

        smtp.sendmail(from_email, to_email, msg.as_string())
    except smtplib.SMTPException as e:
        logger.error(e)
        raise e
    finally:
        smtp.quit()
