from collections import defaultdict
import tkinter as ui
from tkinter.constants import CENTER, LEFT, RIGHT

dict = {'Shubhu':[6284305946, 19, 'Omaxe'], 'Ishaan':[7087382125, 19, 'Sector-35'],'Prateek':[9876721875, 19, 'Sector-37']}
class app:

    def add():

        label1=ui.Label(frame,text="Name :").grid()
        nameEntry= ui.Entry(frame).grid()
        label2=ui.Label(frame,text="Phone No. :").grid()
        phoneEntry= ui.Entry(frame).grid()
        label3=ui.Label(frame,text="Age :").grid()
        ageEntry= ui.Entry(frame).grid()
        label4=ui.Label(frame,text="Locality :").grid()
        localityEntry= ui.Entry(frame).grid()  

        def submit():
            name = nameEntry.get()
            phone= phoneEntry.get()
            age= ageEntry.get()
            locality= localityEntry.get()
            dict = defaultdict(list)
            dict[name].append(phone)
            dict[name].append(age)
            dict[name].append(locality)

        button5=ui.Button(frame,text="ADD",command=submit).grid()  


        
        
        
        print(dict)

    def search():
        entry = input("Write the name of the person whose age you'd like to know, or write 'ALL' to see all names and ages: ")
        if entry == "ALL":
            for key, value in dict.items():
                print("Name: " + key)
                print("Age: " + str(value) + "\n")
        elif entry in dict:
            print('Name: '+ entry)
            print(dict[entry])
        return dict

    def delete():
        deletion = input('Which contact would you like to remove?\n')
        dict.pop(deletion)
        print(dict)



gui=ui.Tk() 

frame = ui.Frame(master=gui, width=250, height=250)

frame.pack()

button1=ui.Button(frame,text="Add Contact",command=app.add).grid(row=0,column=0)
button2=ui.Button(frame,text="Search Contact").grid(row=0,column=1)
button3=ui.Button(frame,text="Contact List").grid(row=0,column=2)
button4=ui.Button(frame,text="Delete Contact").grid(row=0,column=3)


"""print('1. Add Contact')
print('2. Search Contact')
print('3. Delete contact')
n = int(input('\nWhat do you want to do?\nPress number accordingly\n'))
if n==1:
    add(dict)
elif n==2:
    search(dict)
elif n==3:
    delete(dict)

gui.mainloop()

"""
