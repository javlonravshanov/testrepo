from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="savig'", message="Kicha awqom savig'da ayag'im tavig'di ayag'iga uwqab kitti boku")
    #messagebox.showwarning(title="savig'", message="Kicha awqom savig'da ayag'im tavig'di ayag'iga uwqab kitti boku")
    #messagebox.showerror(title="savig'", message="Kicha awqom savig'da ayag'im tavig'di ayag'iga uwqab kitti boku")
    
    #if messagebox.askokcancel(title='ask ok cancel', message="Taviqqa uwqab davom itasammi?"):
        #print("Tavig'akansa")
    #else:
        #print("G'irt tavig'akansa")

    #if messagebox.askretrycancel(title='ask ok cancel', message="Taviqqa uwqab davom itasammi?"):
         #print("Tavig'akansa")
    #else:
        #print("G'irt tavig'akansa")


    #if messagebox.askyesno(title='ask ok cancel', message="Tavig'misan?"):
        #print("Tavig'akansa")
    #else:
        #print("G'irt tavig'akansa")

    messagebox.askyesnocancel(title='ask ok cancel', message="Tavig'misan?")


window = Tk()

button = Button(window,
                text="Click me",
                command = click)
button.pack()

window.mainloop()