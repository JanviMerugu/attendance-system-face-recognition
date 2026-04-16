import tkinter as tk
from tkinter import *
import os
import cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# project module
import show_attendance
import takeImage
import trainImage      
import automaticAttedance
import report
from PIL import Image, ImageTk

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()



def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()
    
def load_img(path):
    img = Image.open(path)
    img = img.resize((200, 200))
    return ImageTk.PhotoImage(img)


haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "./TrainingImageLabel/Trainner.yml"
)
trainimage_path = "./TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = (
    "./StudentDetails/studentdetails.csv"
)
attendance_path = "Attendance"

window = Tk()
window.title("Face Recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#1c1c1c")  # Dark theme


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="#1c1c1c")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="yellow",
        bg="#1c1c1c",  # Dark background for the error window
        font=("Verdana", 16, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="yellow",
        bg="#333333",  # Darker button color
        width=9,
        height=1,
        activebackground="red",
        font=("Verdana", 16, "bold"),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#1c1c1c", relief=RIDGE,
                bd=10, font=("Verdana", 30, "bold"))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#1c1c1c",)
l1.place(x=470, y=10)


titl = tk.Label(
    window, text="CLASS VISION", bg="#1c1c1c", fg="yellow", font=("Verdana", 27, "bold"),
)
titl.place(x=525, y=12)

a = tk.Label(
    window,
    text="Welcome to CLASS VISION",
    bg="#1c1c1c",  # Dark background for the main text
    fg="yellow",  # Bright yellow text color
    bd=10,
    font=("Verdana", 35, "bold"),
)
a.pack()


# -------- IMAGE 1 --------
img1 = load_img("UI_Image/register.png")
frame1 = tk.Frame(window, width=220, height=220, bg="white")
frame1.place(x=150, y=260)
frame1.pack_propagate(False)

label1 = tk.Label(frame1, image=img1, bg="white")
label1.image = img1
label1.pack(expand=True)

# -------- IMAGE 2 --------
img2 = load_img("UI_Image/verifyy.png")
frame2 = tk.Frame(window, width=220, height=220, bg="white")
frame2.place(x=450, y=260)
frame2.pack_propagate(False)

label2 = tk.Label(frame2, image=img2, bg="white")
label2.image = img2
label2.pack(expand=True)

# -------- IMAGE 3 --------
img3 = load_img("UI_Image/attendance.png")
frame3 = tk.Frame(window, width=220, height=220, bg="white")
frame3.place(x=750, y=260)
frame3.pack_propagate(False)

label3 = tk.Label(frame3, image=img3, bg="white")
label3.image = img3
label3.pack(expand=True)

# -------- IMAGE 4 (FIXED) --------
img4 = load_img("UI_Image/report.png")
frame4 = tk.Frame(window, width=220, height=220, bg="white")
frame4.place(x=1050, y=260)
frame4.pack_propagate(False)

label4 = tk.Label(frame4, image=img4, bg="white")
label4.image = img4
label4.pack(expand=True)

def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    # Dark background for the image window
    ImageUI.configure(background="#1c1c1c")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#1c1c1c", relief=RIDGE,
                    bd=10, font=("Verdana", 30, "bold"))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="#1c1c1c", fg="green", font=("Verdana", 30, "bold"),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#1c1c1c",  # Dark background for the details label
        fg="yellow",  # Bright yellow text color
        bd=10,
        font=("Verdana", 24, "bold"),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="#1c1c1c",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="#333333",  # Dark input background
        fg="yellow",  # Bright text color for input
        relief=RIDGE,
        font=("Verdana", 18, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="#1c1c1c",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#333333",  # Dark input background
        fg="yellow",  # Bright text color for input
        relief=RIDGE,
        font=("Verdana", 18, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="#1c1c1c",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#333333",  # Dark background for messages
        fg="yellow",  # Bright text color for messages
        relief=RIDGE,
        font=("Verdana", 14, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("Verdana", 18, "bold"),
        bg="#333333",  # Dark background for the button
        fg="yellow",  # Bright text color for the button
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("Verdana", 18, "bold"),
        bg="#333333",  # Dark background for the button
        fg="yellow",  # Bright text color for the button
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)


r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=150, y=520)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=450, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

def generate_report():
    try:
        overall, monthly, subject = report.generate_report()

        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from tkinter import ttk

        report_window = tk.Toplevel(window)
        report_window.title("Attendance Dashboard")
        report_window.geometry("900x600")
        report_window.configure(bg="#0f2027")

        nav = tk.Frame(report_window, bg="#203a43")
        nav.pack(fill="x")

        content = tk.Frame(report_window, bg="#0f2027")
        content.pack(fill="both", expand=True)

        def clear():
            for widget in content.winfo_children():
                widget.destroy()

        # -------- STYLE --------
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="black",
                        foreground="yellow",
                        fieldbackground="black",
                        rowheight=25,
                        font=("Verdana", 10))

        style.configure("Treeview.Heading",
                        background="black",
                        foreground="yellow",
                        font=("Verdana", 11, "bold"))

        # -------- OVERALL --------
        def show_overall():
            clear()

            search_var = tk.StringVar()

            top = tk.Frame(content, bg="#0f2027")
            top.pack(fill="x")

            tk.Label(top, text="Search:", bg="#0f2027", fg="white").pack(side="left", padx=10)
            entry = tk.Entry(top, textvariable=search_var)
            entry.pack(side="left")

            tree = ttk.Treeview(content)
            tree["columns"] = ("ID", "Name", "Days", "Percentage")

            tree.column("#0", width=0)
            tree.column("ID", anchor="center", width=100)
            tree.column("Name", anchor="center", width=150)
            tree.column("Days", anchor="center", width=100)
            tree.column("Percentage", anchor="center", width=120)

            tree.heading("ID", text="Enrollment")
            tree.heading("Name", text="Name")
            tree.heading("Days", text="Days")
            tree.heading("Percentage", text="Attendance")

            tree.pack(fill="both", expand=True)

            def load_data(event=None):
                tree.delete(*tree.get_children())
                query = search_var.get().lower()

                for _, row in overall.iterrows():
                    if query and query not in str(row["Enrollment"]).lower() and query not in str(row["Name"]).lower():
                        continue

                    tree.insert("", "end",
                                values=(row["Enrollment"],
                                        row["Name"],
                                        row["Days"],
                                        f"{round(row['Percentage'],2)}%"))

            entry.bind("<Return>", load_data)

            load_data()

        # -------- MONTHLY --------
        def show_monthly():
            clear()

            top_frame = tk.Frame(content, bg="#0f2027")
            top_frame.pack(fill="x", pady=10)

            months = sorted([str(m) for m in monthly["Month"].unique()])
            subjects = ["All"] + monthly["Subject"].unique().tolist()

            selected_month = tk.StringVar(value=months[0])
            selected_subject = tk.StringVar(value="All")
            search_var = tk.StringVar()

            tk.Label(top_frame, text="Month:", bg="#0f2027", fg="white").pack(side="left", padx=10)
            tk.OptionMenu(top_frame, selected_month, *months).pack(side="left")

            tk.Label(top_frame, text="Subject:", bg="#0f2027", fg="white").pack(side="left", padx=10)
            tk.OptionMenu(top_frame, selected_subject, *subjects).pack(side="left")

            tk.Label(top_frame, text="Search:", bg="#0f2027", fg="white").pack(side="left", padx=10)
            entry = tk.Entry(top_frame, textvariable=search_var)
            entry.pack(side="left")

            main_frame = tk.Frame(content, bg="#0f2027")
            main_frame.pack(fill="both", expand=True)

            def load_data(event=None):
                for widget in main_frame.winfo_children():
                    widget.destroy()

                month_val = int(selected_month.get())
                subject_val = selected_subject.get()
                query = search_var.get().lower()

                if subject_val == "All":
                    df = monthly[monthly["Month"] == month_val]
                else:
                    df = monthly[(monthly["Month"] == month_val) &
                                 (monthly["Subject"] == subject_val)]

                grouped = df.groupby(["Enrollment", "Name"])

                for (enroll, name), data in grouped:

                    if query and query not in str(enroll).lower() and query not in str(name).lower():
                        continue

                    present = int(data["Days"].sum())
                    absent = max(0, present // 2)
                    total = present + absent
                    percent = round((present / total) * 100, 2) if total > 0 else 0

                    card = tk.Frame(main_frame, bg="#1b2a34", bd=2, relief="ridge", height=150)
                    card.pack(fill="x", padx=20, pady=10)
                    card.pack_propagate(False)

                    left = tk.Frame(card, bg="#1b2a34")
                    left.pack(side="left", padx=20)

                    tk.Label(left, text=f"ID: {enroll} | {name}",
                             fg="cyan", bg="#1b2a34",
                             font=("Verdana", 11, "bold")).pack(anchor="w")

                    tk.Label(left, text=f"✔ Present: {present}", fg="lightgreen", bg="#1b2a34").pack(anchor="w")
                    tk.Label(left, text=f"❌ Absent: {absent}", fg="red", bg="#1b2a34").pack(anchor="w")
                    tk.Label(left, text=f"📚 Total Classes: {total}", fg="white", bg="#1b2a34").pack(anchor="w")

                    fig, ax = plt.subplots(figsize=(2, 2))
                    ax.pie([present, absent], colors=["green", "red"],
                           startangle=90, wedgeprops=dict(width=0.4))

                    ax.text(0, 0, f"{percent}%", ha='center', va='center', color='white')
                    fig.patch.set_facecolor('#1b2a34')

                    chart = FigureCanvasTkAgg(fig, master=card)
                    chart.draw()
                    chart.get_tk_widget().pack(side="right", padx=20)

                    plt.close(fig)

            entry.bind("<Return>", load_data)

            tk.Button(top_frame, text="Show", command=load_data,
                      bg="#203a43", fg="white").pack(side="left", padx=20)

            load_data()

        # -------- SUBJECT --------
        def show_subject():
            clear()

            top_frame = tk.Frame(content, bg="#0f2027")
            top_frame.pack(fill="x", pady=10)

            subjects_list = subject["Subject"].unique().tolist()
            selected_subject = tk.StringVar(value=subjects_list[0])
            search_var = tk.StringVar()

            tk.Label(top_frame, text="Subject:", bg="#0f2027", fg="white").pack(side="left", padx=10)
            tk.OptionMenu(top_frame, selected_subject, *subjects_list).pack(side="left")

            tk.Label(top_frame, text="Search:", bg="#0f2027", fg="white").pack(side="left", padx=10)
            entry = tk.Entry(top_frame, textvariable=search_var)
            entry.pack(side="left")

            main_frame = tk.Frame(content, bg="#0f2027")
            main_frame.pack(fill="both", expand=True)

            def load_data(event=None):
                for widget in main_frame.winfo_children():
                    widget.destroy()

                sub = selected_subject.get()
                query = search_var.get().lower()

                df = subject[subject["Subject"] == sub]
                total = df["Days"].sum()

                for _, row in df.iterrows():

                    if query and query not in str(row["Enrollment"]).lower() and query not in str(row["Name"]).lower():
                        continue

                    present = row["Days"]
                    absent = max(0, total - present)
                    percent = round((present / total) * 100, 2) if total > 0 else 0

                    card = tk.Frame(main_frame, bg="#1b2a34", bd=2, relief="ridge", height=150)
                    card.pack(fill="x", padx=20, pady=10)
                    card.pack_propagate(False)

                    left = tk.Frame(card, bg="#1b2a34")
                    left.pack(side="left", padx=20)

                    tk.Label(left, text=f"ID: {row['Enrollment']} | {row['Name']}",
                             fg="cyan", bg="#1b2a34",
                             font=("Verdana", 11, "bold")).pack(anchor="w")

                    tk.Label(left, text=f"✔ Present: {present}", fg="lightgreen", bg="#1b2a34").pack(anchor="w")
                    tk.Label(left, text=f"❌ Absent: {absent}", fg="red", bg="#1b2a34").pack(anchor="w")
                    tk.Label(left, text=f"📚 Total Classes: {total}", fg="white", bg="#1b2a34").pack(anchor="w")

                    fig, ax = plt.subplots(figsize=(2, 2))
                    ax.pie([present, absent], colors=["green", "red"],
                           startangle=90, wedgeprops=dict(width=0.4))

                    ax.text(0, 0, f"{percent}%", ha='center', va='center', color='white')
                    fig.patch.set_facecolor('#1b2a34')

                    chart = FigureCanvasTkAgg(fig, master=card)
                    chart.draw()
                    chart.get_tk_widget().pack(side="right", padx=20)

                    plt.close(fig)

            entry.bind("<Return>", load_data)

            tk.Button(top_frame, text="Show", command=load_data,
                      bg="#203a43", fg="white").pack(side="left", padx=20)

            load_data()

        # -------- NAV --------
        tk.Button(nav, text="Overall", command=show_overall,
                  bg="#203a43", fg="white", width=15).pack(side="left", padx=10)

        tk.Button(nav, text="Monthly", command=show_monthly,
                  bg="#203a43", fg="white", width=15).pack(side="left", padx=10)

        tk.Button(nav, text="Subject-wise", command=show_subject,
                  bg="#203a43", fg="white", width=15).pack(side="left", padx=10)

        show_overall()
        text_to_speech("Dashboard opened")

    except Exception as e:
        print(e)
        text_to_speech("Error generating report")
        
r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=750, y=520)
r = tk.Button(
    window,
    text="Generate Report",
    command=generate_report,
    bd=10,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=1050, y=520)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("Verdana", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=650, y=650)


window.mainloop()
