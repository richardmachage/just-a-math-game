from tkinter import *
import backend

global points
points = 0

def level_1_button():
    backend.level_1()

    level_label = Label(frame_levels, text='0 to 9',fg='white', bg='green', width=10)
    level_label.grid(row=2, column=2)

def level_2_button():
    backend.level_2()

    level_label = Label(frame_levels, text='10 to 50', bg='yellow', width=10)
    level_label.grid(row=2, column=2)

def level_3_button():
    backend.level_3()

    level_label = Label(frame_levels, text='51 to 100', fg='black', bg='red', width=10)
    level_label.grid(row=2, column=2)

def addition_button():
    backend.addition()

    operation_label = Label(frame_operatioms, text='+', font=30, fg='black')
    operation_label.grid(row=2, column=2)

def subtraction_button():
    backend.subtraction()

    operation_label = Label(frame_operatioms, text='-', font=30, fg='black')
    operation_label.grid(row=2, column=2)

def multiplication_button():
    backend.multiplication()

    operation_label = Label(frame_operatioms, text='*', font=30, fg='black')
    operation_label.grid(row=2, column=2)

def division_button():
    backend.division()

    operation_label = Label(frame_operatioms, text='/', font=30, fg='black')
    operation_label.grid(row=2, column=2)

def play_button():
    play_lable = Label(window, text='what is '+str(backend.random1)+backend.operation+str(backend.random2)+' ?', width=20)
    play_lable.grid(row= 2, column=0, columnspan=2)

    if backend.operation == '+':
        correct_answer = backend.random1 + backend.random2
    elif backend.operation == '-':
        correct_answer = backend.random1 - backend.random2
    elif backend.operation == '*':
        correct_answer = backend.random1 * backend.random2
    elif backend.operation == '/':
        correct_answer = backend.random1 / backend.random2
    global comp_answer
    comp_answer = str(correct_answer)


def okay_button():
    user_answer = e.get()
    from tkinter import messagebox
    if user_answer == comp_answer:
        global points
        points = points + 1
        messagebox.showinfo(title='correct!', message='correct answer, keep it up \n you have '+ str(points)+' points' )
        e.delete(0,END)
        
        
    else:
        ans = messagebox.askquestion(title='wrong!', message='oops! wrong answer \n TRY again ?' ) 
        if (ans == 'no'):
            messagebox.showinfo(title='ANSWER', message='the correct nswer is: \n'+ comp_answer)

        e.delete(0,END)      
        

        

    
window = Tk()
window.title('ARITHMETIC')
window.geometry('400x400')


#top layout
top = Label(window, text='Hellow :)\n select level and choose the operation to play')
top.grid(row=0,column=0, columnspan=2)

#LEVELS
frame_levels = LabelFrame(window, text= 'choose level', border=5, bg='blue', fg='white')
frame_levels.grid(row=1, column=0, sticky='nesw')
frame_levels.propagate(0)

btn_level1 = Button(frame_levels, text= 'LEVEL 1', bg='green', command= level_1_button)
btn_level1.grid(row=1,column=0, sticky='nsew')

btn_level2 = Button(frame_levels, text= 'LEVEL 2', bg='yellow' ,command= level_2_button)
btn_level2.grid(row=2,column=0,sticky='nsew')

btn_level3 = Button(frame_levels, text= 'LEVEL 3', bg='red',command= level_3_button)
btn_level3.grid(row=3,column=0, sticky='nsew')



#OPERATIONS
frame_operatioms= LabelFrame(window, text='choose operation', bg='blue', fg='white')
frame_operatioms.grid(row=1,column=1, sticky='nesw')

btn_add = Button(frame_operatioms, text='ADDITION', width=15, bg='orange', command= addition_button)
btn_add.grid(row=1,column=0, sticky='nsew')

btn_sub = Button(frame_operatioms, text='SUBTRACTION', width=15,bg='orange', command= subtraction_button)
btn_sub.grid(row=2,column=0, sticky='nsew')

btn_mult = Button(frame_operatioms, text='MULTIPLICATION',width=15,bg='orange',command= multiplication_button)
btn_mult.grid(row=3,column=0, sticky='nsew')

btn_div = Button(frame_operatioms, text='DIVISION',width=15,bg='orange',command= division_button)
btn_div.grid(row=4,column=0, sticky='nsew')

#OTHER WINDOW LAYOUTS
btn_play = Button(window, text='PLAY', width=30, relief=RAISED, command=play_button)
btn_play.grid(row=2, column=0, columnspan=2, padx=1, sticky='nsew')

btn_okay = Button(window, text='okay', width=15, command=okay_button)
btn_okay.grid(row=4,column=1, sticky='nsew')

e = Entry(window, bg='grey')
e.grid(row=4,column=0, padx=20)


quit = Button(window, text='QUIT', command=window.destroy, bg='red', fg='white', width=15, relief=SUNKEN)
quit.grid(row=5, column=0, pady=10, columnspan=2, sticky='nsew')



window.mainloop()
