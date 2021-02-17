import tkinter as tk
from tkinter import *
import sqlite3 as sql
#Window configuration
mainWindow=tk.Tk()
mainWindow.title("Saglik Kayit Programi")
mainWindow.geometry("1280x720+100+100")
mainWindow.resizable(0, 0)
#-------------------------------------------------------------------
#Database configuration
connection=sql.connect("rehber.db")
connection.execute("CREATE TABLE IF NOT EXISTS Kisiler (AdSoyad,TelNo,Email,KanSekeri,Boy,Kilo,Vki,SekerHastaligi)")

#-------------------------------------------------------------------
#Calculation Functions



#MenuBar functions
def goToSave():
    frameSave.place(height=720, width=1280)
    frameSearch.place_forget()
    frameList.place_forget()
    frameUpdate.place_forget()
    clearSearchBox()
    clearUpdateBox()


def goToSearch():
    frameSearch.place(height=720, width=1280)
    frameSave.place_forget()
    frameList.place_forget()
    frameUpdate.place_forget()
    clearSaveBox()
    clearUpdateBox()
    

def goToList():
    frameList.place(height=720, width=1280)
    frameSearch.place_forget()
    frameSave.place_forget()
    frameUpdate.place_forget()
    clearUpdateBox()
    clearSaveBox()
    clearSearchBox()
    listPersonRefresh()


def goToListUpdate():
    frameUpdate.place(height=720, width=1280)
    frameSearch.place_forget()
    frameSave.place_forget()
    frameList.place_forget()
    entryUpdateName.insert(END,listboxPerson.get(ACTIVE).split("|")[0].rstrip())
    entryUpdateName.configure(state='disabled')
    entryUpdateNumber.insert(END,listboxPerson.get(ACTIVE).split("|")[1].rstrip())
    entryUpdateEmail.insert(END,listboxPerson.get(ACTIVE).split("|")[2].rstrip())
    entryUpdatePrependial.insert(END,listboxPerson.get(ACTIVE).split("|")[3].rstrip())
    entryUpdateHeight.insert(END,listboxPerson.get(ACTIVE).split("|")[4].rstrip())
    entryUpdateWeight.insert(END,listboxPerson.get(ACTIVE).split("|")[5].rstrip())
    clearSaveBox()
    clearSearchBox()

def goToSearchUpdate():
    frameUpdate.place(height=720, width=1280)
    frameSearch.place_forget()
    frameSave.place_forget()
    frameList.place_forget()
    entryUpdateName.insert(END,listboxSearch.get(ACTIVE).split("|")[0].rstrip())
    entryUpdateName.configure(state='disabled')
    entryUpdateNumber.insert(END,listboxSearch.get(ACTIVE).split("|")[1].rstrip())
    entryUpdateEmail.insert(END,listboxSearch.get(ACTIVE).split("|")[2].rstrip())
    entryUpdatePrependial.insert(END,listboxSearch.get(ACTIVE).split("|")[3].rstrip())
    entryUpdateHeight.insert(END,listboxSearch.get(ACTIVE).split("|")[4].rstrip())
    entryUpdateWeight.insert(END,listboxSearch.get(ACTIVE).split("|")[5].rstrip())
    clearSaveBox()
    clearSearchBox()

#-------------------------------------------------------------------
#Frame functions
def savePerson():
    bmi=float(entrySaveWeight.get())/(float(entrySaveHeight.get())*float(entrySaveHeight.get()))
    
    if bmi<=18.4:
        bmiResult="Zayif"
    
    elif bmi>18.4 and bmi<=25.9:
        bmiResult="Normal"
        
    elif bmi>25.9 and bmi<=29.9:
        bmiResult="Fazla Kilolu"

    elif bmi>29.9 and bmi<=34.9:
        bmiResult="Obez(Sinif 1)"

    elif bmi>34.9 and bmi<=44.9:
        bmiResult="Obez(Sinif 2)"
        
    elif bmi>=45:
        bmiResult="Aşırı Obez"


    prependial=float(entrySavePrependial.get())

    if prependial>=50 and prependial<70:
        prependialResult="Hipoglisemi"
    
    elif prependial>=70 and prependial<100:
        prependialResult="Normal"

    elif prependial>=100 and prependial<125:
        prependialResult="GizliSeker"

    elif prependial>=125:
        prependialResult="Diyabet"

    listboxPerson.insert(END,entrySaveName.get()+(30-len(entrySaveName.get()))*" "+"|"+entrySaveNumber.get()+(15-len(entrySaveNumber.get()))*" "+"|"+entrySaveEmail.get()+(20-len(entrySaveEmail.get()))*" "+"|"+entrySavePrependial.get()+(8-len(entrySavePrependial.get()))*" "+"|"+entrySaveHeight.get()+(4-len(entrySaveHeight.get()))*" "+"|"+entrySaveWeight.get()+(4-len(entrySaveWeight.get()))*" "+"|"+bmiResult+(15-len(bmiResult))*" "+"|"+prependialResult)
    connection.execute("insert into Kisiler values (?,?,?,?,?,?,?,?)",
                [entrySaveName.get(),entrySaveNumber.get(),entrySaveEmail.get(),entrySavePrependial.get(),entrySaveHeight.get(),entrySaveWeight.get(),bmiResult,prependialResult])

    connection.commit()

    lblSavedName['text']="Ad Soyad:{}".format(entrySaveName.get())
    lblSavedNumber['text']="Telefon Numarasi:{}".format(entrySaveNumber.get())
    lblSavedEmail['text']="Mail adresi:{}".format(entrySaveEmail.get())
    lblSavedPrepandial['text']="Aclik Kan Sekeri:{}".format(entrySavePrependial.get())
    lblSavedHeight['text']="Boy:{}".format(entrySaveHeight.get())
    lblSavedWeight['text']="Kilo:{}".format(entrySaveWeight.get())
    






def searchPerson():
    listboxSearch.delete(0, END)
    for searchInfo in connection.execute("SELECT * FROM Kisiler WHERE AdSoyad=?",
                       [entrySearchName.get()]):
            listboxSearch.insert(END,searchInfo[0]+(30-len(searchInfo[0]))*" "+"|"+searchInfo[1]+(15-len(searchInfo[1]))*" "+"|"+searchInfo[2]+(20-len(searchInfo[2]))*" "+"|"+searchInfo[3]+(8-len(searchInfo[3]))*" "+"|"+searchInfo[4]+(4-len(searchInfo[4]))*" "+"|"+searchInfo[5]+(4-len(searchInfo[5]))*" "+"|"+searchInfo[6]+(15-len(searchInfo[6]))*" "+"|"+searchInfo[7])

def updatePerson():
    bmi=float(entryUpdateWeight.get())/(float(entryUpdateHeight.get())*float(entryUpdateHeight.get()))
    
    if bmi<=18.4:
        bmiResult="Zayif"
    
    elif bmi>18.4 and bmi<=25.9:
        bmiResult="Normal"
        
    elif bmi>25.9 and bmi<=29.9:
        bmiResult="Fazla Kilolu"

    elif bmi>29.9 and bmi<=34.9:
        bmiResult="Obez(Sinif 1)"

    elif bmi>34.9 and bmi<=44.9:
        bmiResult="Obez(Sinif 2)"
        
    elif bmi>45:
        bmiResult="Aşırı Obez"


    prependial=float(entryUpdatePrependial.get())

    if prependial>=50 and prependial<70:
        prependialResult="Hipoglisemi"
    
    elif prependial>=70 and prependial<100:
        prependialResult="Normal"

    elif prependial>=100 and prependial<125:
        prependialResult="GizliSeker"

    elif prependial>=125:
        prependialResult="Diyabet"

    connection.execute("UPDATE Kisiler SET TelNo=?,Email=?,KanSekeri=?,Boy=?,Kilo=?,Vki=?,SekerHastaligi=? WHERE AdSoyad=?",
                       [entryUpdateNumber.get(),entryUpdateEmail.get(),entryUpdatePrependial.get(),entryUpdateHeight.get(),entryUpdateWeight.get(),bmiResult,prependialResult,entryUpdateName.get()])
               

    connection.commit()
    goToList()


 

def listPersonRefresh():
    listboxPerson.delete(0,'end')
    for personInfo in connection.execute("SELECT * FROM Kisiler"):
        listboxPerson.insert(END,personInfo[0]+(30-len(personInfo[0]))*" "+"|"+personInfo[1]+(15-len(personInfo[1]))*" "+"|"+personInfo[2]+(20-len(personInfo[2]))*" "+"|"+personInfo[3]+(8-len(personInfo[3]))*" "+"|"+personInfo[4]+(4-len(personInfo[4]))*" "+"|"+personInfo[5]+(4-len(personInfo[5]))*" "+"|"+personInfo[6]+(15-len(personInfo[6]))*" "+"|"+personInfo[7])


def deleteSearchPerson():              
    connection.execute("DELETE FROM Kisiler WHERE AdSoyad=? AND TelNo=? AND Email=? AND KanSekeri=? AND Boy=? AND Kilo=? AND Vki=? AND SekerHastaligi=?",
                                                                                                                                         [listboxSearch.get(ACTIVE).split("|")[0].rstrip(),
                                                                                                                                         listboxSearch.get(ACTIVE).split("|")[1].rstrip(),
                                                                                                                                         listboxSearch.get(ACTIVE).split("|")[2].rstrip(),
                                                                                                                                         listboxSearch.get(ACTIVE).split("|")[3].rstrip(),
                                                                                                                                         listboxSearch.get(ACTIVE).split("|")[4].rstrip(),
                                                                                                                                         listboxSearch.get(ACTIVE).split("|")[5].rstrip(),
                                                                                                                                         listboxSearch.get(ACTIVE).split("|")[6].rstrip(),
                                                                                                                                         listboxSearch.get(ACTIVE).split("|")[7].rstrip()])
    connection.commit()
    listboxSearch.delete(ACTIVE)

def deleteListPerson():              
    connection.execute("DELETE FROM Kisiler WHERE AdSoyad=? AND TelNo=? AND Email=? AND KanSekeri=? AND Boy=? AND Kilo=? AND Vki=? AND SekerHastaligi=?",
                                                                                                                                         [listboxPerson.get(ACTIVE).split("|")[0].rstrip(),
                                                                                                                                         listboxPerson.get(ACTIVE).split("|")[1].rstrip(),
                                                                                                                                         listboxPerson.get(ACTIVE).split("|")[2].rstrip(),
                                                                                                                                         listboxPerson.get(ACTIVE).split("|")[3].rstrip(),
                                                                                                                                         listboxPerson.get(ACTIVE).split("|")[4].rstrip(),
                                                                                                                                         listboxPerson.get(ACTIVE).split("|")[5].rstrip(),
                                                                                                                                         listboxPerson.get(ACTIVE).split("|")[6].rstrip(),
                                                                                                                                         listboxPerson.get(ACTIVE).split("|")[7].rstrip()])
    connection.commit()
    listboxPerson.delete(ACTIVE)
 
#-------------------------------------------------------------------
#MenuBar configuration
menuBar=tk.Menu(mainWindow)
mainWindow.config(menu=menuBar)
personMenu=tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Islemler",menu=personMenu)
personMenu.add_command(label="Yeni kisi ekle",command=goToSave)
personMenu.add_command(label="Kisileri listele",command=goToList)
personMenu.add_command(label="Kisi ara",command=goToSearch)
#-------------------------------------------------------------------


#-------------------------------------------------------------------
#Save Frame
frameSave=tk.Frame(mainWindow,background="turquoise3")

lblSavedLast=tk.Label(frameSave,text="Son eklenen kisi:",font="Times 20",bg="turquoise3",fg="snow")
lblSavedLast.place(x=700,y=0)

lblSaveTitle=tk.Label(frameSave,text="Kisi Kaydet",font="Times 20",bg="turquoise3",fg="snow")
lblSaveTitle.place(x=0,y=0)

lblSaveName=tk.Label(frameSave,text="Ad Soyad:",font="Times 20",bg="turquoise3",fg="snow")
lblSaveName.place(x=0,y=50)

lblSavedName=tk.Label(frameSave,text="Ad Soyad:",font="Times 20",bg="turquoise3",fg="snow")
lblSavedName.place(x=700,y=50)

entrySaveName=tk.Entry(frameSave,font="Times 20")
entrySaveName.place(x=220,y=50)

lblSaveNumber=tk.Label(frameSave,text="Telefon Numarasi:",font="Times 20",bg="turquoise3",fg="snow")
lblSaveNumber.place(x=0,y=100)

lblSavedNumber=tk.Label(frameSave,text="Telefon Numarasi:",font="Times 20",bg="turquoise3",fg="snow")
lblSavedNumber.place(x=700,y=100)

entrySaveNumber=tk.Entry(frameSave,font="Times 20")
entrySaveNumber.place(x=220,y=100)

lblSaveEmail=tk.Label(frameSave,text="Mail adresi:",font="Times 20",bg="turquoise3",fg="snow")
lblSaveEmail.place(x=0,y=150)

lblSavedEmail=tk.Label(frameSave,text="Mail adresi:",font="Times 20",bg="turquoise3",fg="snow")
lblSavedEmail.place(x=700,y=150)

entrySaveEmail=tk.Entry(frameSave,font="Times 20")
entrySaveEmail.place(x=220,y=150)

lblSavePrependial=tk.Label(frameSave,text="Aclik Kan Sekeri:",font="Times 20",bg="turquoise3",fg="snow")
lblSavePrependial.place(x=0,y=200)

lblSavedPrepandial=tk.Label(frameSave,text="Aclik Kan Sekeri:",font="Times 20",bg="turquoise3",fg="snow")
lblSavedPrepandial.place(x=700,y=200)

entrySavePrependial=tk.Entry(frameSave,font="Times 20")
entrySavePrependial.place(x=220,y=200)

lblSaveHeight=tk.Label(frameSave,text="Boy:",font="Times 20",bg="turquoise3",fg="snow")
lblSaveHeight.place(x=0,y=250)

lblSavedHeight=tk.Label(frameSave,text="Boy:",font="Times 20",bg="turquoise3",fg="snow")
lblSavedHeight.place(x=700,y=250)

entrySaveHeight=tk.Entry(frameSave,font="Times 20")
entrySaveHeight.place(x=220,y=250)

lblSaveWeight=tk.Label(frameSave,text="Kilo:",font="Times 20",bg="turquoise3",fg="snow")
lblSaveWeight.place(x=0,y=300)

lblSavedWeight=tk.Label(frameSave,text="Kilo:",font="Times 20",bg="turquoise3",fg="snow")
lblSavedWeight.place(x=700,y=300)

entrySaveWeight=tk.Entry(frameSave,font="Times 20")
entrySaveWeight.place(x=220,y=300)

buttonSave=tk.Button(frameSave,text="Kaydet",font="Times 20",command=savePerson)
buttonSave.place(x=0,y=350)
#-------------------------------------------------------------------
#List Frame
frameList=tk.Frame(mainWindow,background="green3")

listboxPerson=Listbox(frameList,font="Consolas",selectmode="extended",width=200)
listboxPerson.place(x=0,y=100)

listTitle=tk.Label(frameList,text="Kayitli Kisiler:",font="Times 20",bg="green3",fg="snow")
listTitle.place(x=0,y=0)

listName=tk.Label(frameList,text="Ad Soyad",font="Times",bg="green3",fg="snow")
listName.place(x=0,y=70)

listNumber=tk.Label(frameList,text="Numara",font="Times",bg="green3",fg="snow")
listNumber.place(x=300,y=70)

listEmail=tk.Label(frameList,text="E-mail",font="Times",bg="green3",fg="snow")
listEmail.place(x=450,y=70)

listPrependial=tk.Label(frameList,text="Kan sekeri",font="Times",bg="green3",fg="snow")
listPrependial.place(x=610,y=70)

listHeight=tk.Label(frameList,text="Boy",font="Times",bg="green3",fg="snow")
listHeight.place(x=700,y=70)

listWeight=tk.Label(frameList,text="Kilo",font="Times",bg="green3",fg="snow")
listWeight.place(x=740,y=70)

listBms=tk.Label(frameList,text="Vucut kitle indexi",font="Times",bg="green3",fg="snow")
listBms.place(x=800,y=70)


listDiabetes=tk.Label(frameList,text="Seker Hastaligi",font="Times",bg="green3",fg="snow")
listDiabetes.place(x=950,y=70)


buttonListUpdate=tk.Button(frameList,text="Guncelle",font="Times 20",command=goToListUpdate)
buttonListUpdate.place(x=0,y=320)

buttonListDelete=tk.Button(frameList,text="Sil",font="Times 20",command=deleteListPerson)
buttonListDelete.place(x=200,y=320)


#-------------------------------------------------------------------
#Search Frame
frameSearch=tk.Frame(mainWindow,background="aquamarine2")

lblSearchTitle=tk.Label(frameSearch,text="Kisi Ara",font="Times 15",bg="aquamarine2",fg="snow")
lblSearchTitle.place(x=0,y=0)

searchName=tk.Label(frameSearch,text="Ad Soyad",font="Times",bg="aquamarine2",fg="snow")
searchName.place(x=0,y=170)

searchNumber=tk.Label(frameSearch,text="Numara",font="Times",bg="aquamarine2",fg="snow")
searchNumber.place(x=300,y=170)

searchEmail=tk.Label(frameSearch,text="E-mail",font="Times",bg="aquamarine2",fg="snow")
searchEmail.place(x=450,y=170)

searchPrependial=tk.Label(frameSearch,text="Kan sekeri",font="Times",bg="aquamarine2",fg="snow")
searchPrependial.place(x=610,y=170)

searchHeight=tk.Label(frameSearch,text="Boy",font="Times",bg="aquamarine2",fg="snow")
searchHeight.place(x=700,y=170)

searchWeight=tk.Label(frameSearch,text="Kilo",font="Times",bg="aquamarine2",fg="snow")
searchWeight.place(x=740,y=170)

searchBms=tk.Label(frameSearch,text="Vucut kitle indexi",font="Times",bg="aquamarine2",fg="snow")
searchBms.place(x=800,y=170)


searchDiabetes=tk.Label(frameSearch,text="Seker Hastaligi",font="Times",bg="aquamarine2",fg="snow")
searchDiabetes.place(x=950,y=170)


lblSearchName=tk.Label(frameSearch,text="Ad Soyad:",font="Times 15",bg="aquamarine2",fg="snow")
lblSearchName.place(x=0,y=50)

entrySearchName=tk.Entry(frameSearch,font="Times 15")
entrySearchName.place(x=220,y=50)

buttonSearch=tk.Button(frameSearch,text="Kisi Ara",font="Times 15",command=searchPerson)
buttonSearch.place(x=0,y=100)

buttonSearchUpdate=tk.Button(frameSearch,text="Kisi Guncelle",font="Times 15",command=goToSearchUpdate)
buttonSearchUpdate.place(x=200,y=450)

buttonSearchDelete=tk.Button(frameSearch,text="Kisi Sil",font="Times 15",command=deleteSearchPerson)
buttonSearchDelete.place(x=400,y=450)

listboxSearch=Listbox(frameSearch,font="Consolas",selectmode="extended",width=200)
listboxSearch.place(x=0,y=200)


#-------------------------------------------------------------------
#update frame
frameUpdate=tk.Frame(mainWindow,background="aquamarine2")

lblUpdateTitle=tk.Label(frameUpdate,text="Kisi Guncelle",font="Times 20",bg="aquamarine2",fg="snow")
lblUpdateTitle.place(x=0,y=0)

lblUpdateName=tk.Label(frameUpdate,text="Ad Soyad:",font="Times 20",bg="aquamarine2",fg="snow")
lblUpdateName.place(x=0,y=50)

entryUpdateName=tk.Entry(frameUpdate,font="Times 20")
entryUpdateName.place(x=220,y=50)

lblUpdateNumber=tk.Label(frameUpdate,text="Telefon Numarasi:",font="Times 20",bg="aquamarine2",fg="snow")
lblUpdateNumber.place(x=0,y=100)

entryUpdateNumber=tk.Entry(frameUpdate,font="Times 20")
entryUpdateNumber.place(x=220,y=100)

lblUpdateEmail=tk.Label(frameUpdate,text="Mail adresi:",font="Times 20",bg="aquamarine2",fg="snow")
lblUpdateEmail.place(x=0,y=150)

entryUpdateEmail=tk.Entry(frameUpdate,font="Times 20")
entryUpdateEmail.place(x=220,y=150)

lblUpdatePrependial=tk.Label(frameUpdate,text="Aclik Kan Sekeri:",font="Times 20",bg="aquamarine2",fg="snow")
lblUpdatePrependial.place(x=0,y=200)

entryUpdatePrependial=tk.Entry(frameUpdate,font="Times 20")
entryUpdatePrependial.place(x=220,y=200)

lblUpdateHeight=tk.Label(frameUpdate,text="Boy:",font="Times 20",bg="aquamarine2",fg="snow")
lblUpdateHeight.place(x=0,y=250)

entryUpdateHeight=tk.Entry(frameUpdate,font="Times 20")
entryUpdateHeight.place(x=220,y=250)

lblUpdateWeight=tk.Label(frameUpdate,text="Kilo:",font="Times 20",bg="aquamarine2",fg="snow")
lblUpdateWeight.place(x=0,y=300)

entryUpdateWeight=tk.Entry(frameUpdate,font="Times 20")
entryUpdateWeight.place(x=220,y=300)

buttonUpdatePerson=tk.Button(frameUpdate,text="Guncelle",font="Times 20",command=updatePerson)
buttonUpdatePerson.place(x=0,y=350)

#-------------------------------------------------------------------
#Load listbox
for personInfo in connection.execute("SELECT * FROM Kisiler"):
    listboxPerson.insert(END,personInfo[0]+(30-len(personInfo[0]))*" "+"|"+personInfo[1]+(15-len(personInfo[1]))*" "+"|"+personInfo[2]+(20-len(personInfo[2]))*" "+"|"+personInfo[3]+(8-len(personInfo[3]))*" "+"|"+personInfo[4]+(4-len(personInfo[4]))*" "+"|"+personInfo[5]+(4-len(personInfo[5]))*" "+"|"+personInfo[6]+(15-len(personInfo[6]))*" "+"|"+personInfo[7])
#-------------------------------------------------------------------
#clear entry boxes
def clearUpdateBox():
    entryUpdateName.configure(state='normal')
    entryUpdateName.delete(0,'end')
    entryUpdateNumber.delete(0,'end')
    entryUpdateEmail.delete(0,'end')
    entryUpdatePrependial.delete(0,'end')
    entryUpdateHeight.delete(0,'end')
    entryUpdateWeight.delete(0,'end')

def clearSearchBox():
    entrySearchName.delete(0,'end')
    listboxSearch.delete(0,'end')

def clearSaveBox():
    entrySaveName.delete(0,'end')
    entrySaveNumber.delete(0,'end')
    entrySaveEmail.delete(0,'end')
    entrySavePrependial.delete(0,'end')
    entrySaveHeight.delete(0,'end')
    entrySaveWeight.delete(0,'end')

goToList()
mainWindow.mainloop()
