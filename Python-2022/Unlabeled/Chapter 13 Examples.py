import tkinter

class MyGUI:
    
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.label = tkinter.Label(self.main_window, test = "Hello World!")
        
        self.label.pack()
        
        tkinter.mainloop()
        
my_gui = MyGUI()