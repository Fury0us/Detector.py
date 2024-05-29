#!/usr/bin/python3
# Display the current cursor position and RGB values at the cursor

import pyautogui

def main():
    x, y = pyautogui.position()
    rgb = pyautogui.screenshot().getpixel((x, y))
    print(f"x: {x}, y: {y}, RGB: {rgb}")

main()