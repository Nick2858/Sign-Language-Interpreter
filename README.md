# Sign Language Interpreter

This is a project I developped in 2022 while I was in high school. It utilizes Open-CV and MediaPipe to translate alphabetical sign language to text on a screen with Text-To-Speech playback using pyttsx3. 

## Demo

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/RDK9m6hkhY0/0.jpg)](https://youtu.be/RDK9m6hkhY0)

## How it Works
When running the [`signlanguageinterpreter.py`](signlanguageinterpreter.py) script, make sure that you have a webcam connected to your computer. The video feed from the camera is split into a left hand and right hand side.

### Left Hand

Your left hand is used for controls including playback, confirming letters, backspace, clear, adding a space. These controls can be found in the [`Controls`](Controls) folder. 

### Right Hand

The right hand is used for spelling letters, the symbols for these letters can be found in the [`Letters`](Letters) folder. Note that some letter symbols had to be modified from the standard symbols as MediaPipe has a hard time detecting when fingers are crossed.

### Determining Hand Symbols

After every frame, MediaPipe outputs a nested list where the coordinates of each "joint" in both the left and right hand are stored. For each hand sign, the position of these finger joints is unique. Therefore, by comparing the coordinates of the finger joints relative to each other, symbols can be identified.
