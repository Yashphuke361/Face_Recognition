import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
import urllib.request
import os
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import OptionMenu


# Firebase credentials and database reference][[][
cred = credentials.Certificate("yashkey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattaindancerealtime-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')


def capture_image(studentIds, device_ip):
    url = f"http://192.168.235.46:4747/video"
    cap = cv2.VideoCapture(url)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Resize the frame to 216x216
        resized_frame = cv2.resize(frame, (216, 216))
        # Show the frame in a window
        cv2.imshow('Camera Preview', frame)

        # Add a capture button to the window
        button_text = "Capture"
        if not 'button_added' in locals():
            cv2.namedWindow('Camera Preview')
            cv2.moveWindow('Camera Preview', 0, 0)
            button_added = True
        cv2.putText(frame, f"Press '{button_text}' to capture", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Wait for a key press
        key = cv2.waitKey(1)
        # Check if the 'c' key is pressed
        if key == ord('c'):
            # Save the resized image in BGR format
            img_path = f"C://Users//yashp//Documents//sem4//miniproject//face//FaceRec//FFace-Copy//Images//{studentIds}.jpg"
            cv2.imwrite(img_path, resized_frame)
            # Release the capture and close the window
            cap.release()
            cv2.destroyAllWindows()
            return img_path

        # Check if the 'q' key is pressed
        elif key == ord('q'):
            # Release the capture and close the window
            cap.release()
            cv2.destroyAllWindows()
            return None

# Function to handle form submission

def submit_form():
    studentIds = (id_entry.get())
    name = name_entry.get()
    major = major_var.get()
    starting_year = year_var.get()
    total_attendance = int(total_entry.get())
    last_attendance_time = "2023-04-03 14:30:54"
    standing= "G"

    # Check if any of the fields are empty
    if not studentIds or not name or not major or not starting_year:
        status_label.config(text="Error: Please fill out all fields.")
        return

    # Make sure the total_attendance field can be converted to an integer
    try:
        total_attendance = int(total_attendance)
    except ValueError:
        status_label.config(text="Error: Total Attendance must be a number.")
        return

    # Wait for the window to be closed and get the image path

    img_path = capture_image(studentIds, 4747)

    data = {
        "name": name,
        "major": major,
        "starting_year": starting_year,
        "total_attendance": total_attendance,
        "last_attendance_time": last_attendance_time,
        "img_path": img_path,
        "standing": standing,
        "year": 1

    }

    ref.child(studentIds).set(data)
    status_label.config(text="Student registered successfully!")


# Create GUI window
window = tk.Tk()
window.title("Student Registration")
window.geometry("1000x500")
window.configure(bg="#6F50F4")

# Create form fields
major_options = ["Computer Engineering", "Mechanical", "Civil","Information Tecnology "]
year_options = [2023, 2022, 2021,2020,2019,2018,2017]
id_label = tk.Label(window, text="Student ID",font=("Candara", 35), bg="#6F50F4", fg="white")
id_entry = tk.Entry(window,font=("Candara", 35))
name_label = tk.Label(window, text="Name",font=("Candara", 35), bg="#6F50F4", fg="white")
name_entry = tk.Entry(window,font=("Candara", 35))

major_var = tk.StringVar()
major_var.set(major_options[0])
major_label = tk.Label(window, text="Course", font=("Candara", 35), bg="#6F50F4", fg="white")
major_dropdown = OptionMenu(window, major_var, *major_options)
major_dropdown.config(width=22, font=("Candara", 30))

#year_entry = tk.Entry(window,font=("Candara", 35))
year_var = tk.StringVar()
year_var.set(year_options[0])
year_label = tk.Label(window, text="Course", font=("Candara", 35), bg="#6F50F4", fg="white")
year_dropdown = OptionMenu(window, year_var, *year_options)
year_dropdown.config(width=22, font=("Candara", 30))

total_label =tk.Label(window,text="Total Attendance",font=("Candara", 35), bg="#6F50F4", fg="white")
total_entry =tk.Entry(window,font=("Candara", 35))


# Create submit button
submit_button = tk.Button(window, text="Submit", font=("Candara", 35), bg="#6F4FF8", fg="white",command=submit_form)

# Create status label
status_label = tk.Label(window, text="status", font=("Candara", 20), bg="#6F4FF8", fg="white")


# Add form fields to window
id_label.grid(row=0, column=0, padx=5, pady=5)
id_entry.grid(row=0, column=1, padx=5, pady=5)
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry.grid(row=1, column=1, padx=5, pady=5)
major_label.grid(row=2, column=0, padx=5, pady=5)
major_dropdown.grid(row=2, column=1, padx=5, pady=5)
year_label.grid(row=3, column=0, padx=5, pady=5)
year_dropdown.grid(row=3, column=1, padx=5, pady=5)
total_label.grid(row=4, column=0, padx=5, pady=5)
total_entry.grid(row=4, column=1, padx=5, pady=5)
submit_button.grid(row=6, column=1, pady=10)
status_label.grid(row=6, column=0, padx=3, pady=10, sticky='w')

# Add submit button to window

# Add status label to window

# Start GUI loop
window.mainloop()