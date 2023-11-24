import tkinter as tk

def fake_hack():
    window = tk.Tk()
    window.title("Error! Hacked by MrDyatlov")
    window.geometry("350x150")
    """label_one = tk.Label(text="Hacked by", font="Verdana 15")
    label_two = tk.Label(text="MrDyatlov", font="Verdana 20")
    label_three = tk.Label(text="Yohohoho bilgisayarın bana emanet.", font="Verdana 13")
    label_one.pack()
    label_two.pack()
    label_three.pack()"""

    window.mainloop(10)


numberos = list(range(1, 111))

for i in numberos:
    fake_hack()


