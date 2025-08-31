# import re
# test  = "reminde me after 10 second that sip some water"


# if "reminde" in test.lower():
#     task = test.lower().split("that")[1]


# # numbers = re.findall(r'\d+', test)

# # # print(int(num for num in numbers))

# # numbers = [int(num) for num in numbers]
# # for num in numbers:
# #     final = int(num)

# # print(final)




# match = re.search(r'\d+', test)
# if match:
#     number = int(match.group())
#     print(number)   # 30

import pyautogui
import uuid
# import pyscreeze

screenshort = pyautogui.screenshot()
id = uuid.uuid1()
screenshort.save(f"Images/{id}.jpg")

# with open(f"Images/{id}.png", "w") as file:




# import pyautogui

# im = pyautogui.screenshot()
# im.save("SS1.jpg")