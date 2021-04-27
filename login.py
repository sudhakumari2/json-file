from tkinter import *
import tkinter.messagebox as mb
class loginak(frame):
    def _init_(self,master):
        self.label_username=label(self,text='username',front=("times new roman",15))
        self.label_password=label(self,text='password',front=("times new roman",15))
        self.entry_username=entry(self)
        self.entry_password=entry(self)
        self.label_username.grid(raw=0,stickey=E)
        self.label_password.grid(raw=1,stickey=E)
        self.label_username.grid(raw=0,column=1)
        self.label_password.grid(raw=1,column=1)
        self.button=button(self,text='login',command=self.login)
        self.button.grid(columnspan=2)
        self.pack()
        def login(self):
            username=self.entry_username.get()
            password=self.entry_password.get()
            if username=='ak' and password=='admin':
                mb.showinfo("login","login sucessful")
            else:
                mb.showinfo("login","login failed")
ak=tk()
login=loginak(ak)
ak.mainloop()
        