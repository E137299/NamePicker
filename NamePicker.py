from tkinter import*
import random

root = Tk()
root.geometry("360x330")
root.configure(background="teal")
root.title("Name Picker")
#### MODEL ####
list = []

def second_period():
    global list, class_selected
    list = ["Scott B.","Che B."," Cooper B.","Collin C.","Ameryss D.","Kate D.","Matthew F.","Vivian G.","Marshall G.","Weston H.","Hunter J.","Gavin K.","Tae L.","Aidan L.","Hudson M.","Judson M.","Alex M.","Jakob O.","Rieve T.","Ryan V.","Drew W."]
    clase.config(text="Second Period")

def third_period():
    global list
    list = ["Danica A.","Leonardo A.","Amaya B.","Zachary B.","Noah B","Kai B.","Sam C.","Marissa G.","Maddie G.","Harper H.","Wren H.","Wren Heinley","Soleil H.","Ford H.","Samir K.","Lucian M.","William M.","Elijah S.","Joseph S."]
    clase.config(text="Third Period")

def fourth_period():
    global list
    list = ["Michael C.","Jack D.","Jack E.","Donovan F.","Isaac G.","Jack H.","Brighton H.","Olivia H.","Anders J.","Darrell J.","Kun Hee L.","Kathleen O.","Ezekiel P.","Wyatt P.","Gabriel S.","Aberdine M.","Griffen S.","Will S.","Wyatt T.","Yuval T.","Theo V."]
    clase.config(text="Fourth Period")

def fifth_period():
    global list
    list = ["Avery B.","Rylie B.","Hank B.","Quinn C.","Huey C.","Diego C.","Colin D.","Owen D.","Matthew G.","Ryan G.","Owen M.","Miles N.","Israel P.","William R.","James S.","Sebastian P.","Winn S.","Sonia S.","Kemble W.","Cosmo Y."]
    clase.config(text="Fifth Period")

def seventh_period():
    global list
    list = ["Levee A.","Jake B.","Bennett B.","Luke B.","Willie C.","John D.","Evan G.","Boone G.","Elizabeth H.","Himeer J.","Xander L.","Veronica L.","Nathan L.","Aidan M.","Charles M.","Henry R.","Cooper S.","Liam S.","Muscy T."]
    clase.config(text="Seventh Period")

def eight_period():
    global list
    list = ["Logan","Charlie","Ricky","Jackson","August","Malia","Roan","Matthew","Preston","Sterling","Eli","Ryan","Danny","Piper","Xander","Chance","Ty","Liam","Oliver","Holden"]
    clase.config(text="Eight Period")


def pick_student():
    global list
    if len(list)>0:
        student.config(text=list.pop(random.randint(0,len(list)-1)))
    else:
        student.config(text="Reset Class")
#### CONTROLLER ####"
title= Label(root,text="Name Picker", font=("Times New Roman",20), bg="teal").place(x=110, y=20, )

class_selected = Label(root,text="Selected class: ",font=("Times New Roman",15),bg="teal")
class_selected.place(x=20, y=200)

clase = Label(root,text="",font=("Times New Roman",20),bg="teal", fg ="white")
clase.place(x=150,y=195)

student_selected = Label(root,text="Selected student: ",font=("Times New Roman",15),bg="teal")
student_selected.place(x=20, y=260)

student = Label(root, text="", font=("Times New Roman",20),bg="teal",fg="white")
student.place(x=167,y=255)

second = Button(root, text="2nd Period", command = second_period)
second.place(x=20,y=70,width=100, height=30)

third = Button(root, text="3rd Period",command = third_period)
third.place(x=130,y=70,width=100,height=30)

fourth = Button(root, text="4th Period", command = fourth_period)
fourth.place(x=240,y=70,width=100,height=30)

fifth = Button(root, text="5th Period", command = fifth_period)
fifth.place(x=20,y=110,width=100, height=30)

seventh = Button(root, text="7th Period", command = seventh_period)
seventh.place(x=130,y=110,width=100, height=30)

eigth = Button(root, text="8th Period", command = eight_period)
eigth.place(x=240,y=110,width=100, height=30)

student_picker = Button(root, text="Randomly Select A Student", command = pick_student)
student_picker.place(x=20,y=150, width=320, height=30)

#### VIEW ####





root.mainloop()