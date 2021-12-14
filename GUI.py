import pandas as pd
import tkinter as tk
from tkinter import ttk
import sys
from PIL import ImageTk,Image
from pandastable import Table, TableModel

goodfood= pd.read_csv("../csv/goodfood.csv")
goodfood.drop('Unnamed: 0', axis=1, inplace=True)


cuisinelist=['indian','mexican','thai','japanese','italian','chinese','hungarian','german','vietnamese']

citylist = goodfood.city.unique()


LARGE_FONT=("Times New Roman",24)
SMALL_FONT=("Times New Roman",18)
SMALLER_FONT=("Times New Roman",12)

import json
with open('indexer.json') as f:
    indexer = json.load(f)

global ids
ids=[]

global goodcuisine

def CheckCity(self,controller,cityR):
    self.controller = controller
    if(len(cityR.get())==0):
        popupmsg("Please Enter a Value. Field cannot be Empty","Fill The Field","OK")
        sys.exit(1)
    else:
        if cityR.get().lower() in citylist:
            label1=tk.Label(self,text="Yay!! We have this city in our list. Press the below button to continue.",font=SMALL_FONT)
            label1.pack(pady=10,padx=10)
            Nextbutton=ttk.Button(self,text="Continue",command=lambda:controller.show_frame(SecondPage))                   
            Nextbutton.pack(pady=20,padx=25)            
        else:
            popupmsg("We don't have any such city. Try again.", "City not Present","OK")
            

def CheckCuisine(self,controller,cuisineEnter):
    
    self.controller = controller
    if(len(cuisineEnter.get())==0):
        popupmsg("Please Enter a Value. Field cannot be Empty","Fill The Field","OK")
        sys.exit(1)
    else:
        if cuisineEnter.get().lower() in cuisinelist:
            label1=tk.Label(self,text="Yay!! We have this cuisine in our list. Press the below button to continue.",font=SMALLER_FONT)
            label1.pack(pady=10,padx=10)
            print(cuisineEnter.get())
            
            # global ids
            
            ids = indexer[cuisineEnter.get()][:10]
            print(ids)
            goodcuisine=goodfood[goodfood['business_id'].isin(ids)][['name', 'address', 'city', 'state','senti_polarity']].sort_values('senti_polarity', axis=0, ascending=False)
            # return goodcuisine
            # label=tk.Label(self,text="List of Top 10 Restaurants",font=SMALL_FONT)

            # pt = Table(self,dataframe=goodcuisine, showstatusbar=True)
            # pt.show()
            # table(goodcuisine)

            SU=ttk.Button(self,text="Click here to find top 10 restaurants",command=lambda:table(self,controller,goodcuisine))
            SU.pack(pady=15,padx=15)
            
        else:
            popupmsg("We don't have any such category. Try again.", "Cuisine not Present","OK")

def table(self,controller,goodcuisine):
    print(goodcuisine)
    matter = tk.Label(self, text=str(goodcuisine), font=SMALLER_FONT)
    matter.pack()
    # self.table = pt = Table(dataframe=goodcuisine, showstatusbar=True)
    # pt.show()


def popupmsg(msg,heading,buttonText):
    popup=tk.Tk()
    popup.geometry('500x150')
    popup.wm_title(heading)
    label=tk.Label(popup,text=msg,font=SMALLER_FONT)
    label.pack(side="top",fill="x",pady=20,padx=10)
    b1=ttk.Button(popup,text=buttonText,command=popup.destroy)
    b1.pack()
    popup.mainloop()


class GUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        
        tk.Tk.wm_title(self,"Yelp Dataset Challenge")
        
        
        container=tk.Frame(self) 
        container.pack(side="top",fill="none",expand=False)        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1) #0 is the min size
        
        self.frames={} #Creating an empty dictionary
        
        for F in (SecondPage,FinalPage):
            frame=F(container,self)
            self.frames[F]= frame
            frame.grid(row=0,column=0,sticky="nsew")
        # seld.frames[FinalPage] = FinalPage(container, self)
        self.show_frame(SecondPage)

        
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame): #Inheriting every frame we used
    
    def __init__(self,parent,controller):
        cityEnterV=tk.StringVar()
        tk.Frame.__init__(self,parent) #Parent Class is the GUI class
        
        Wel=tk.Label(self,text="Welcome to Restaurant Recommendation System",font=LARGE_FONT)
        Wel.pack(pady=20,padx=10,fill="none") 
        
        LIFB=tk.Label(self,text="Enter the name of the city",font=SMALL_FONT)
        LIFB.pack(pady=20,padx=10,fill="none") 
        
        nameEnter=tk.Entry(self,bd=0,textvariable=cityEnterV)
        nameEnter.pack()
        
        Nextbutton=ttk.Button(self,text="Check",command=lambda:CheckCity(self,controller,nameEnter))                   
        Nextbutton.pack(pady=25,padx=25,fill="none")


        
        
        
        
        
        
        

class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        cuisineEnterV=tk.StringVar()
        tk.Frame.__init__(self,parent)
        
        Wel=tk.Label(self,text="Welcome to Restaurant Recommendation System",font=LARGE_FONT)
        Wel.pack(pady=20,padx=10,fill="none") 
        
        RHSB=ttk.Label(self,text="Enter the name of the cuisine",font=SMALL_FONT)
        RHSB.pack(pady=10,padx=10) 
        
        global cuisineEnter
        cuisineEnter = tk.Entry(self,bd=0,textvariable=cuisineEnterV)
        print(cuisineEnter.get())
        #cuisineEnterV = cuisineEnterV.lower()
        cuisineEnter.pack()

        Nextbutton=ttk.Button(self,text="Check",command=lambda:CheckCuisine(self,controller,cuisineEnter))                   
        Nextbutton.pack(pady=30,padx=25)
        



class FinalPage(tk.Frame):
        def __init__(self,parent,controller):
            # self.goodcuisine = goodcuisine
            
            # indexer = json.load('indexer.json')
            # print(indexer['chinese'][0])
            print("HELLO")
            print(ids)
            # goodcuisine=goodfood[goodfood['business_id'].isin(ids)][['name', 'address', 'city', 'state','senti_polarity']].sort_values('senti_polarity', axis=0, ascending=False)
            # # goodcuisine = goodfood[(goodfood['category1']).str.contains(cuisineEnter.get()) | (goodfood['category2']).str.contains(cuisineEnter.get()) | (goodfood['category3']).str.contains(cuisineEnter.get()) | (goodfood['category4']).str.contains(cuisineEnter.get()) | (goodfood['category5']).str.contains(cuisineEnter.get()) | (goodfood['category6']).str.contains(cuisineEnter.get()) | (goodfood['category7']).str.contains(cuisineEnter.get()) | (goodfood['category8']).str.contains(cuisineEnter.get())] 
            #                       # | (goodfood['category9']).str.contains(cuisine) | (goodfood['category10']).str.contains(cuisine)]




            # final=goodcuisine
            # print(goodcuisine)
            # for i in goodcuisine.index:
            #     #if goodcuisine.category1[i] == cuisine:
            #     final = goodcuisine[['name', 'address', 'senti_polarity']]

            # f2=final.sort_values('senti_polarity', axis=0, ascending=False).head(10)
            # f1=f2[['name', 'address']]


            # print(goodcuisine)
            goodcuisine=goodfood[goodfood['business_id'].isin(ids)][['name', 'address', 'city', 'state','senti_polarity']].sort_values('senti_polarity', axis=0, ascending=False)
            tk.Frame.__init__(self,parent)
            label=ttk.Label(self,text="List of Top 10 Restaurants",font=SMALL_FONT)

            self.table = pt = Table(self,dataframe=goodcuisine, showstatusbar=True)
            pt.show()
            

app=GUI() #Calling the class
app.geometry('1000x600')
app.configure()
# imgpath = './adarsh/yelp.jpg'
# img = Image.open(imgpath)
# photo = ImageTk.PhotoImage(img)

canvas = tk.Canvas(app, bd=0, highlightthickness=1, width=1250,height=300)
canvas.pack()
# canvas.create_image(550, 230, image=photo)



app.mainloop() #Tkinter functionality
