"""
Types a text with a speed similar to a human.
Installed xdotool on Linux for this.
"""

import subprocess
import time
import sys
# open the textfile
text = "hello to my little friend" #open(sys.argv[1]).read().strip()
for ch in text:
    # type out the text
    subprocess.call(["xdotool", "type", ch])
    # increase or decrease the time below to type slower or faster
    time.sleep(0.1)