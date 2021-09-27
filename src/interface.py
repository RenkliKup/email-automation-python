from tkinter import *
from tkinter import filedialog
import os
from smtp import Smtp
import threading
import logging
from sql import CompanyDb
mail=Smtp()

logger=logging.getLogger(__name__)
formatter=logging.Formatter("%(lineno)d:%(asctime)s:%(levelname)s")
fileHandler=logging.FileHandler("./log/interface.log")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
class Interface:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("400x400")
        self.files=[]
    def askFileName(self): 

        filename=filedialog.askopenfilename(initialdir="c:/",title="Please select a file")
        self.files.append(filename)
        filesLen=len(self.files)
        attachment_label=Label(text=f"{filesLen} Files")
        attachment_label.place(x=130,y=145)
        mail.setFiles(self.files)
            
            
       
    def mailFrame(self,):
        mail_label=Label(self.window,text="Sender Email:")
        mail_label.place(x=0,y=0)
        client=Label(self.window,text=os.getenv("mail"))
        client.place(x=75,y=0)
        textArea=Text(self.window)
        textArea.place(x=10,y=25,width=300,height=100)

        sendMailButton=Button(self.window,text="Send",command=lambda:self.Sendthreads(textArea))
        sendMailButton.place(x=0,y=140)
        
        
        attachment_button=Button(self.window,text="Attachment",command=lambda:self.askFileName())
        attachment_button.place(x=40,y=140)
        succesDeleteDb=Label(self.window,text="")
        succesDeleteDb.place(x=110,y=170)
        deleteDb_button=Button(self.window,text="DB Delete",command=lambda:[succesDeleteDb.configure(text=f"Deleted {len(CompanyDb().lenDb())} rows"),CompanyDb().deleteTable(),threading.Timer(2,lambda:succesDeleteDb.configure(text="")).start()])
        deleteDb_button.place(x=120,y=140)

        self.window.mainloop()
    def sendMail(self,entry):
        text=str(entry.get("1.0",END)).strip()
        
        result=mail.SendMail(text)
        Label(text=str(result)).place(x=0,y=400)
    def Sendthreads(self,entry):
        t1=threading.Thread(target=lambda:self.sendMail(entry),)
        t1.start()

