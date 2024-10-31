import cv2
import mediapipe as mp
import time
from pynput.keyboard import Key, Controller
import subprocess
import pyttsx3


def pick(lmList, hand, sentence, chosen):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][0] < lmList[hand][fingerPIP[point]][0]:
            pass
        else:
            return sentence, chosen
    if lmList[hand][4][1] < lmList[hand][0][1] and lmList[hand][4][0] < lmList[hand][5][0] and lmList[hand][4][1]\
            < lmList[hand][7][1]:
        chosen = True

    return sentence, chosen

def choose(lmList, hand, sentence, picked, chosen):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][0] < lmList[hand][fingerPIP[point]][0]:
            pass
        else:
            return sentence, picked, chosen
    if lmList[hand][4][1] < lmList[hand][0][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][4][1]\
            < lmList[hand][7][1]:
        picked = False
        chosen = False
    return sentence, picked, chosen

def space(lmList, hand, sentence, chosen):
    if lmList[hand][8][0] > lmList[hand][6][0]:
        for point in range(1, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][0] < lmList[hand][fingerPIP[point]][0] and lmList[hand][fingerPIP[point]][0] < lmList[hand][8][0]:
                pass
            else:
                return sentence, chosen
        if lmList[hand][4][1] < lmList[hand][0][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][4][1] \
                < lmList[hand][7][1]:
            chosen = True
            sentence += " "
    return sentence, chosen

def backspace(lmList, hand, sentence, chosenBack):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][0] < lmList[hand][fingerPIP[point]][0]:
            pass
        else:
            return sentence, chosenBack
    if lmList[hand][4][1] > lmList[hand][0][1] and lmList[hand][4][0] < lmList[hand][5][0] and lmList[hand][4][1] \
            > lmList[hand][7][1] and lmList[hand][5][1] > lmList[hand][17][1]:
        sentence = sentence[:-1]
        chosenBack = True
    return sentence, chosenBack

def chooseBack(lmList, hand, sentence, chosenBack):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][0] < lmList[hand][fingerPIP[point]][0]:
            pass
        else:
            return sentence, chosenBack
    if lmList[hand][4][1] > lmList[hand][0][1] and lmList[hand][4][0] > lmList[hand][7][0] and lmList[hand][4][1] \
            > lmList[hand][7][1] and lmList[hand][5][1] > lmList[hand][17][1]:
        chosenBack = False

    return sentence, chosenBack

def play(lmList, hand, sentence, chosen):
    """
    This function checks if the user wants to playback their sentence and then uses text to speech to play it back.
    """
    if lmList[hand][20][0] > lmList[hand][18][0]:
        for point in range(len(fingerMCP) - 1):
            if lmList[hand][fingerTIP[point]][0] < lmList[hand][fingerPIP[point]][0] and lmList[hand][fingerPIP[point]][0] < lmList[hand][20][0]:
                pass
            else:
                return sentence, chosen
        if lmList[hand][4][1] < lmList[hand][0][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][4][1] \
                < lmList[hand][7][1]:
            engine.say(str(sentence))
            engine.runAndWait()
            sentence = ""

    return sentence, chosen

def A(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] < lmList[hand][5][1] and lmList[hand][4][0] < lmList[hand][3][0] and lmList[hand][5][0] < lmList[hand][18][0]:
        picked = True
        sentence += "a"
    return sentence, picked

def B(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerMCP[point]][1] and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerPIP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][17][0]\
            - lmList[hand][5][0] > lmList[hand][20][0] - lmList[hand][8][0] and lmList[hand][5][0] < lmList[hand][18][0]:
        picked = True
        sentence += "b"
    return sentence, picked

def C(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerMCP[point]][1] and lmList[hand][fingerTIP[point]][1]\
                > lmList[hand][fingerDIP[point]][1] and lmList[hand][5][0] < lmList[hand][18][0]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] < lmList[hand][5][0] and lmList[hand][17][0]\
            - lmList[hand][5][0] > lmList[hand][20][0] - lmList[hand][8][0]:
        picked = True
        sentence += "c"
    return sentence, picked

def D(lmList, hand, sentence, picked):
    if lmList[hand][8][1] < lmList[hand][6][1]:
        for point in range(1, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0]:
            picked = True
            sentence += "d"
    return sentence, picked

def E(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][11][1] > lmList[hand][18][1] and lmList[hand][14][1] < lmList[hand][11][1] and lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][9][0] and lmList[hand][5][0] < lmList[hand][18][0]:
            picked = True
            sentence += "e"

    return sentence, picked

def F(lmList, hand, sentence, picked):
    if lmList[hand][8][1] > lmList[hand][6][1]:
        for point in range(1, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
                return sentence, picked
        if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][20][0]\
                > lmList[hand][17][0] and lmList[hand][5][0] < lmList[hand][18][0]:
            picked = True
            sentence += "f"

    return sentence, picked

def G(lmList, hand, sentence, picked):
    if lmList[hand][8][0] < lmList[hand][6][0]:
        for point in range(1, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][0] > lmList[hand][fingerPIP[point]][0]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] < lmList[hand][9][1] and lmList[hand][4][0] < lmList[hand][5][0] and lmList[hand][5][0] > lmList[hand][18][0]:
            picked = True
            sentence += "g"
    return sentence, picked

def H(lmList, hand, sentence, picked):
    if lmList[hand][8][0] < lmList[hand][6][0] and lmList[hand][12][0] < lmList[hand][10][0]:
        for point in range(2, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][0] > lmList[hand][fingerPIP[point]][0]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] < lmList[hand][5][0] and\
                lmList[hand][5][0] > lmList[hand][18][0] and lmList[hand][12][1] - lmList[hand][8][1] <\
                lmList[hand][13][1] - lmList[hand][5][1]:
            picked = True
            sentence += "h"

    return sentence, picked

def I(lmList, hand, sentence, picked):
    if lmList[hand][20][1] < lmList[hand][18][1]:
        for point in range(len(fingerMCP) - 1):
            if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][9][0] and lmList[hand][5][0] < lmList[hand][18][0]:
                picked = True
                sentence += "i"

    return sentence, picked

def J(lmList, hand, sentence, picked):
    if lmList[hand][20][0] < lmList[hand][18][0]:
        for point in range(len(fingerMCP) - 1):
            if lmList[hand][fingerTIP[point]][0] > lmList[hand][fingerPIP[point]][0]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] < lmList[hand][6][1] and lmList[hand][4][0] < lmList[hand][5][0] and lmList[hand][5][0] > lmList[hand][18][0]:
            picked = True
            sentence += "j"

    return sentence, picked

def K(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if point <= 1 and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerMCP[point]][1]:
            pass
        elif point > 1 and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] < lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0]\
            and lmList[hand][12][0] > lmList[hand][13][0] and lmList[hand][8][0] < lmList[hand][9][0]:
        picked = True
        sentence += "k"
    return sentence, picked

def L(lmList, hand, sentence, picked):
    if lmList[hand][8][1] < lmList[hand][6][1]:
        for point in range(1, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] < lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0]:
            picked = True
            sentence += "l"
    return sentence, picked

def M(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][11][1] < lmList[hand][18][1] and lmList[hand][14][1] < lmList[hand][11][1] and lmList[hand][4][0] > lmList[hand][9][0] and lmList[hand][5][0] < lmList[hand][18][0]:
            picked = True
            sentence += "m"

    return sentence, picked

def N(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][11][1] < lmList[hand][19][1] and lmList[hand][14][1] > lmList[hand][11][1] and lmList[hand][4][0] > lmList[hand][9][0] and lmList[hand][5][0] < lmList[hand][18][0]:
            picked = True
            sentence += "n"

    return sentence, picked

def O(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][11][1] > lmList[hand][18][1] and lmList[hand][14][1] < lmList[hand][11][1] and lmList[hand][4][1] >\
            lmList[hand][5][1] and lmList[hand][4][0] < lmList[hand][9][0] and lmList[hand][4][0] > lmList[hand][5][0] \
            and lmList[hand][5][0] < lmList[hand][18][0]:
            picked = True
            sentence += "o"

    return sentence, picked

def P(lmList, hand, sentence, picked):
    if lmList[hand][8][0] < lmList[hand][6][0] and lmList[hand][12][0] < lmList[hand][10][0]:
        for point in range(2, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][0] > lmList[hand][fingerPIP[point]][0]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] < lmList[hand][5][0] and \
                lmList[hand][5][0] > lmList[hand][18][0] and lmList[hand][12][1] - lmList[hand][8][1] >\
                lmList[hand][13][1] - lmList[hand][5][1]:
            picked = True
            sentence += "p"
    return sentence, picked

def Q(lmList, hand, sentence, picked):
    if lmList[hand][8][0] < lmList[hand][6][0]:
        for point in range(1, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][0] > lmList[hand][fingerPIP[point]][0]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] > lmList[hand][9][1] and lmList[hand][4][0] < lmList[hand][5][0] and lmList[hand][5][0] > lmList[hand][18][0]:
            picked = True
            sentence += "q"
    return sentence, picked

def R(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if point <= 1 and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerMCP[point]][1] and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerPIP[point]][1]:
            pass
        elif point > 1 and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1] and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0] \
            and lmList[hand][12][0] < lmList[hand][13][0]:
        picked = True
        sentence += "r"
    return sentence, picked

def S(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] < lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][3][0] and lmList[hand][5][0]\
            < lmList[hand][18][0] and lmList[hand][7][1] > lmList[hand][10][1]:
        picked = True
        sentence += "s"
    return sentence, picked

def T(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] < lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][3][0] and lmList[hand][5][0]\
            < lmList[hand][18][0] and lmList[hand][7][1] < lmList[hand][10][1]:
        picked = True
        sentence += "t"
    return sentence, picked

def U(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if point <= 1 and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerMCP[point]][1] and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerPIP[point]][1]:
            pass
        elif point > 1 and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]  and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] < lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0] \
            and lmList[hand][12][0] < lmList[hand][13][0]:
        picked = True
        sentence += "u"
    return sentence, picked

def V(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if point <= 1 and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerMCP[point]][1] and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerPIP[point]][1]:
            pass
        elif point > 1 and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]  and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0]\
            and lmList[hand][12][0] > lmList[hand][13][0] and lmList[hand][8][0] < lmList[hand][5][0]:
        picked = True
        sentence += "v"
    return sentence, picked

def W(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if point <= 2 and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerMCP[point]][1]:
            pass
        elif point > 2 and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]:
            pass
        else:
            return sentence, picked
    if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0]\
            and lmList[hand][16][0] > lmList[hand][13][0] and lmList[hand][8][0] < lmList[hand][5][0]:
        picked = True
        sentence += "w"
    return sentence, picked

def X(lmList, hand, sentence, picked):
    for point in range(len(fingerMCP)):
        if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
            if point > 0 and lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerMCP[point]][1]:
                pass
            elif point == 0 and lmList[hand][fingerTIP[point]][1] < lmList[hand][fingerMCP[point]][1]:
                pass
            else:
                return sentence, picked
        else:
            return sentence, picked
    if lmList[hand][4][1] > lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][3][0] and lmList[hand][5][0]\
            < lmList[hand][18][0] and lmList[hand][8][1] < lmList[hand][9][1]:
        picked = True
        sentence += "x"
    return sentence, picked

def Y(lmList, hand, sentence, picked):
    if lmList[hand][20][1] < lmList[hand][18][1]:
        for point in range(len(fingerMCP) - 1):
            if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] < lmList[hand][5][1] and lmList[hand][4][0] < lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0]:
                picked = True
                sentence += "y"

    return sentence, picked

def Z(lmList, hand, sentence, picked):
    if lmList[hand][8][1] < lmList[hand][6][1]:
        for point in range(1, len(fingerMCP)):
            if lmList[hand][fingerTIP[point]][1] > lmList[hand][fingerPIP[point]][1]:
                pass
            else:
                return sentence, picked
        if lmList[hand][4][1] < lmList[hand][5][1] and lmList[hand][4][0] > lmList[hand][5][0] and lmList[hand][5][0] < lmList[hand][18][0]:
            picked = True
            sentence += "z"
    return sentence, picked

engine = pyttsx3.init()
engine.setProperty("rate", 120)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

fingerMCP = [5,9,13,17]
fingerPIP = [6,10,14,18]
fingerDIP = [7,11,15,19]
fingerTIP = [8,12,16,20]

uprightHandLetters = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
controls = [pick, space, play]

sentence = ""
picked = True
chosen = False
spoken = False
chosenBack = False

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.75)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


while True:
    singleList = {}
    lmList = {}
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                singleList[id] = cx, cy
                #if id ==0:
                cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
            lmList[results.multi_hand_landmarks.index(handLms)] = singleList
            singleList={}
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    h,w,c = img.shape

    w = int(w/2)
    start_point = (w , 0)
    end_point = (w , h)

    #setup fps and display
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)

    img = cv2.line(img, start_point, end_point, (0,0,0), 9)
    img = cv2.line(img, (0, h - 25 ),(w *2, h-25), (255, 255, 255), 50)
    cv2.putText(img, sentence[-15:], (10, h - 10), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    handAmount = 0

    for hand in lmList: #runs for both hands
        if not picked:
            if lmList[hand][0][0] > w: #checks if the hand is on the right side of the screen
                for letter in uprightHandLetters: #calls each letter function to check which letter is being displayed
                    sentence, picked = letter(lmList,hand, sentence, picked)
        elif picked and lmList[hand][0][0] < w and not chosen: #checks if a letter has been picked
                for option in controls: #checks to see if the user is trying to call on any controls (play,backspace, clear, select)
                    sentence, chosen = option(lmList, hand, sentence, chosen)
                if not chosenBack:
                    sentence, chosenBack = backspace(lmList,hand,sentence, chosenBack)
                if chosenBack:
                    sentence,chosenBack = chooseBack(lmList,hand,sentence, chosenBack)

        elif chosen and picked and lmList[hand][0][0] < w:
            sentence, picked, chosen = choose(lmList, hand, sentence, picked, choose)
