from tkinter import *
root = Tk()

# number of clicks
counter = 0
def clicked():
    global counter #global variable counter
    counter += 1
    label1['text'] = 'Number of clicks: ' + str(counter)

#reset function
def reset():
    global counter
    counter = 0
    label1['text'] = 'Press the button.'

# title of window
root.title('Count of clicks') 

# text
label1=Label(root, text='Press the button.',fg='black',font=20) # fg는 글자 색 지정, font로 글자 설정
label1.pack(side=LEFT, padx=10, pady=10)
# button1
button1 = Button(root,text='Click me!',highlightbackground='green', bg='green', font=15,width=30,height=5,command= clicked) #command로 버튼 클릭 시 동작할 함수 지정, bg로 색상지정, width,height로 각각 넓이 높이 지정
button1.pack(side=LEFT, padx=10, pady=10)
# button2
button2 = Button(root,text='RESET',highlightbackground='red', bg='red',width=30,height=5,font=15,command=reset)
button2.pack(side=LEFT,padx=10, pady=10)
root.mainloop()