
import Flags
import Commands
import pyautogui
import socket
import struct
import Constants




def task(flag,connectionSocket):


    print "thread started"

    # close window action
    if flag == Commands.COMMANDS_CLOSE_WINDOW:
        try:
            print "DEBUG: close window block"

            pyautogui.keyDown('alt')
            pyautogui.keyDown('F4')

            pyautogui.keyUp('alt')
            pyautogui.keyUp('F4')



        except ValueError:
            print "exception = ", ValueError.message




            # escape button action
    elif flag == Commands.COMMANDS_ESC:
        try:
            print "DEBUG: close window block"

            pyautogui.keyDown('esc')
            pyautogui.keyUp('esc')



        except ValueError:
            print "exception = ", ValueError.message



            # Enter action
    elif flag == Commands.COMMANDS_ENTER:
        try:
            print "DEBUG: Enter block"

            pyautogui.keyDown('enter')

            pyautogui.keyUp('enter')



        except ValueError:
            print "exception = ", ValueError.message



            # mouse left click
    elif flag == Commands.COMMANDS_MOUSE_LEFT_CLICK:
        try:
            print "DEBUG: left click block"
            x, y = pyautogui.position()
            pyautogui.mouseDown(x, y, 'left', 0.0)
            pyautogui.mouseUp(x, y, 'left', 0.0)



        except ValueError:
            print "exception = ", ValueError.message




            # mouse left long click
    elif flag == Commands.COMMANDS_MOUSE_LEFT_LONG_CLICK:
        try:
            print "DEBUG: left long click block"
            x, y = pyautogui.position()
            pyautogui.mouseDown(x, y, 'left', 0.0)



        except ValueError:
            print "exception = ", ValueError.message




            # close window action
    elif flag == Commands.COMMANDS_MOUSE_RIGHT_CLICK:
        try:
            print "DEBUG: mouse right block"

            x, y = pyautogui.position()
            pyautogui.mouseDown(x, y, 'right', 0.0)
            pyautogui.mouseUp(x, y, 'right', 0.0)



        except ValueError:
            print "exception = ", ValueError.message







            # scroll up action
    elif flag == Commands.COMMANDS_SCROLL_VERTICAL_UP:
        try:
            print "DEBUG: mouse scroll up block"

            pyautogui.vscroll(-190)



        except ValueError:
            print "exception = ", ValueError.message







            #  scroll down action
    elif flag == Commands.COMMANDS_SCROLL_VERTICAL_DOWN:
        try:
            print "DEBUG: mouse scroll down block"
            pyautogui.vscroll(190)



        except ValueError:
            print "exception = ", ValueError.message



