import pyautogui

def ClientOrientation(region_x, region_y):
    local = "Photos\Client\Albion Symbol.png"
    while True:
        loc = pyautogui.locateOnScreen(local)
        if loc is not None:
            location_x = int(loc[0])
            location_y = int(loc[1])
            while True:
                img = pyautogui.screenshot(region=(location_x, location_y, region_x, region_y))
                center = pyautogui.locateCenterOnScreen(img)
                if center:
                    break
            print(center)
            center_x = center.x
            center_y = center.y
            break
    return location_x, location_y, center_x, center_y
