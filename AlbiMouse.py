import csv
import time
import os
import threading
from pynput.keyboard import Events as KeyEvents
from pynput.mouse import Events as MousEvents
from AlbiMethods import ClientOrientation

class AlbiMouse():
    def __init__(self   ):
        flocal = "Pathing\Raw_Paths\\"
        name = "Albion Path - "
        num = str(os.listdir(flocal).__len__())
        ext = ".csv"
        file = flocal + name + num + ext
        self.region_x = 1280
        self.region_y = 800
        self.csvfile = open(file, 'w', newline='')
        self.csvwriter = csv.writer(self.csvfile)
        self.start()

    def start(self):
        self.clientx,self.clienty, self.centerx, self.centery = ClientOrientation(self.region_x,self.region_y)
        print('starting mouse')
        while True:
            with KeyEvents() as event:
                answer = str(event.get().key).replace('\'', '')
                if answer == '1':
                    mythread = threading.Thread(target=self.MouseRecorder())
                    mythread.start()
                if answer == '0':
                    print('End')
                    break
        self.csvwriter.writerow((self.centerx, self.clienty))
        self.csvfile.close()
        print('ended')

    def MouseRecorder(self):
        print('Starting!')
        starttime = time.time()
        pressed = False
        while True:
            with MousEvents() as event:
                answer = event.get()
                if hasattr(answer, 'pressed'):
                    if answer.pressed == True:
                        print('start recording')
                        starttime = time.time()
                        tmp = []
                        pressed = True
                    if answer.pressed == False:
                        print('Release')
                        endtime = time.time() - starttime
                        endtime = endtime / tmp.__len__()
                        self.EnterData(tmp,endtime,)
                        pressed == False
                    if str(answer.button) == 'Button.right':
                        print('Closed File')
                        break
                if pressed:
                    x = answer.x
                    y = answer.y
                    tmp.append((x, y))

    def EnterData(self,data,time):
        for i in data:
            ent = i[0],i[1],time
            self.csvwriter.writerow(ent)


AlbiMouse()