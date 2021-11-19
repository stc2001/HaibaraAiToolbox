# 本软件一些元素可能涉及其它法人或实体的版权（东宝株式会社），因此图形界面的图标，文字并不能单独提取用于商用
# 本ソフトウェアの一部の要素は、他の法人や実体の著作権（東宝株式会社）に関連している可能性がありますので、グラフィカルインターフェースのアイコンは、文字だけではなく、商用用に抽出できません。
# Some elements of the software may involve the copyright of other legal persons or entities (Dongbao Co., Ltd.), so the icons and text of the graphical interface cannot be extracted separately for commercial use
# 来自其它许可证的开源组件请依照相应的开源许可证
# For other open source components from other licenses, please follow the corresponding open source license

ifHit = True
import tkinter as tk
import tkinter.messagebox
from tkinter.messagebox import askyesno
import os
import sys
def WarningBox():
    tk.messagebox.showwarning('警告', '不要随意给灰原哀磕cp')
def ErrorBox():
    tk.messagebox.showerror('错误', '你不是灰原哀的cp')
def closeWindow():
    ans = askyesno(title='提示',message='关闭窗口？')
    if ans:
        sys.exit()
    else:
        return

def hitFunctionOCR():
    import OCRAuto
    global ifHit
    if ifHit:
        RootWindowInterface.destroy()
        OCRAuto.runApps()
    else:
        ifHit = False

def hitFunctionNotes():
    import tkinterEditor
    global ifHit
    if ifHit:
        RootWindowInterface.destroy()
        tkinterEditor.MainEditorProgram(False)
    else:
        ifHit = False

def GetScreen():
    import Photo
    global ifHit
    if ifHit:
        RootWindowInterface.destroy()
        Photo.ExecPhotosCut()
    else:
        ifHit = False

def HAhitFunctionSelfShot():
    import HAbgChange
    global ifHit
    if ifHit:
        RootWindowInterface.destroy()
        try:
            HAbgChange.SelfShotFunction()
        except:
            pass
    else:
        ifHit = False

def HAPhotoCut():
    import HAselfShot
    global ifHit
    if ifHit:
        RootWindowInterface.destroy()
        HAselfShot.HAPhoto()
    else:
        ifHit = False

def Interface():
    global RootWindowInterface,photo
    RootWindowInterface = tk.Tk()
    labelBox = tk.Label(RootWindowInterface,  text='哀酱の\n实用\n工具箱',font=('Arial', 12), width=7, height=5)
    labelBox.grid(row=0,column=0)
    d = tk.Button(RootWindowInterface, text='OCR', font=('Arial', 12), width=5, height=1, command=hitFunctionOCR)
    d.grid(row=2,column=0)
    f = tk.Button(RootWindowInterface, text='截图', font=('Arial', 12), width=5, height=1, command=GetScreen)
    f.grid(row=3,column=0)
    e = tk.Button(RootWindowInterface, text='便签', font=('Arial', 12), width=5, height=1, command=hitFunctionNotes)
    e.grid(row=4,column=0)

    g = tk.Button(RootWindowInterface, text='自拍杆', font=('Arial', 12), width=5, height=1, command=HAhitFunctionSelfShot)
    g.grid(row=5, column=0)
    h = tk.Button(RootWindowInterface, text='证件照', font=('Arial', 12), width=5, height=1, command=HAPhotoCut)
    h.grid(row=6, column=0)

    photo = tk.PhotoImage(file='./HaibaraAi.gif')
    Lab = tk.Label(RootWindowInterface,  compound='center',image=photo)
    Lab.grid(row=1,column=0) # 设置主界面

    RootWindowInterface.protocol('WM_DELETE_WINDOW', closeWindow)
    RootWindowInterface.mainloop()

def ResetProgram():
    HaibaraAiToolbox = sys.executable
    os.execl(HaibaraAiToolbox, HaibaraAiToolbox, * sys.argv)

if __name__ == "__main__":
    Interface()
    ResetProgram()

