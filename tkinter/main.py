from tkinter import Tk, ttk
from tkinter.constants import NSEW

class MainWindow():
    def __init__(self):
        self.root = Tk()
        self.button_salir = ttk.Button(self.root, text='Salida', command=self.cuando_haga_click)

        self.button_salir.grid(column=0, row=0, sticky=(NSEW))
        self.root.mainloop()

    def cuando_haga_click(self):
        print("Hice click")

def main():
    MainWindow()
    return 0

if __name__ == "__main__":
    main()