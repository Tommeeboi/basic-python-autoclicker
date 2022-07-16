import pyautogui
import time

limit = input("How long do you want to click for? (Seconds): ")
delay = input("How long do you want to wait before the programs starts clicking? (Seconds): ")

fixedLimit = int(limit) * 9.5
fixedDelay = int(delay)
i = 0

print(f"Starting in {fixedDelay} seconds!")
time.sleep(fixedDelay)

print(f"Clicking... (For {limit} Seconds)")
while i < fixedLimit:

    pyautogui.click()

    i+=1