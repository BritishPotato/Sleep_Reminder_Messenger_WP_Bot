"""
You've Been Staying Up Too Late Sender WhatsApp Web Bot
aka "YBSUTLSWWB"

In "messages.txt", repeating messages are after
the first empty line.

TODO
Just needs to check between 01.00 and 06.00 and
we are done!
"""
import pyautogui
import pyperclip
import time
import datetime

# Generally WP background (229, 221, 213)
# Message (255, 255, 255)
# Check Pixel at pyautogui.pixel(379,972)

# Pause interval between each PyAutoGUI call.
pyautogui.PAUSE = 3.5
# Failsafe TRUE/FALSE?
pyautogui.FAILSAFE = True

# Pixel location constants.
emoji_loc = (368,1052)
message_box_loc = (834, 1048)
response_loc = (379,972)
offline_loc = (1285, 1041)

# Emoticons :), requires pyperclip (HACK)
happy_bot = "┌|^ω^|┘"
shrug_bot = r"¯\_|ツ|_/¯"


# Get messages.txt content.
with open ("messages.txt", "r") as myfile:
    data=myfile.read().split("\n")

hour_start = 0
hour_end = 0
gif_search = ""
gif_messages = []
repeating_messages = []
option_number = 0
for i in data:
    if i == "# Start and End hours":
        option_number = 1
    elif i == "# GIF Search Term":
        option_number = 2
    elif i == "# GIF Messages":
        option_number = 3
    elif i == "# Repeating Messages":
        option_number = 4
    
    elif i:
        if option_number == 1:
            hour_start = int(i[:2])
            hour_end = int(i[3:5])
        if option_number == 2:
            gif_search = i
        elif option_number == 3:
            gif_messages.append(i)
        elif option_number == 4:
            repeating_messages.append(i)

def click_on_message_box():
    pyautogui.click(message_box_loc)

# Define clicks.
def click_on_emoji():
    pyautogui.click(emoji_loc)

def click_offline():
    pyautogui.click(offline_loc)

def click_on_gif(write=True):
    click_on_emoji()
    pyautogui.typewrite(gif_search, interval=0.15)
    pyautogui.typewrite(["down"] * 7, interval=0.1)
    pyautogui.typewrite(["enter"])

print("Waiting for time...")
while not (hour_start <= datetime.datetime.now().hour < hour_end):
    time.sleep(1800)
print("The time has come.")
print("Sending initial message.")

click_on_message_box()
pyautogui.typewrite("Yo", interval=0.5)
pyautogui.typewrite(["enter"], interval=0.1)
click_offline()

print("Waiting for response...")
check_response = pyautogui.pixel(379,972)
while check_response != (255, 255, 255):
    time.sleep(30)
    check_response = pyautogui.pixel(379,972)
print("Response received.")

print("Sending GIF and GIF message(s)...")
click_on_gif()
for i, gif_message in enumerate(gif_messages):
    pyautogui.typewrite(gif_message, interval=0.15)
    if i == 1:
        print("success")
        pyperclip.copy(happy_bot)
        pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite(["enter"])
click_offline()
print("Message sent")

# If they send message:
print("Waiting for response...")
while hour_start <= datetime.datetime.now().hour < hour_end:
    if pyautogui.pixel(response_loc[0], response_loc[1]) == (255, 255, 255):
        print("Redundant response received...")
        print("Sending repeating message(s)...")
        click_on_message_box()
        for i, repeating_message in enumerate(repeating_messages):
            pyautogui.typewrite(repeating_message, interval=0.2)
            if i == 1:
                pyperclip.copy(shrug_bot)
                pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(["enter"])
        click_offline()
        print("Message sent.")
    else:
        time.sleep(30)

