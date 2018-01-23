
import random
from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Application(Frame):

    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.a = {} # sets up dict to contain names and emails
        

    def create_widgets(self):

        self.box_Title = Label(self, text = "Enter person name and email address")
        self.box_Title.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.name_Box = Label(self, text = "Name: ")
        self.name_Box.grid(row = 1, column = 0, sticky = W)
        self.email_Box = Label(self, text = "Email: ")
        self.email_Box.grid(row = 2, column = 0, sticky = W)
        self.name_Ent = Entry(self)
        self.name_Ent.grid(row = 1, column = 1, sticky = W)
        self.email_Ent = Entry(self)
        self.email_Ent.grid(row = 2, column = 1, sticky = W)

        
        self.submit_Button = Button(self, text = "Add names", command = self.getInfo)
        self.submit_Button.grid(row = 4, column = 0, sticky = W)
        self.draw_Button = Button(self, text = "Draw pairs", command = self.secret_Santa)
        self.draw_Button.grid(row = 4, column = 2, sticky = W)

        # Below code creates a button to clear list of names and reset program.
        self.reset_Button = Button(self, text = "Clear names", command = self.reset_Santa)
        self.reset_Button.grid(row = 5, column = 0, sticky = W)
        

    def getInfo(self):

        name = self.name_Ent.get()
        email = self.email_Ent.get()

        self.a[name] = email
        self.name_Ent.delete(0, END)
        self.email_Ent.delete(0, END)

        return self.a


    def secret_Santa(self):

        # create list of names from dict keys
        # later use name to return email address for match notification

        names = list(self.a.keys())

        
        random.shuffle(names)

        
        match = []  
        for (i, x) in enumerate(names):
            match +=  [x, names[i-1]]

            # EMAIL SECTION
            my_address = "EMAIL@gmail.com"   # replace with own email address.
            to_address = self.a[x]
            msg = MIMEMultipart()
            msg['From'] = my_address
            msg['To'] = to_address
            msg['Subject'] = "Secret Santa Draw Results"
            body = """Dear %s,
            Congratulations, your match for this year's Secret Santa is %s
            Please have your gift ready for exchange on the 25th December and
            remember to stick within the €80 budget.

            Merry Christmas,
            Secret Santa Team"""%(x, names[i-1])
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(my_address, "PASSWORD")  # replace with password for above email address.
            text = msg.as_string()
            server.sendmail(my_address, to_address, text)
            server.quit()
        
        # write match results out to a file as confirmation.
        file = open("Results_backup.txt", "w")
        file.write(str(match))
        file.close()



    def reset_Santa(self):

        # When clear names button pushed this function assigns an empty dictionary to a.

        self.a = {}


   



# Main

root = Tk()
root.title("Conlisk Secret Santa")
root.geometry("300x150")

app = Application(root)

root.mainloop()


   
