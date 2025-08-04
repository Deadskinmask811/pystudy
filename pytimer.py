import time
import math
import subprocess

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
                print(f"Time remaining: 0{time_remaining[0]}:0{time_remaining[1]}", end="\r")
    else:
        print(f"Time remaining: {time_remaining[0]}:{time_remaining[1]}", end="\r")

def playAlarm():
    subprocess.run("/home/coty/Projects/pythontimer/playsound.sh")

def getUserInput():
    user_option = input("(1) 1 Minute, (2) 5 Minutes, (3) 10 Minutes, (c) Custom Time...\n")
    match user_option:
        case "1":
            return [1, 0] 
        case "2":
            return [5, 0]
        case "3":
            return [10, 0]
        case "c":
            return customTimeInput() 
        case _:
            raise Exception

    
def customTimeInput():
    customTime = int(input("Input num of minutes to start timer with\n"))
    return [customTime,0]

def main():
    studyTime = None
    while(type(studyTime) != list):
        try:
            print("Select time option")
            studyTime = getUserInput()
        except Exception as e:
            print(f"\n***** Invalid Input *****\n")
        
    timer(studyTime)
    print("time over")
    playAlarm()
     
if __name__ == "__main__":
    main()
