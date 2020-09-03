"""
!/usr/bin/env python3
__AUTHOR = "JIMOH IDRIS OLANSHILE"
__DATE = "AUG 2020 - till date."
"""
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk
import os as gd, subprocess as sp, time, webbrowser
global relPth
def homeScreen(event):
    def getIt(event):
        def refresh():
            txt1.delete ("1.0", END)
            txt1.insert (INSERT, "To get the Password of any profile, simply copy and paste the User Profile and click the Go button. PS: Click Refresh if you can't find your WIFI network.\n" + "-" * 160 + "\n")
            txt1.insert (INSERT, output)

        def getPass(event):
            ssid = input1.get()
            if ssid == "":mb.showerror ("Error", "Field can't be empty")
            else:
                try:
                    output = sp.check_output ("netsh wlan show profile " + "\"" + ssid + "\"" + " key = clear")
                    n = str(output).rpartition ("Key Content")
                    n = n [2].partition ("\\r\\n")
                    n = n [0].rpartition (": ")
                    p = n [2]
                    root.geometry("880x500+340+100")
                    txt2 = Text (root, width = 26, height = 6)
                    txt2.insert (INSERT, "SSID:\n" + ssid + "\n\nPassword:\n" + p)
                    txt2.place (x = 647, y = 280)
                    txt2.config (state = DISABLED)
                except:
                    mb.showerror ("Error", "Invalid entry, \nMake sure you've copied the SSID correctly!!!")

        output = sp.check_output ("netsh wlan show profile")
        root.geometry("880x500+340+100")
        scrollbar = Scrollbar(root)
        scrollbar.pack ( side = RIGHT, fill = Y )
        txt1 = Text (root, yscrollcommand = scrollbar.set, wrap = WORD)
        txt1.insert (INSERT, "To get the Password of any profile, simply copy and paste the User Profile and click the Go button. PS: Click Refresh if you can't find your WIFI network.\n" + "-" * 160 + "\n")
        txt1.insert (INSERT, output)
        #txt1.insert (INSERT, "\n" + "=" * 80)
        txt1.pack (side = LEFT)
        #txt1.config (state = DISABLED)
        scrollbar.config (command = txt1.yview )
        input1 = StringVar()
        ent = Entry (root, bd = 2, width = 30, textvariable = input1)
        ent.place (x = 660, y = 150)
        ent.focus_set()
        ent.bind ("<Return>", getPass)
        btn = Button (root, text = "Go", command = getPass, bg = "#8e388e", fg = "WHITE")
        btn.place (x = 740, y =190)
        btn = Button (root, text = "Refresh", command = refresh, bg = "#8e388e", fg = "WHITE")
        btn.place (x = 728, y =220)
        
    ########create app menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Export to TXT", command=getIt)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Update", command=getIt)
    helpmenu.add_command(label="Donate", command=getIt)
    helpmenu.add_command(label="About Us", command=getIt)
    helpmenu.add_command(label="How to use", command=getIt)
    root.config (menu=menubar)
    root.configure (background = "#363277")
    root.title ("GLWP - Get Local WiFi Password")
    homBG = PhotoImage (file = relPth + "back.png")
    hLabel = Label (root, image = homBG)
    hLabel.place (x=0, y=0, relwidth=1, relheight=1)
    root.geometry ("610x350+340+200")
    Label (root, text = "Get Local WiFi Password", bg = "#8e388e", fg = "WHITE", font = ("ROBOTO", 15, "bold")).place (x=0,y=0,relwidth=1)
    intro = "The software GLWP was developed and written for educational purposes only. It should only be used on an autorized PC as it is highly illegal to use this software without necessary autorization. The developer or programmer or person thus shall not be held responsible for any atrocities committed with this software. It is solely the user's responsible to use this software legally and within the laws of the state or country he / she resides."
    txt = Text(root, width = 70, height = 7, wrap = WORD)
    txt.insert(INSERT, intro)
    txt.config (state = DISABLED)
    txt.place(x=22, y=60)
    pLab = Label (root, text = "(Click The Button Below or Enter to Proceed)", fg = "BLACK", font = ("ROBOTO", "9"))
    pLab.place (x = 175, y = 250)
    Button (root, command = getIt, text = "Profile Search", bg = "#8e388e", fg = "White", font = ("ROBOTO", 9)).place(x=260, y = 270)
    txt.focus_force()
    txt.bind ("<Return>", getIt)


root = Tk()
root.title ("??")
root.geometry ("610x350+340+200")
splashScreen = PhotoImage (file = relPth + "back.png")
splashLabel = Label (root, image = splashScreen)
splashLabel.focus_set()
splashLabel.bind ("<Return>", homeScreen)
splashLabel.place (x = 0, y = 0, relwidth = 1, relheight = 1)
txtLabel = Label (root, text = "GLWP - Get Local WiFi Password", bg = "#8e398e", font = ("ROBOTO", "12", "bold"), fg = "WHITE")
txtLabel.place (x = 170, y = 130)
txtLabel = Label (root, text = "Developed By Idris Olanshile Jimoh", bg = "#393278", font = ("ROBOTO", "7"), fg = "WHITE")
txtLabel.place (x = 230, y = 330)
txtLabel.bind ("<Button-1>", homeScreen)
root.mainloop ()
