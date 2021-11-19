# thanks to github users : alsoamit
# from github project : text-editor


import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk
Read=False
def MainWindowEditor():
    global window
    window = tk.Tk()
    window.title("哀酱の便签")
    window.columnconfigure(0, weight=0, minsize=250)
    window.columnconfigure(1, weight=1, minsize=400)
    window.rowconfigure(0, weight=1, minsize=600)

# event handlers


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"SI Code - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"SI Code - {filepath}")

def setting():
    global ComMenu
    RootWindowInterface = tk.Tk()
    xVariable = tk.StringVar()
    labelBox = tk.Label(RootWindowInterface, text='设置\n字体大小', font=('Arial', 12), width=6, height=3)
    labelBox.grid(row=0, column=0)
    ComMenu = ttk.Combobox(RootWindowInterface, textvariable=xVariable)

    ComMenu["value"] = ("small", "medium", "large")
    ComMenu.current(1)
    ComMenu.grid(row=1, column=0,  sticky="nesw")
    def xFunc(event):
        value=ComMenu.get()
        print(value)


    ComMenu.bind("<<ComboboxSelected>>", xFunc)
    RootWindowInterface.mainloop()

# frames
def MainEditorProgram(self):
    global txt_edit,varChar
    MainWindowEditor()
    left__Frame = tk.Frame(master=window, bg="white", width=200, padx=10, pady=15)

    # components
    txt_edit = tk.Text(window, bg="#eaeaea", fg="#222",
                       borderwidth=0, relief=tk.FLAT, padx=10, pady=10)
    btn_open = tk.Button(left__Frame, text="Open",
                         padx=5, pady=5, width=31, relief=tk.FLAT, bg="#eaeaea", command=open_file)
    btn_save = tk.Button(left__Frame, text="Save As",
                         padx=5, pady=5, width=31, relief=tk.FLAT, bg="#eaeaea", command=save_file)
    btn_setting = tk.Button(left__Frame, text="Setting",
                         padx=5, pady=5, width=31, relief=tk.FLAT, bg="#eaeaea", command=setting)


    # packing everything up
    txt_edit.grid(row=0, column=1, sticky="nesw")
    left__Frame.grid(row=0, column=0,  sticky="nesw")
    btn_open.grid(row=0, column=0, sticky="nesw")
    btn_save.grid(row=1, column=0, sticky="nesw")
    btn_setting.grid(row=2, column=0, sticky="nesw")
    if self == True:
        f=open('./temp.txt','r')
        varChar=f.read()

        txt_edit.insert(tk.END,varChar)
    window.mainloop()
