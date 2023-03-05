from tkinter import *
from tkinter import ttk
import classes
import mongoInteractReducedFeatures


class HomeFrame(Frame):
    def __init__(self,master):
        super(HomeFrame,self).__init__(master)
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.pack()
        self.createWidgets()

    def getFeatureCode(self,selectedFeature):
        if(selectedFeature == "Age"):
            return("0")
        elif(selectedFeature == "Weight"):
            return("3")
        else:
            return("13")
    def getClassCode(self,selectedClass):
        if(selectedClass == "Normal"):
            return(1)
        elif(selectedClass == "Ischemic changes (Coronary Artery)"):
            return(2)
        elif(selectedClass == "Old Anterior Myocardial Infarction"):
            return(3)
        elif(selectedClass == "Old Inferior Myocardial Infarction"):
            return(4)
        elif(selectedClass == "Sinus tachycardia"):
            return(5)
        elif(selectedClass == "Sinus bradycardia"):
            return(6)
        elif(selectedClass == "Ventricular Premature Contraction (PVC)"):
            return(7)
        elif(selectedClass == "Supraventricular Premature Contraction"):
            return(8)
        elif(selectedClass == "Left bundle branch block"):
            return(9)
        elif(selectedClass == "Right bundle branch block"):
            return(10)
        elif(selectedClass == "Left ventricle hypertrophy"):
            return(11)
        elif(selectedClass == "Atrial Fibrillation or Flutter"):
            return(12)
        else:
            return(13)
    def minClicked(self,selectedClass,selectedFeature,displayBox):
        c = self.getClassCode(selectedClass)
        f = self.getFeatureCode(selectedFeature)
        res = mongoInteractReducedFeatures.getMinFeature(c,f)
        displayBox.delete('1.0', END)
        displayBox.insert('1.0', str(res))

    def maxClicked(self,selectedClass, selectedFeature,displayBox):
        c = self.getClassCode(selectedClass)
        f = self.getFeatureCode(selectedFeature)
        res = mongoInteractReducedFeatures.getMaxFeature(c,f)
        displayBox.delete('1.0', END)
        displayBox.insert('1.0', str(res))

    def avgClicked(self,selectedClass, selectedFeature,displayBox):
        c = self.getClassCode(selectedClass)
        f = self.getFeatureCode(selectedFeature)
        res = mongoInteractReducedFeatures.getAvgFeature(c,f)
        displayBox.delete('1.0', END)
        displayBox.insert('1.0', str(res))

    def createWidgets(self):
        selectedClass = StringVar(self)
        selectedClass.set('Choose a Class')
        classList = ["Normal","Ischemic changes (Coronary Artery)", "Old Anterior Myocardial Infarction", "Old Inferior Myocardial Infarction", "Sinus tachycardia", "Sinus bradycardia",
            "Ventricular Premature Contraction (PVC)", "Supraventricular Premature Contraction", "Left bundle branch block", "Right bundle branch block", "Left ventricle hypertrophy",
            "Atrial Fibrillation or Flutter", "Others"]
        classes = OptionMenu(self,selectedClass,*classList)
        classes.pack(side = TOP, padx=40,pady=20)

        selectedFeature = StringVar(self)
        selectedFeature.set('Choose a Feature')
        featureList = ["Age","Weight","heart rate"]
        features = OptionMenu(self,selectedFeature,*featureList)
        features.pack(side = TOP, padx=40,pady=20)

        displayBox = Text(self,width=10,font="Helvetica 15 bold",height=1)
        displayBox.pack(padx=30,pady=40,side=TOP)
        displayBox.insert('1.0',"Hello")

        Button(self,text='GET MIN',width=10,font="Helvetica 15 bold",height=1,anchor=CENTER,\
               command=lambda : self.minClicked(selectedClass.get(),selectedFeature.get(),displayBox)).pack(padx=40,pady=40,side=LEFT)
        Button(self,text='GET MAX',width=10,font="Helvetica 15 bold",height=1,anchor=CENTER,\
               command=lambda : self.maxClicked(selectedClass.get(),selectedFeature.get(),displayBox)).pack(padx=40,pady=40,side=LEFT)
        Button(self,text='GET AVG',width=10,font="Helvetica 15 bold",height=1,anchor=CENTER,\
               command=lambda : self.avgClicked(selectedClass.get(),selectedFeature.get(),displayBox)).pack(padx=40,pady=40,side=LEFT)

root=Tk()
root.geometry('700x400')
root.resizable(width=False,height=False)
root.configure(background='#ffffff')

hf=HomeFrame(root)
root.mainloop()
