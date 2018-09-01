"""
Testing out pyautogui
https://pyautogui.readthedocs.io/en/latest/cheatsheet.html
"""

import pyautogui

# current mouse x and y
pyautogui.position()

# current screen resolution width and height
pyautogui.size()

# True if x & y are within the screen.
pyautogui.onScreen(x, y)

# 2.5 second pause after each PyAutoGUI call
pyautogui.PAUSE = 2.5

pyautogui.FAILSAFE = True

# move mouse to XY coordinates over num_second 
# seconds
pyautogui.moveTo(x, y, duration=num_seconds)  

# move mouse relative to its current position
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  

# Calling click() just clicks the mouse once with the
# left button at the mouse’s current location, but
# the keyword arguments can change that:
# ("left", "middle", 'right')
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

# for readability
# >>> pyautogui.rightClick(x=moveToX, y=moveToY)
# >>> pyautogui.middleClick(x=moveToX, y=moveToY)
# >>> pyautogui.doubleClick(x=moveToX, y=moveToY)
# >>> pyautogui.tripleClick(x=moveToX, y=moveToY)

pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
