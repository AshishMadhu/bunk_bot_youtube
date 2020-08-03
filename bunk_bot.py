import os
from time import sleep, time
import winsound
import cv2
import sys
import pyautogui
import speech_recognition as sr
import pytesseract
from HelperFunctions import returnComparatorList, most_frequent, pyautoguiMoveClickSleep, pyautoguiMoveTypeSleep
from HelperFunctions import returnMostCommonWord, returnComparison, returnStrAndRegexList

# theres a "tesseract.exe" file you need to download if you use this on windows
pytesseract.pytesseract.tesseract_cmd = 'G:\\Programs files\\Tesseract-OCR\\tesseract.exe'

# chrome 
x1, y1 = 302, 1065

# search field
x2, y2 = 682, 62

# audio button on start
x3, y3 = 612, 811

# video
x4, y4 = 714, 820

# join
x5, y5 = 1350, 605

# message
x6, y6 = 1614, 119

# message-input
x7, y7 = 1635, 986

# leave call
x10, y10 = 976, 987

# message-box
x8, y8 = 1522, 237
x9, y9 = 1914, 952

# meeting link
meeting_link = "https://meet.google.com/baz-cmhd-hru"

a = time()

def clock():
    """
    The clock function returns the amount of time that had passed since the code had begun execution in minutes
    :return:
    """
    return (time() - a) // 60

def answerAttendance():
    pyautogui.moveTo( x7, y7, duration=1 )
    pyautogui.click()
    sleep( 2 )
    pyautogui.typewrite( "present sir", .5 )
    pyautogui.press('enter')
    sleep( 2 )

sleep_time = 2
def open_chrome_join_meeting():
    pyautogui.moveTo(x1, y1, duration=1)
    pyautogui.click()
    sleep(sleep_time)
    pyautogui.moveTo(x2, y2, duration=1)
    pyautogui.click()
    pyautogui.typewrite(meeting_link,0)
    pyautogui.press('enter')
    sleep(sleep_time + 5)
    pyautogui.moveTo(x3, y3, duration=1)
    pyautogui.click()
    sleep(sleep_time)
    pyautogui.moveTo(x4, y4, duration=1)
    pyautogui.click()
    sleep(sleep_time)
    pyautogui.moveTo(x5, y5, duration=1)
    pyautogui.click()
    sleep(sleep_time + 4)
    pyautogui.moveTo(x6, y6, duration=1)
    pyautogui.click()
    sleep(sleep_time)
    pyautogui.moveTo(x7, y7, duration=1)
    pyautogui.click()
    sleep(sleep_time)
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS ) 
    im1 = pyautogui.screenshot("ss1.png")
    img1 = cv2.imread('ss1.png')
    crop1 =img1[y8:y9, x8:x9]
    cv2.imwrite("ss1.png",crop1)
    

def check_answers(time):
    while(clock() != time):
        sleep(10)
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS ) 
        im2 = pyautogui.screenshot("ss2.png")
        img2 = cv2.imread('ss2.png')
        crop2 =img2[y8:y9, x8:x9]
        cv2.imwrite("ss2.png",crop2)
        try:
            if(returnComparison("ss1.png", "ss2.png",1) >= 2):
                a1,b1=returnMostCommonWord("ss2.png")
                print(a1)
                print(b1)
                if(b1>=2):
                    pyautogui.moveTo(x7, y7, duration=1)
                    pyautogui.click()
                    sleep(1)
                    pyautogui.typewrite(a1, .5)
                    pyautogui.press('enter')
                    sleep(2)
            else:
                print("nothing new here")
        except:
            print(sys.exc_info())
        cv2.imwrite("ss1.png",crop2)
        sleep(20)

def check_for_attendance(time):
    r = sr.Recognizer()
    while(clock() != time):
      
        # Exception handling to handle 
        # exceptions at the runtime 
        try: 
          
            # use the microphone as source for input. 
            with sr.Microphone() as source2: 
               
                # wait for a second to let the recognizer 
                # adjust the energy threshold based on 
                # the surrounding noise level  https://meet.google.com/zrq-ffih-fwh
                r.adjust_for_ambient_noise(source2, duration=0.2) 
              
                #listens for the user's input  
                audio2 = r.listen(source2,phrase_time_limit=5) 
              
                # Using google to recognize audio 
                MyText = r.recognize_google(audio2,language='en-IN') 
                MyText = MyText.lower() 
                print("Did you say "+MyText) 
                if(MyText.find("sanjay")!=-1 or MyText.find("today")!=-1 or MyText.find("sonu")!=-1 or MyText.find("sujoy")!=-1 or MyText.find("sachai")!=-1 or MyText.find("suji")!=-1):
                    answerAttendance()
                
                if(MyText.find("one seventy four")!=-1 or MyText.find("74")!=-1 or  MyText.find("174")!=-1 or  MyText.find("7474")!=-1):
                    # x11,y11,x12,y12,x13,y13=1625,156,1694,976,1872,985
                    answerAttendance()   
           
              
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
          
        except sr.UnknownValueError: 
            print('unknown values')
            print(" ")  

if __name__ == "__main__":
    open_chrome_join_meeting()
    check_answers(40)
    check_for_attendance(60)
    print("exited loop succesfully")   
    sleep(10)
    pyautogui.moveTo(x10, y10, duration=1)
    pyautogui.click()
    fp.close()

