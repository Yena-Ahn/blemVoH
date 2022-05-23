from tkinter import *
tk = Tk()
tk.title('Convert length')
def Ft2Cm():
    ft2cm = entry1.get()
    entry2.delete(0,"end")
    entry2.insert(0,round(float(ft2cm)*30.48,4))
def Cm2Ft():
    cm2ft = entry2.get()
    entry1.delete(0,"end")
    entry1.insert(0,round(float(cm2ft)/30.48,4))

label1 = Label(tk,text='ft').grid(row=0, column=0)
label2 = Label(tk,text='cm').grid(row=1,column=0)

# 각 단위 입력받는 부분 만들기
entry1 = Entry(tk)
entry2 = Entry(tk)


entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

btn1 = Button(tk,text='ft->cm',bg='black',fg='black',command=Ft2Cm).grid(row=2,column=0)
btn2 = Button(tk,text='cm->ft',bg='black',fg='black',command=Cm2Ft).grid(row=2,column=1)

tk.mainloop()