from tkinter import *
from tkinter import messagebox 
root = Tk()
root.title("Heart Report")
root.geometry("400x400")

question1_radioButton = StringVar(value="0")
question1 = Label(root,text="Do you feel shortness of breath during routine activities?")
question1.pack()
question1_r1 = Radiobutton(root,text="Yes",variable=question1_radioButton,value="Yes")
question1_r1.pack()
question1_r2 = Radiobutton(root,text="No",variable=question1_radioButton,value="No")
question1_r2.pack()


question2_radioButton = StringVar(value="0")
question2 = Label(root,text="Do you have swelling in your feet, ankles, legs or abdomen?")
question2.pack()
question2_r1 = Radiobutton(root,text="Yes",variable=question2_radioButton,value="Yes")
question2_r1.pack()
question2_r2 = Radiobutton(root,text="No",variable=question2_radioButton,value="No")
question2_r2.pack()


question3_radioButton = StringVar(value="0")
question3 = Label(root,text="Do you feel any of these symntoms - confusion, disorentation or loss of memory ?")
question3.pack()
question3_r1 = Radiobutton(root,text="Yes",variable=question3_radioButton,value="Yes")
question3_r1.pack()
question3_r2 = Radiobutton(root,text="No",variable=question3_radioButton,value="No")
question3_r2.pack()


question4_radioButton = StringVar(value="0")
question4 = Label(root,text="Do you experience shortness of breath while at rest or lying down?")
question4.pack()
question4_r1 = Radiobutton(root,text="Yes",variable=question4_radioButton,value="Yes")
question4_r1.pack()
question4_r2 = Radiobutton(root,text="No",variable=question4_radioButton,value="No")
question4_r2.pack()


question5_radioButton = StringVar(value="0")
question5 = Label(root,text="Do you experience persistent wheezing or coughing that produces white or pink blood tinged mucus ?")
question5.pack()
question5_r1 = Radiobutton(root,text="Yes",variable=question5_radioButton,value="Yes")
question5_r1.pack()
question5_r2 = Radiobutton(root,text="No",variable=question5_radioButton,value="No")
question5_r2.pack()


def heart_score():
    score = 0
    if question1_radioButton.get()=="Yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="Yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="Yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="Yes":
        score = score+20
        print(score)
    if question5_radioButton.get()=="Yes":
        score = score+20
        print(score)    
        
    if score <=20:
        messagebox.showinfo("Report","You don't need to visit a doctor")
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report","You don't need to visit a doctor")
    elif score > 40 and score <= 60:
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    elif score > 60 and score <= 80:
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
    else :    
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
        
btn = Button(root,text = "Check",command=heart_score)
btn.pack()
root.mainloop()
