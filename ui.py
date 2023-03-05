from tkinter import *
import easygui
import os
import shutil
import predict
import _pickle as pickle

allpaths=[]
filePathList = []
students = []
class Tapp(Frame):
        def __init__(self,master):
                super(Tapp,self).__init__(master)
                self.pack()
                self.wid()
                self.red = ""
                self.tar = ""

        def wid(self):
                self.id=StringVar()
                self.id.set(None)

                self.sidebar = Text(self, bg='white', width=30,height=45,\
                             relief='sunken', borderwidth=2)
                self.sidebar.pack(expand=True, fill='both', side='left', anchor='nw')
                #self.sidebar.insert(END,"jjWHUHFAJGHA")

                Button(self,text="Link Data to Test", command= self.reduce).pack(padx=30,pady=30,side=TOP)

                Button(self,text="Link Target Output", command= self.target).pack(padx=30,pady=30,side=TOP)

                Button(self,text="Predict", command= self.predict_test).pack(padx=30,pady=30,side=TOP)

                Button(self,text="Understanding Dataset", command= self.ds).pack(padx=30,pady=30,side=TOP)

        def reduce(self):
                self.red=easygui.fileopenbox()


        def target(self):
                self.tar=easygui.fileopenbox()

        def predict_test(self):
                result = predict.getResult(self.red,self.tar)
                string = ""
                for line in result:
                        string = string + line + "\n"
                self.sidebar.insert(END,string)

        def ds(self):
                import datasetUI.py

r2=Tk()
r2.title("PDF Editor")
a=Tapp(r2)
r2.mainloop()
