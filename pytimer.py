import time
import math
import subprocess
import random
import webbrowser

def timer(studyTime):
    time_remaining = studyTime
    while time_remaining[0] >= 0 and time_remaining[1] >= 0:
        if time_remaining[1] == 0:
            if time_remaining[0] >= 1:
                time_remaining[0] -= 1
                time_remaining[1] = 60
        time_remaining[1] -= 1
        displayTime(time_remaining)
        time.sleep(1.0)

def displayTime(time_remaining):
    if time_remaining[1] < 10:
        print(f"\rTime remaining: 0{time_remaining[0]}:0{time_remaining[1]}", end="", flush=True)
    else:
        print(f"\rTime remaining: {time_remaining[0]}:{time_remaining[1]}", end="", flush=True)

def playAlarm():
    subprocess.run("/home/coty/Projects/pythontimer/playsound.sh")

def getUserInput():
    user_option = input()
    match user_option:
        case "1":
            return [1, 0] 
        case "2":
            return [5, 0]
        case "3":
            return [10, 0]
        case "4":
            return [15, 0]
        case "5":
            return [30, 0]
        case "6":
            return [60, 0]
        case "c":
            return customTimeInput() 
        case "m":
            return getMusic() 
        case _:
            raise Exception

def displayOptions():
    print("##################")
    print("(1) 1 Minute")
    print("(2) 5 Minute")
    print("(3) 10 Minutes")
    print("(4) 15 Minutes")
    print("(5) 30 Minutes")
    print("(6) 1 Hour")
    print("(c) Custom Time")
    print("(m) Get random song copied to clipboard for study vibes")
    print("##################")
    
def customTimeInput():
    customTime = int(input("Input number of minutes to start timer with\n"))
    return [customTime,0]

def getMusic():
    try:
        print("trying to open file...")
        with open("playlist.txt", "r") as file_object:
            content = file_object.read()
            lines = content.split()
            rand_num = random.randint(0, len(lines) - 1) 
            url = lines[rand_num]
            webbrowser.open(url, new=2, autoraise=True)
            return url 
    except FileNotFoundError:
        print("No such file exists in script directory")

def main():
    studyTime = None
    while(type(studyTime) != list):
        try:
            displayOptions()
            studyTime = getUserInput()
        except Exception as e:
            print(f"\n***** Invalid Input *****\n")
    
    timer(studyTime)
    print("time over")
    playAlarm()
     
if __name__ == "__main__":
    main()
