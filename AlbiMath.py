import pyautogui
import math
import csv
import os
import time


class AlbiCenterCircle():
    def __init__(self):
        self.radius = 350

    def MakeRadianData(self,Raw_Paths):
        csvfile, csvwriter = self.MakeRadianFile()
        a = open(Raw_Paths, newline='')
        b = csv.reader(a)
        c = list(b)
        xy = c.pop()
        x1 = float(xy[0])
        y1 = float(xy[1])
        pyautogui.moveTo((x1,y1))
        print(c)
        for i in c:
            x2 = int(i[0])
            y2 = int(i[1])
            radian = self.FindRadians(x2,y2,x1,y1)
            ent = (radian,float(i[2]))
            print(ent)
            csvwriter.writerow(ent)
        print(c.__len__())
        csvfile.close()

    def ReadRadianData(self,RadianFile,centx,centy):
        a = open(RadianFile, newline='')
        b = csv.reader(a)
        c = list(b)
        a.close()
        x = centx
        y = centy
        radianList = []
        pyautogui.moveTo((x, y))
        for i in c:
            radian = float(i[0])
            wtime = float(i[1])
            newpoints = self.FindDegreedPoint(x,y, radian)
            ent = (newpoints,wtime)
            radianList.append(ent)
            pyautogui.mouseDown(newpoints[0],newpoints[1])
            time.sleep(wtime)
        pyautogui.mouseUp()
        return radianList

    def FindDegreedPoint(self,orginx,orginy,radian):
        newx = orginx + (self.radius * math.sin(radian))
        newy = orginy + (self.radius * math.cos(radian))
        xy = newx,newy
        return xy

    def FindRadians( self,destination_x,destination_y,origin_x,origin_y):
        deltaX = destination_x - origin_x
        deltaY = destination_y - origin_y
        degrees_temp = math.atan2(deltaX, deltaY) / math.pi * 180
        if degrees_temp < 0:
            degrees_final = 360 + degrees_temp
        else:
            degrees_final = degrees_temp
        radian = math.radians(degrees_final)
        return radian

    def MakeRadianFile(self):
        name = "Pathing\Radians_Paths\Cracked Earth Radians - "
        num = str(os.listdir("Pathing\Radians_Paths").__len__())
        ext = ".csv"
        file = name + num + ext
        print(file)
        csvfile = open(file, 'w', newline='')
        csvwriter = csv.writer(csvfile)
        return csvfile, csvwriter



Raw_Path = "Pathing\Raw_Paths\Cracked Earth - 1.csv"
Path1 = "Pathing\Radians_Paths\Routes\Cracked Earth Radians - Gate2Flag.csv"
Path2 = "Pathing\Radians_Paths\Cracked Earth Radians - 1.csv"
a = AlbiCenterCircle()
#a.MakeRadianData(Raw_Path)
a.ReadRadianData(Path1,924,524)
a.ReadRadianData(Path2,924,524)