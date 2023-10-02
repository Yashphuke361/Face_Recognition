import tkinter as tk
from PIL import Image, ImageTk
import subprocess

# Create a window
window = tk.Tk()
window.geometry('1100x420')
window.configure(bg='#6F50F4')

# Set the title of the window
window.title('Attendance  system')


# Define the function that will run when a button is clicked
def run_python_file (filename):
    try:
        subprocess.run(['python', filename])
    except:
        print('Error running file')


# Define the images
image1 = Image.open(r'C:\Users\yashp\Documents\sem4\miniproject\face\FaceRec\FFace-Copy\icon\icon\student.png')
image1 = ImageTk.PhotoImage(image1)

#image2 = Image.open(r'C:\Users\yashp\Documents\sem4\miniproject\face\FaceRec\FFace-Copy\icon\icon\hk.jpg')
#image2 = ImageTk.PhotoImage(image2)

image3 = Image.open(r'C:\Users\yashp\Documents\sem4\miniproject\face\FaceRec\FFace-Copy\icon\icon\ko.png')
image3 = ImageTk.PhotoImage(image3)

image4 = Image.open(r'C:\Users\yashp\Documents\sem4\miniproject\face\FaceRec\FFace-Copy\icon\icon\hi.jpg')
image4 = ImageTk.PhotoImage(image4)

# Create the buttons
button1 = tk.Button(window, text='1.Register', font=("Candara", 23), image=image1, compound='top', command=lambda: run_python_file('capture7.py'),
                    bg='SlateBlue3', fg='white')
#button2 = tk.Button(window, text='2.Upload Database', font=("Candara", 23), image=image2, compound='top', command=lambda: run_python_file('download.py'),
#                    bg='SlateBlue3', fg='white')
button3 = tk.Button(window, text='2.Update Image',  font=("Candara", 23),image=image3, compound='top', command=lambda: run_python_file('EncodeGenerator.py'),
                    bg='SlateBlue3', fg='white')
button4 = tk.Button(window, text='3.Take Attendance', font=("Candara", 23), image=image4, compound='top', command=lambda: run_python_file('main.py'),
                    bg='SlateBlue3', fg='white')

# Add the buttons to the window
button1.pack(side='left', padx=20, pady=20)
#button2.pack(side='left', padx=20, pady=20)
button3.pack(side='left', padx=20, pady=20)
button4.pack(side='left', padx=20, pady=20)

# Start the window
window.mainloop()
