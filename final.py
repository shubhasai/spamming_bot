from tkinter import *
import threading
m = Tk()
m.title('SPAMMING BOT')
m.geometry("500x500")
m.maxsize(500,500)
ch = "NONE"
name = "hi"
password = "1"
def run():
    word = name
    n = password
    print(word)
    
    print(n)
    def meet():
        import pyautogui
        # import webbrowser as wb
        import time
        time.sleep(35)
        msg = "BOT ACTIVATED"
        # pyautogui.moveTo(1070, 100)
        # pyautogui.click()
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        for i in range(n):

            # pyautogui.moveTo(1070, 100) .
            # pyautogui.click()
            pyautogui.typewrite(word)
            pyautogui.press("enter")
    def whatsapp():
        import pyautogui
        import webbrowser as wb
        import time
        def emoji():
            pyautogui.moveTo(440, 685)
            pyautogui.click() 
            pyautogui.moveTo(445, 495)
            pyautogui.click() 
            pyautogui.click()
            pyautogui.press("enter")
        msg = "Bot Activated"
        clngmsg = "Task Completed sir"
        wb.open("https://web.whatsapp.com/")
        time.sleep(50)
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        for i in range(n):
            pyautogui.typewrite(word)
            time.sleep(1)
            pyautogui.press("enter")
            #emoji()

        #emoji()
        # pyautogui.press("enter")
        pyautogui.typewrite(clngmsg)
        pyautogui.press("enter")
    def sticker():
        import pyautogui
        import time
        time.sleep(10)
        pyautogui.moveTo(440, 685)
        pyautogui.click() 
        pyautogui.moveTo(560, 700)
        pyautogui.click()
        time.sleep(7)

        for i in range(n):
            time.sleep(7)
            x = 560
            for x in range (560,1060,20):
                pyautogui.moveTo(x, 470)
                pyautogui.click()

    if ch == "WHATSAPP":
        whatsapp()
    if ch == "MEET":
        meet()
    if ch == "STICKER IN WHATSAPP":
        sticker()


# bg = PhotoImage(file = "Spamming.png")
# can1 = Canvas( m, width = 550, height= 600)
# can1.pack(fill = "both", expand = True)
# can1.create_image( 0, 0, image = bg,anchor = "nw")
def threading1(): 
    t1= threading.Thread (target = run) 
    t1.start()
def printchoice(event):
    global ch
    ch = variable.get()
name_var=StringVar()
passw_var=IntVar()
variable = StringVar(m)
variable.set("SELECT PLATFORM")
option_menu = OptionMenu(m, variable, "WHATSAPP","MEET","STICKER IN WHATSAPP",command = printchoice)
option_menu.pack()
def msg():
    global name
    name = name_var.get()
    global password
    password=passw_var.get()
    name_var.set("")
    passw_var.set("")

name_label = Label(m, text = 'Message', font=('calibre',10, 'bold'))
name_entry = Entry(m,textvariable = name_var, font=('calibre',10,'normal'))
passw_label = Label(m, text = 'Number of times You want to send', font = ('calibre',10,'bold'))
passw_entry=Entry(m, textvariable = passw_var, font = ('calibre',10,'normal'))
sub_btn= Button(m,text = 'Submit', command = msg)
start_btn= Button(m,text = 'START', command = threading1)
name_label.pack()
name_entry.pack()
passw_label.pack()
passw_entry.pack()
sub_btn.pack()
start_btn.pack()
m.mainloop()

