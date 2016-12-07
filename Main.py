import Flags
import Commands
import pyautogui
import socket
import struct
import Constants
import thread
import NewSliceOfTask
# --------------main program------------------

class MousePadServerPy(object):

    # 	=====global vars =====

    lastx = 0
    lasty = 0
    flag_block = -1
    firstTimeCoordinate = True


    def runCommand(self):

        socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpPort = Constants.TCP_PORT
        socketVar.bind(('', tcpPort))
        socketVar.listen(2)

        hostname = socket.gethostname()
        sizeOfMessage = len(hostname)
        while True:



            connectionSocket, address = socketVar.accept()
            flag = connectionSocket.recv(20).decode('utf-8')

            print flag


            # search block for device


            if flag == Flags.FLAG_SEARCH:
                 try:

                     print "DEBUG: search block"
                     connectionSocket.send(struct.pack("!H", sizeOfMessage))
                     connectionSocket.send(hostname)
                     continue

                 except ValueError:
                     print "exception = ",ValueError.message


            # close window action
            elif flag == Flags.FLAG_OPENED_PAD:
                try:
                    print "DEBUG: close window block"

                    thread.start_new_thread(NewSliceOfTask.task,(flag,connectionSocket))


                    continue

                except ValueError:
                    print "exception = ", ValueError.message





















# --------------main program------------------


# calling the program




m = MousePadServerPy()
m.runCommand()




