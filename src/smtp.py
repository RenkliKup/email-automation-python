import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import logging
from HasCompany import hasCompany
from tqdm import tqdm
logger=logging.getLogger(__name__)
formatter=logging.Formatter("%(lineno)d:%(asctime)s:%(levelname)s")
fileHandler=logging.FileHandler("./log/mail.log")
fileHandler.setFormatter(formatter)

class Smtp:
    def __init__(self):
        
        self.sender_mail=os.getenv("mail")
        self.receiver=self.receiverRead()
        self.password=os.getenv("pass")
        self.files=[]
    def receiverRead(self):
        try:    
            with open("src/alicilar.txt",mode="r") as r:
                i=r.read()
            receiver=i.split(" ")
            return receiver 
        except Exception as e:
            logger.error(str(e))
            return False
    def setFiles(self,files):
        self.files=files
    def mailText(self,receiver,text):
    
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_mail
            message['To'] = receiver
            message['Subject'] = 'A test mail sent by Python. It has an attachment.'
            message_text = """
                        %s
                        """.strip() % (text)
            message.attach(MIMEText(message_text,"plain"))
            if len(self.files)>0:
                for f in self.files: 
                    attachment = MIMEApplication(open(f, "rb").read(), _subtype="txt")
                    attachment.add_header('Content-Disposition','attachment', filename=f)
                    message.attach(attachment)
            message=message.as_string()
            
            return message
        except Exception as e:
            logger.error(str(e))
            return False
    def  SendMail(self,text):
        try:
            
            for receiver in tqdm(self.receiver):
                if hasCompany(receiver):
                    self.server=smtplib.SMTP("smtp.gmail.com",port=587)
                    self.server.ehlo()
                    self.server.starttls()
                    self.server.login(self.sender_mail,self.password)
                    self.server.sendmail(receiver,self.sender_mail,self.mailText(receiver,text))
                    self.server.close()
                else:
                    continue
        except Exception as e:
            logger.error(str(e))
            return False
