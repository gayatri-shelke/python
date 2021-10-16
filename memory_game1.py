# from tkinter import*
# import random
# top=Tk()
# top.title("memory game")
# top.geometry("500x400")

# matches=[1,1,2,2,3,3,4,4,5,5,6,6]
# random.shuffle(matches)
# # print(matches)
# my_frame=Frame(top)
# my_frame.pack(pady=10)
# def something():
#     pass

# b0=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b1=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b2=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b3=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b4=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b5=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b6=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b7=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b8=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b9=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b10=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)
# b11=Button(my_frame,text=" ",font=("bold",20),height=3,width=6,command=something)


# b0.grid(row=0,column=0)
# b1.grid(row=0,column=1)
# b2.grid(row=0,column=2)
# b3.grid(row=0,column=3)

# b4.grid(row=1,column=0)
# b5.grid(row=1,column=1)
# b6.grid(row=1,column=2)
# b7.grid(row=1,column=3)

# b8.grid(row=2,column=0)
# b9.grid(row=2,column=1)
# b10.grid(row=2,column=2)
# b11.grid(row=2,column=3)





# top.mainloop()



import tkinter as tk
from tkinter import ttk
top=tk.Tk()
top.title("gayatri")
top.geometry("500x550")
name_lable=ttk.Label(top,text="enter your name:")
name_lable.grid(row=0,column=0)

age_lable=ttk.Label(top,text="enter your email:")
age_lable.grid(row=1,column=0)

gender_lable=ttk.Label(top,text="select your gender:")
gender_lable.grid(row=4,column=0)


name_var=tk.StringVar()
name_var=ttk.Entry(top,width=16,textvariable=name_var)
name_var.grid(row=0,column=1)
name_var.focus()

email_var=tk.StringVar()
email_var=ttk.Entry(top,width=16,textvariable=email_var)
email_var.grid(row=1,column=1)
# email_var.focus()

gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(top,width=14,textvariable=gender_var,state='readonly')
gender_combobox['values']=('male','famale','others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)


# create redio button
usertypes=tk.StringVar()
radiobt1=ttk.Radiobutton(top,text='student',value='student',variable=usertypes)
radiobt1.grid(row=5,column=0)

radiobt1=ttk.Radiobutton(top,text='teacher',value='teacher',variable=usertypes)
radiobt1.grid(row=5,column=1)



# creat button
def action():
    user_name=name_var.get()
    user_age=email_var.get()
    print(f'{user_name}{user_age}')
sumbit_button=ttk.Button(top,text="sumbit")
sumbit_button.grid(row=6,column=0)

top.mainloop()

import tkinter 
from tkinter import ttk
top=tkinter.Tk()
top.title("about my self information")
top.geometry('500x550')
name=ttk.Label(top,text='enter the number:')
name.grid(row=0,column=0)

age_lable=ttk.Label(top,text='enter the age:')
age_lable.grid(row=1,column=0)

gender_var=ttk.Label(top,text='select your gender')
gender_var.grid(row=2,column=0)

name_var=tkinter.StringVar()
name_var=ttk.Entry(top,width=14,textvariable=name_var)
name_var.grid(row=0,column=1)

age_var=tkinter.StringVar()
age_var=ttk.Entry(top,width=14,textvariable=age_var)
age_var.grid(row=1,column=1)

gender_var=tkinter.StringVar()
gender_combobox=ttk.Combobox(top,width=12,textvariable=gender_var)
gender_combobox['value']=['male','female','others']
gender_combobox.grid(row=2,column=1)




top.mainloop()



# import requests
# import json

# saral_api = "http://saral.navgurukul.org/api/courses"
# saral_url = requests.get(saral_api)
# data = saral_url.json()
# with open("courses.json","w") as saral_data :
#     json.dump(data,saral_data,indent=4)

# serial_no = 1
# for courses in data["availableCourses"]:
#     print(serial_no ,".",courses["name"],courses["id"])
#     serial_no += 1
# course = int(input("enter the course number: "))
# print(data["availableCourses"][course-1]["name"])

# saral_api_1 = ("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][course-1]["id"])+"/exercises")
# saral_url_1=requests.get(saral_api_1)
# data_1 = saral_url_1.json()
# with open ("parents.json","w") as saral_data_1 :
#     json.dump(data_1,saral_data_1,indent=4)      
    
# no=0
# print(data_1["data"][1]["slug"])
# for child in range(len(data_1["data"])):
#     no+=1
#     print("        ",no,".",data_1["data"][child]["name"])
#     serial_no_1=1
#     if data_1["data"][child]["childExercises"] == []:
#         print("             ",serial_no_1,".",data_1["data"][child]["slug"])
#         serial_no_1 += 1
#     else:

#         serial_no=1
#         for Question in range(len(data_1["data"][child]["childExercises"])):
#             print("              ",serial_no,".",data_1["data"][child]["childExercises"][Question]["name"])
#             serial_no+=1

# serial_no+=1
# Slug= int(input("Enter the number of child :"))
# print(data_1["data"][Slug-1]["name"])
# serial_no=1
# for Question in range(len(data_1["data"][Slug-1]["childExercises"])):
#     if data_1["data"][child]["childExercises"] == []:
#         print("              ",serial_no,".",data_1["data"][Slug-1]["childExercises"][Question]["name"])
#         serial_no+=1

# slug_ind=[]
# no=0
# List=[] 
# for child in range(len(data_1["data"])):
#     no+=1
#     serial_no_1=1
#     if data_1["data"][child]["childExercises"] == List:
#         serial_no_1 += 1

#         serial_no=1
#         for Question in range(len(data_1["data"][Slug-1]["childExercises"])):
#             if data_1["data"][child]["childExercises"] == List:
#                 print("              ",serial_no,".",data_1["data"][Slug-1]["childExercises"][Question]["name"])
#                 slug = data_1["data"][Slug-1]["childExercises"][Question]["slug"]
#                 parent = data_1["data"][Slug-1]["childExercises"][Question]['id']
#                 slug1 = requests.get(" http://saral.navgurukul.org/api/courses/"+parent+"/exercise/getBySlug?slug="+slug)

#                 slug2 = slug1.json()
#                 slug_ind.append(slug2["content"])
#                 serial_no+=1
#         break
    