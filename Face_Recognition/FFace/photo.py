import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class CameraPreview:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Camera Preview")
        self.window.resizable(width=False, height=False)

        self.capture_button = tk.Button(self.window, text="Capture Image", command=self.capture_image)
        self.capture_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.pack()

        self.video_capture = cv2.VideoCapture(0)
        self.show_frame()

        self.window.mainloop()

    def show_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.imgtk = imgtk
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
        self.window.after(10, self.show_frame)

    def capture_image(self):
        ret, frame = self.video_capture.read()
        if ret:
            filename = filedialog.asksaveasfilename(defaultextension=".jpg")
            if filename:
                cv2.imwrite(filename, frame)


if __name__ == '__main__':
    CameraPreview()
