# from tkinter import*
# import random
# from tkinter import messagebox
# # import random
# top = Tk()
# top.title("memory game")
# # root.iconbitmap('c:/gui/codemy.ico')
# # root.geometry("500x550")
# # # Code to add widgets will go here...
# # # creat the match
# matches=[1,1,2,2,3,3,4,4,5,5,6,6]
# # # shuffles our mathes
# random.shuffle(matches)
# # print(matches)
# # creat buttons frame
# my_frame=Frame(top)
# my_frame.pack(pady=10)
# # define some varieble
# count=0
# answer_list=[]
# answer_dict={}
# # funcation clicking button
# def button_click(b,number):
#     global count,answer_list,answer_dict
#     if b["text"]==" " and count < 2:
#         b["text"]=matches[number]
#         answer_list.append(number)
#         answer_dict[b]=matches[number]
#         count+=1
#         # print(answer_dict)
#         # start to determine correct or not
#     if len(answer_list)==2:
#         if matches[answer_list[0]]==matches[answer_list[1]]:
#             my_lable.config(text="MATCH")
#             for key in answer_dict:
#                 key["state"]="disabled"
#             count=0
#             answer_list=[]
#             answer_dict={}
#         else:
#             my_lable.config(text="oh!")
#             count=0
#             answer_list=[]
#             # pop box
#             messagebox.showinfo("Incorrect","Incorrect")
#             # reset button
#             for key in answer_dict:
#                 key["text"] =" "
                
#             answer_dict={}



# # # define buttons
# b0=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b0,0))
# b1=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b1,1))
# b2=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b2,2))
# b3=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b3,3))
# b4=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b4,4))
# b5=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b5,5))
# b6=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b6,6))
# b7=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b7,7))
# b8=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b8,8))
# b9=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b9,9))
# b10=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(10,10))
# b11=Button(my_frame,text=" ",font=("helvetical",20),height=3,width=6,command=lambda:button_click(b11,11))
# # # grid our button
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

# my_lable=Label(top,text=" ")
# my_lable.pack(pady=20)
# top.mainloop()



# import pywhatkit 
# pywhatkit.sendwhatmsg('7498643970','hello',1,2)