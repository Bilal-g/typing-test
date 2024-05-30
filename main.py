import curses
from random import randint
import time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()

curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

GREENONBLACK = curses.color_pair(1)
REDONBLACK = curses.color_pair(2)

def GenerateRandomText(numOfWords):
    with open("words.txt", 'r') as file:
        allWordsList = file.readlines()
    newWordsList = []
    for i in range(0, numOfWords):
        newWord = allWordsList[randint(0, len(allWordsList) - 1)].replace("\n", "")
        newWordsList.append(newWord)
    newWordsText = ""
    for j in newWordsList:
        newWordsText += j + " "
    
    return newWordsText.rstrip()

def PrintWPM():
    WPMWindow = curses.newwin(0, 15, 4, 0)
    wpm = 60 * len(text.split(" ")) / elapsedTime
    WPMWindow.addstr("WPM: " + (str(round(wpm, 2))))
    WPMWindow.refresh()
    WPMWindow.erase()

def PrintAccuracy():
    accuracyWindow = curses.newwin(0, 15, 2, 0)
    correct = 0
    for i in range(0, len(textList)):
        if textList[i] == userTextList[i]:
            correct += 1
    
    accuracy = correct * 100 / len(userTextList)
    accuracyWindow.addstr("Accuracy: " + (str(round(accuracy, 2))))
    accuracyWindow.refresh()
    accuracyWindow.erase()

def PressBackspace():
    cursorCoords = stdscr.getyx()
    x = cursorCoords[1] - 1
    y = cursorCoords[0]
    stdscr.move(y, x)
    stdscr.addch(textList[index - 1])
    stdscr.move(y, x)
    userTextList.pop()


text = GenerateRandomText(20)
textList = list(text)
userTextList = []
index = 0

stdscr.addstr(text)
stdscr.move(0, 0)

timerIsStarted = False


while True:
    key = stdscr.getch()
    if not timerIsStarted:
        startTime = time.perf_counter()
        timerIsStarted = True
    
    if 8 == key:
        if index != 0:
            PressBackspace()
            index -= 1
    
    elif 9 == key:
        text = GenerateRandomText(20)
        textList = list(text)
        userTextList = []
        stdscr.clear()
        stdscr.addstr(text)
        stdscr.move(0, 0)
        stdscr.refresh()
        index = 0
        timerIsStarted = False

    elif chr(key) == textList[index]:
        stdscr.addch(textList[index], GREENONBLACK)
        index += 1
        userTextList.append(chr(key))
    elif chr(key) != textList[index]:
        stdscr.addch(textList[index], REDONBLACK)
        index += 1
        userTextList.append(chr(key))

    stdscr.refresh()
    if index == len(textList):
        break

endTime = time.perf_counter()
elapsedTime = endTime - startTime

PrintAccuracy()
PrintWPM()
stdscr.refresh()
stdscr.getch()