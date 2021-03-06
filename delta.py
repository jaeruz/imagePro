#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 24, 2020 12:13:38 PM CST  platform: Windows NT

import sys
from charlie import improc
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import delta_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    delta_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    delta_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def clicked(e1,e2):
    v = e1
    d= e2
    improc(v,float(d))
    root.destroy()
    
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family Consolas -size 30 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("800x600+558+236")
        top.minsize(148, 1)
        top.maxsize(1000, 1000)
        top.resizable(1, 1)
        top.title("Pedestrian Detector")
        top.configure(background="#408080")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.1, rely=0.0, relheight=0.992, relwidth=0.894)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#77bbbb")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.35, rely=0.185,height=44, relwidth=0.523)
        self.Entry1.configure(background="#d9d9d9")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.056, rely=0.185, height=46, width=182)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#77bbbb")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Consolas} -size 13")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Car Velocity :''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.266, rely=0.622, height=113, width=336)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#408080")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#004040")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Start''')

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.056, rely=0.286, height=46, width=202)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#77bbbb")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Consolas} -size 13")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Distance limit :''')

        self.Entry1_2 = tk.Entry(self.Frame1)
        self.Entry1_2.place(relx=0.35, rely=0.286,height=44, relwidth=0.523)
        self.Entry1_2.configure(background="#d9d9d9")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="-family {Courier New} -size 10")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")

        self.menubar = tk.Menu(top,font=font9,bg='#408080',fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.0, rely=0.0, relheight=1.092, relwidth=0.106)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#326363")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Button1.configure(command=lambda:clicked(self.Entry1.get(),self.Entry1_2.get()))

if __name__ == '__main__':
    vp_start_gui()





