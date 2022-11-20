# Written by Curtis Newton

try:
    import tkinter, sys, webbrowser
    from tkinter import messagebox, filedialog
except ImportError: print("Sorry, can´t find required libraries.", "", "", file=sys.stderr)

class MainWindow(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.textArea, self.menuBar, self.menu, self.filename = None, None, None, None
        self.title("NTextEditor")
        self.iconbitmap("resources/icon.ico")
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.create_widgets()
        self.config(menu=self.menuBar)
        self.mainloop()

    def quit(self) -> None:
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?", icon = "warning"):
            self.destroy()
            quit()

    def show_credits(self) -> None:
        messagebox.showinfo("About...", "NTextEditor v2.0\nWritten in Python by Curtis Newton\n")
        webbrowser.open_new_tab("https://github.com/CaptainFuture-CN")

    def open_file(self) -> None:
        self.filename = filedialog.askopenfilename(title="NTextEditor - Open a file", initialdir="/")
        self.textArea.insert("1.0", open(self.filename, "r").read())

    def create_widgets(self) -> None:
        self.textArea = tkinter.Text(self)
        self.menuBar = tkinter.Menu(self)

        self.menu = tkinter.Menu(self.menuBar, tearoff=0)

        self.menu.add_command(label="About...", command=self.show_credits)
        self.menu.add_command(label="Save...")
        self.menu.add_command(label="Save As...")
        self.menu.add_command(label="Open...", command=self.open_file)
        self.menu.add_command(label="Exit", command=self.quit)

        self.menuBar.add_cascade(label="NTextEditor", menu=self.menu)
        self.textArea.pack()



if __name__ == "__main__": app = MainWindow()