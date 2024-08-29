from tkinter import *
from tkinter import messagebox

root = Tk()
user_gender = IntVar()

global value


def button_click():
    global value
    age = user_age.get()
    weight = user_weight.get()
    height = user_height.get()



    if not age or not weight or not height:
        messagebox.showerror("Error", "All fields must be filled out.")

    try:
        user_weight_value = int(user_weight.get())
        user_height_value = float(user_height.get()) ** 2
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height.")
        return

    value = user_weight_value / user_height_value


    if value < 18.5:
        messagebox.showinfo("BMI", f"Your BMI :{value} - Underweight ")
    elif 18.5 < value < 24.9:
        messagebox.showinfo("BMI", f"Your BMI :{value} - Normal ")
    elif 25 < value <29.9:
        messagebox.showinfo("BMI", f"Your BMI :{value} - Overweight ")
    elif 30 < value < 34.9:
        messagebox.showinfo("BMI", f"Your BMI :{value} - Obese ")
    else:
        messagebox.showinfo("BMI", f"Your BMI :{value} - Extremely Obese ")

root.title("BMI Calculator")
root.configure(bg='white')
root.geometry("400x400")

user_age = Entry(root,selectbackground="lightblue", selectforeground="black")
user_age.pack()
user_age.place(x=160, y=10)

user_age_label = Label(text="Enter your age: ")
user_age_label.pack()
user_age_label.place(x=5, y=10)

user_gender_label = Label(root, text="Select your gender: ")
user_gender_label.pack()
user_gender_label.place(x=5, y=60)

user_gender_radiobutton = Radiobutton(root, text="Male", variable=user_gender, value=1)
user_gender_radiobutton2 = Radiobutton(root, text="Female", variable=user_gender, value=2)
user_gender_radiobutton.pack()
user_gender_radiobutton.place(x=160, y=60)
user_gender_radiobutton2.pack()
user_gender_radiobutton2.place(x=245, y=60)

user_weight = Entry(root,selectbackground="lightblue", selectforeground="black")
user_weight.pack()
user_weight.place(x=160, y=110)

user_age_label = Label(text="Enter your weight(kg): ")
user_age_label.pack()
user_age_label.place(x=5, y=110)

user_height = Entry(root,selectbackground="lightblue", selectforeground="black")
user_height.pack()
user_height.place(x=160, y=160)

user_height_label = Label(text="Enter your height(m): ")
user_height_label.pack()
user_height_label.place(x=5, y=160)

button = Button(root, text="Calculate",activebackground="blue", activeforeground="white", command=button_click)
button.pack()
button.place(x=195, y=210)

root.mainloop()
