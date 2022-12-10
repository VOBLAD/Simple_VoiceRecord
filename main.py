import datetime
import sounddevice
from scipy.io.wavfile import write
from tkinter import *


def voice_recorder():
       duration = 10
       recording = sounddevice.rec((duration*44100), samplerate=44100, channels=2)
       sounddevice.wait()
       tm = datetime.datetime.now().strftime("%H-%M-%d-%m-%y")
       write(tm +".wav", 44100, recording)
       lb.config(text="Готово")


root =Tk()
root.geometry("250x400")
root.title("Диктофон")
root.resizable(False, False)
root.config(bg="black")
icon = PhotoImage(file="rec.png")



lb = Label(root, text="СТАРТ", fg="white", bg="black", font='Arial 15 bold')
lb.pack(padx=10, pady=70)

lb1 = Label(root,text="10 Секунд", fg="white", bg="black", font='Arial 15 bold')
lb1.pack(padx=10, pady=10)

bt = Button(root, image=icon, relief=FLAT, bg="black", command=voice_recorder)
bt.pack(side=BOTTOM, pady=55)

root.mainloop()




