import pyautogui
import keyboard
print('This is a weird hotkey maker by the great incompetent and nooby CybearTron')
print('Ok so me being so bad... I couldnt quite implement the stop feature.... So you gotta..... Ummm... Stop it on ur own by struggling to open this tab and closing it... ☺')
m=2000
n=input('Enter The key that shall be pressed...Currently only one key works......   ')
hotk=input('Hotkey button i.e. which key starts the hotkey(Try not to put the hotkey and the key to be pressed the same or ur pc go destructed hehehe)U can use more than one key for this like ctrl+`:     ')

def hotkeyattack():
    
    while m==2000:
        
    
       pyautogui.press(n)
      
       
    
keyboard.add_hotkey(hotk, lambda:hotkeyattack())    





hwlo=input()
