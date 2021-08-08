import cv2
import d3dshot
import os
import time
from pynput.keyboard import Events as KeyEvents
from AlbiMethods import ClientOrientation

class AlbiRecorder():
    def __init__(self):
        self.region_x = 1280
        self.region_y = 800
        self.screenshot = d3dshot.create(capture_output='numpy')
        self.LoadPhotoFolders()

    def Main(self):
        self.clientx,self.clienty, self.centerx, self.centery = ClientOrientation(self.region_x,self.region_y)
        opts = {'1': self.Capture_Screen, '2': self.SceenCaptureLoop,'9': self.End}
        print('1- Capture Data 2- Read Screen 9- End')
        while True:
            with KeyEvents() as event:
                answer = str(event.get().key).replace('\'','')
            if answer in opts:
                break
        print(answer)
        opts[answer]()

    def SceenCaptureLoop(self):
        cas = None
        print('Add Classifier? -y?')
        addclassifier = input()
        if addclassifier == 'y':
            cas = self.CascadeClassifier()
        while True:
            key, frame = self.ShowFrame(region=(self.clientx, self.clienty, self.clientx+self.region_x, self.clienty+self.region_y), cas=cas)
            if key == 48:
                cv2.destroyAllWindows()
                break
        self.Main()

    def Capture_Screen(self):
        save_local,fext,num = self.CheckFolder()
        while save_local:
            with KeyEvents() as eventz:
                ans = str(eventz.get().key).replace('\'','')
                print('Press 1 to capture | Press 0 to End')
                if ans == '1':
                    print('press 2 to save?')
                    time.sleep(0.50)
                    with KeyEvents() as eventz:
                        ans = str(eventz.get().key).replace('\'', '')
                    key,frame = self.ShowFrame(region=(self.clientx, self.clienty, self.clientx+self.region_x, self.clienty+self.region_y),name=str(num), waitkey=3)
                    if ans == '2':
                        num = num+1
                        saveas = save_local + str(num) + fext
                        print('saving '+saveas)
                        cv2.imwrite(saveas, frame)
                        print('saved')
                        cv2.destroyAllWindows()
                    else:
                        print('not saving')
                if ans == '0':
                    break
        self.Main()

    def ShowFrame(self,region,name='check me out',cas=None, waitkey = 1):
        frame = self.screenshot.screenshot(region=(int(region[0]), int(region[1]), int(region[2]), int(region[3])))
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        if cas is not None:
            data = cas.detectMultiScale(frame, minSize=(0, 0), maxSize=(30 ,30))
            for (x, y, w, h) in data:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                x2 = (x+w)
                y2 = (y+h)
                cop = frame[x2:y2 , x:y]
                save_local = 'Photos/Maps/p/'
                num = str(os.listdir(save_local).__len__())
                saveas = save_local+num+".png"
                print(cop)
                cv2.imwrite(saveas, cop)
                print("Detected save")

        cv2.imshow(name, frame)
        key = cv2.waitKey(waitkey)
        return key, frame

    def CheckFolder(self):
        while True:
            print('Enter Folder')
            folder = input()
            if folder in self.PhotoFolders:
                save_local = 'Photos/' + folder + '/Gathered_Photos/'
                fext = '.png'
                num = os.listdir(save_local).__len__()
                break
                print(str(num)+' Images in This Folder')
            else:
                print(' Folder not Found')
            if folder == 'end':
                return False, False, False
        return save_local,fext,num

    def CascadeClassifier(self):
        print('Set Cascade')
        filename = input()
        dir2cas = "Photos\\" + filename + "\classifier\cascade.xml"
        cascade = cv2.CascadeClassifier(dir2cas)
        return cascade

    def LoadPhotoFolders(self):
        self.PhotoFolders = os.listdir('Photos')

    def End(self):
        print('End')

