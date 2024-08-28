from tkinter import *

root = Tk()

root.title("BMI Calculator")
root.configure(bg='white')
root.geometry("400x400")

user_age = Entry(root,selectbackground="lightblue", selectforeground="black")
user_age.pack()
user_age.place(x=140, y=10)

user_age_label = Label(text="Enter your age: ")
user_age_label.pack()
user_age_label.place(x=5, y=10)

user_weight = Entry(root,selectbackground="lightblue", selectforeground="black")
user_weight.pack()
user_weight.place(x=140, y=60)

user_age_label = Label(text="Enter your weight: ")
user_age_label.pack()
user_age_label.place(x=5, y=60)

user_height = Entry(root,selectbackground="lightblue", selectforeground="black")
user_height.pack()
user_height.place(x=140, y=110)

user_height_label = Label(text="Enter your height: ")
user_height_label.pack()
user_height_label.place(x=5, y=110)


button = Button(root, text="Calculate",activebackground="blue", activeforeground="white")
button.pack()
button.place(x=180, y=160)

root.mainloop()
