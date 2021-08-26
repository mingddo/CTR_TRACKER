from time import sleep
import pyautogui
import time
import pyperclip

def get_positions():
    for i in range(30):
        print(pyautogui.position())
        time.sleep(.5)

def click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click()
    pyautogui.click(x,y,clicks =5, interval=1)

def typewrite(txt):
    pyperclip.copy(txt)
    # pyautogui.typewrite(['a','b','c'], interval=0.1)
    # pyautogui.typewrite('\n', interval=0.1)
    # pyautogui.typewrite(txt, interval=0.1)
    pyautogui.hotkey('ctrl', 'v')

def click_center_object(obj):
    click_center = pyautogui.locateCenterOnScreen(obj, confidence=0.9)
    print('click_center_object',click_center )
    pyautogui.click(click_center)

if __name__ == '__main__':
    sleep(2)
    # for _ in range(5):
    #     click_center_object('7.png')
# click_center_object('7.png')
# click_center_object('9.png')
# click_center_object('+.png')
# click_center_object('2.png')
# click_center_object('7.png')
# click_center_object('=.png')
    ch = '아린아 이것은 봇일까?'
    click_center_object('chat1.png')
    typewrite(ch)
    click_center_object('send.png')
