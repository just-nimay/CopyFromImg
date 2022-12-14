import pytesseract
from PIL import ImageGrab
import pynput
import clipboard
import time

import keyboard

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pos = {}



language = 'rus'


avaible_lang = ['rus', 'eng']

def make_screenshot(pos):
    print('geting positions...')
    x1 = round(pos['pos_1'][0])
    y1 = round(pos['pos_1'][1])

    x2 = round(pos['pos_2'][0])
    y2 = round(pos['pos_2'][1])
    print('get position succesfull')
    print('making screenshot...')

    image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    print('screenshot makes succesfull')

    return image

def get_text(image):
    print('lang in function:', language)
    
    return pytesseract.image_to_string(image, lang=language)



def on_click(x, y, button, pressed):

    if pressed:
        pos['pos_1'] = (x, y)
    else:
        pos['pos_2'] = (x, y)    
    if not pressed:

        # Stop listener
        return False

def start_getting_pos():
    with pynput.mouse.Listener(
    on_click=on_click) as listener:
        listener.join()

def recognition():
    print('COPY TEXT')
    print('waiting for select area...')
    start_getting_pos()
    print('i get the position')
    
    print('making screenshot...')
    image = make_screenshot(pos)
    print('i make screenshot')

    text = get_text(image)
    print('i get text')
    print(text)
    clipboard.copy(text) 
    print('Copied succesfully!')

def change_lang():
    global language
    print('CHANGE LANGUAGE')
    while True:
        language = input('enter language (avaible: Russian - "rus", English - "eng"):')
        if language not in avaible_lang:
            print('This is not avaible language!')
        else:
            print('Language changed succesfily!')
            print(f'current language: {language}')
            return
           


hello = '''
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LIKE YOU!    |  |  |     |         |      |
     |  |  And many other |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"     
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
'''
print(hello)
print('\nHi!')


print(f'current language is: "{language}"\n')
print('for change language press "ctrl+shift+x"\n')
print('press "ctrl+shift+s" for get text\nfor exit press "esc"')
                        
keyboard.add_hotkey("ctrl+shift+s", recognition)
keyboard.add_hotkey("ctrl+shift+x", change_lang)
keyboard.wait('esc')

bye = '''
              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |     See you           | |
              | |      next time        | |
              | |       Goodbye         | |
              | |                       | |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

print(bye)
time.sleep(2.5)










