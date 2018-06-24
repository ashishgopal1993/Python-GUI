from tkinter import *
import serial
import time


serial_data = serial.Serial(port='COM3', baudrate=9600)


def click_set_angle():
    angle = input_k_angle.get()
    print(angle)
    serial_data.write('k'.encode())
    time.sleep(0.5)
    serial_data.write(angle.encode())
    input_k_angle.delete(first=0, last=10)
    time.sleep(0.5)


def click_rotate_servo():
    init_angle = input_s_i_angle.get()
    fnl_angle = input_s_f_angle.get()
    step = input_s_step.get()

    serial_data.write('s'.encode())
    time.sleep(1)
    serial_data.write(init_angle.encode())
    time.sleep(1)
    serial_data.write(fnl_angle.encode())
    time.sleep(1)
    serial_data.write(step.encode())
    time.sleep(0)

    print(init_angle)
    print(fnl_angle)
    print(step)

    input_s_i_angle.delete(first=0, last=10)
    input_s_f_angle.delete(first=0, last=10)
    input_s_step.delete(first=0, last=10)


def click_reset():
    serial_data.write('x'.encode())
    time.sleep(0.5)
    print("Reset clicked!")


# Main window initialization
root = Tk()
root.title("Servo Motor Conrol_KJSCE")
root.configure(bg="white")

# Main window title initialization
title_main = Label(root, text="Servo Motor Control", fg="red", bg="white", font=("Times New Roman", 30))
title_main.grid(columnspan=4)

# Main window sub-titles initialization
title_sub = Label(root, text="Graphical User Interface to control Servo Motor rotations", fg="black", bg="white", font=("Times New Roman", 16))
title_sub.grid(columnspan=4)

# Image display
frame_tp = Frame(root)
frame_tp.grid(columnspan=4)
photo_side = PhotoImage(file="ServoMotor.png")
label_photo = Label(frame_tp, image=photo_side)
label_photo.grid(columnspan=3)

title_knob = Label(root, text="Knob Mode:", fg="red", bg="white", font=("Times New Roman", 14))
title_knob.grid(row=5, column=0, sticky=W)

title_sweep = Label(root, text="Sweep Mode:", fg="red", bg="white", font=("Times New Roman", 14))
title_sweep.grid(row=9, column=0, sticky=W)

# Blank rows
label_blank = Label(root, text=" ", bg="white")
label_blank.grid(row=4, sticky=W)
label_blank = Label(root, text=" ", bg="white")
label_blank.grid(row=8, sticky=W)

# For knob mode:
label_k_angle = Label(root, text="Enter any angle between 0° & 180°:", fg="red", bg="white", font=("Times New Roman", 14))
label_k_angle.grid(row=6, column=1, sticky=W)
input_k_angle = Entry(root)
input_k_angle.grid(row=6, column=2, sticky=W)
button_k_set_angle = Button(root, text="Set Angle", fg="white", bg="red", font=("Times New Roman", 12), cursor="plus", command=click_set_angle)
button_k_set_angle.grid(row=6, column=3, sticky=W)

# For Sweep mode:
# Initial angle
label_s_i_angle = Label(root, text="Enter starting angle between 0° & 180°:", fg="red", bg="white", font=("Times New Roman", 14))
label_s_i_angle.grid(row=10, column=1, sticky=W)
input_s_i_angle = Entry(root)
input_s_i_angle.grid(row=10, column=2, sticky=W)

# Final angle
label_s_f_angle = Label(root, text="Enter final angle between 0° & 180°:", fg="red", bg="white", font=("Times New Roman", 14))
label_s_f_angle.grid(row=11, column=1, sticky=W)
input_s_f_angle = Entry(root)
input_s_f_angle.grid(row=11, column=2, sticky=W)

# Step size
label_s_step = Label(root, text="Enter valid step size:", fg="red", bg="white", font=("Times New Roman", 14))
label_s_step.grid(row=12, column=1, sticky=W)
input_s_step = Entry(root)
input_s_step.grid(row=12, column=2, sticky=W)

button_s_rotate_servo = Button(root, text="Start Rotation", fg="white", bg="red", font=("Times New Roman", 12), cursor="plus", command=click_rotate_servo)
button_s_rotate_servo.grid(row=10, column=3, sticky=W)

# Reset button
button_reset = Button(root, text="Reset Motor", fg="white", bg="red", font=("Times New Roman", 12), cursor="plus", command=click_reset)
button_reset.grid(row=11, column=3, sticky=W)

root.resizable(width=False, height=False)
root.mainloop()