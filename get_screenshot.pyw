"""
Quickly gets screenshot without opening terminal.
"""

import pyscreenshot as ImageGrab
import os
import time

 
def screenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '/snap_full_' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()