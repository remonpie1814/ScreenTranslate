from tkinter import *
from tkinter import ttk
import threading
import os
from capture_image import capture_area
import image_to_text
import translate
import time

coord = []
area = []
stop_flag = False

def on_click(x, y, button, pressed):
    if pressed:
        coord.append((x,y))

    if not pressed:
        return False

def open_select_area_window(*args):
    def select_area(event):
        if event.num == 1:
            coord.append((event.x,event.y))
        
        if len(coord)>2:
            coord[0],coord[1]=coord[1],coord[2]
            del coord[2:]
        
        if len(coord)==2:
            entry1.delete(0,"end")
            entry1.insert(0,coord[0])
            entry2.delete(0,"end")
            entry2.insert(0,coord[1])
            canvas.delete("all")
            canvas.create_rectangle(coord[0][0],coord[0][1],coord[1][0],coord[1][1],fill="red")

        
    def select_complete(*args):
        if os.path.isfile("savedScreen.png"):
            os.remove("savedScreen.png")
        
        new_win.destroy()
        set_capture_area(coord)
    
    new_win = Tk()
    h = new_win.winfo_screenheight()
    w = new_win.winfo_screenwidth()
    new_win.title("번역할 부분 지정")
    new_win.geometry("%dx%d"%(w,h))
    new_win.wm_attributes('-alpha', 0.8)
    new_win.resizable(False, False)
    canvas = Canvas(new_win, width=w, height=h-100)
    canvas.pack()

    btn = ttk.Button(new_win, text="완료", command=select_complete)
    btn.pack()
    new_win.bind("<Button>",select_area)
    new_win.bind("<Return>",select_complete)
    new_win.bind("<Escape>",lambda e: new_win.destroy())
    new_win.mainloop()

    
def show_translation(target_text=""):
    textbox.delete(0.0,"end")
    textbox.insert(0.0,target_text)

def set_capture_area(coord):
    if coord[0][0]>coord[1][0]:
        coord[0],coord[1]=coord[1],coord[0]
    global area
    area = [coord[0][0],coord[0][1],coord[1][0]-coord[0][0],coord[1][1]-coord[0][1]]

def capture_thread_start(*args):
    global stop_flag
    t0 = threading.Thread(target=lambda: capture_image(),daemon=True)
    stop_flag = False

    t0.start()


def capture_thread_stop(*args):
    global stop_flag
    stop_flag = True

def capture_image():
    
    while not stop_flag:

        is_new = capture_area(area)
        if is_new:
            text = image_to_text.image_to_text('savedScreen.png')
            translated_text = translate.translate(text)
            print("번역 결과: ",translated_text)
            show_translation(translated_text)
        time.sleep(3)
    return
    


    



if __name__ == '__main__':

    root = Tk()
    root.title("번역기")
    root.geometry("720x500")

    mainframe = ttk.Frame(root, padding="3 3 12 12")

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Button(mainframe, text="번역할 부분 지정", command=open_select_area_window).grid(column=1, row=1, sticky=W)
    ttk.Button(mainframe, text="번역", command=capture_thread_start).grid(column=1, row=2, sticky=W)
    entry1 = ttk.Entry(root, width=10 )
    entry1.grid(row=2, column=0)
    
    entry2 = ttk.Entry(root, width=10 )
    entry2.grid(row=2, column=1)
    textbox = Text(root, width=20, height=10,xscrollcommand=ttk.Scrollbar(orient="vertical"))
    textbox.grid(row=1, column=0, columnspan=2,sticky=(W, E),ipadx=100,ipady=100)

    



    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    # press backspace to stop
    root.bind("<BackSpace>", capture_thread_stop)
    root.bind("<Return>", open_select_area_window)
    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()