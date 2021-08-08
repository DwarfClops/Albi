import json
import cv2
import pyautogui
from pynput.keyboard import Events as KeyEvents
import math

def MakeList():
    folder = input("Enter Folder")
    photodir = 'Photos/'+folder+'/'+folder+'/images'
    newlist = open(folder+'List.txt', 'w')
    a = open('Photos/'+folder+'/'+folder+'/annotations.json')
    c = json.load(a)
    c.pop('___sa_version___')
    for i in c:
        Photo = i
        PhotoData = c[i]
        itms = PhotoData['instances']
        print(itms)
        for obj in itms:
            points = obj['points']
            x1 = str(int(points['x1']))
            y1 = str(int(points['y1']))
            x2 = str(int(points['x2']))
            y2 = str(int(points['y2']))
            entry = photodir + '/' + Photo + ' ' + x1 + ',' + y1 + ',' + x2 + ',' + y2 + '\n'
            print(entry)
            newlist.write(entry)
    newlist.close()

def CreatePositiveImages():
    folder = input("Enter Folder")
    print('Creating Neg Images')
    clist = open(folder+'List.txt','r')
    savelocal = 'Photos/'+folder+'/p/'
    photodir = 'Photos/'+folder+'/'+folder+'/images/'
    num = 0
    for i in clist:
        print(i)
        st = i.split(' ')
        name = st[0].split('/')[-1]
        photofile = photodir+name
        print(photofile)
        img = cv2.imread(photofile)
        points = tuple(st[1].split(','))
        print(points)
        x1 = int(points[0])
        x2 = int(points[1])
        y1 = int(points[2])
        y2 = int(points[3])
        cop = img[x2: y2, x1:y1]
        if cop.size != 0:
            pfilename = str(num)+'.png'
            print(pfilename)
            savefile = savelocal+pfilename
            print(savefile)
            cv2.imwrite(savefile,cop)
            num = num + 1

def doCircleMath():
    loc = pyautogui.locateOnScreen("Photos\Maps\Albion Symbol.png")
    print(loc)
    locx = loc[0]
    locy = loc[1]
    while True:
        with KeyEvents() as event:
            print('End??')
            answer = str(event.get().key).replace('\'', '')
            if answer == '1':
                pos = pyautogui.position()
                x = pos.x
                y = pos.y
                distance = math.sqrt(((locx - x) ** 2) + ((locy - y) ** 2))
                print(distance)
                this = x + distance
                that = y + distance
                b = (this,that)
                c = (locx,locy)
                d = (x,y)
                print(b)
                print(c)
                print(d)

def trythis():
    filez = 'Cracked Earth - 19.csv'
    a = open(filez)
    b = a.read()