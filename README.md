# Sign Language Interpreter

This project utilizes Open-CV and MediaPipe to translate alphabetical sign language to text on a screen with Text-To-Speech playback using pytts. 


## Functionality
When running the [`signlanguageinterpreter.py`](signlanguageinterpreter.py) script, make sure that you have a webcam connected to your computer. The video feed from the camera is split into a left hand and right hand side.

### Left Hand

Your left hand is used for controls including playback, confirming letters, backspace, clear, adding a space. These controls can be found in the [`Controls`](Controls) folder. 

### Right Hand

The right hand is used for spelling letters, the symbols for these letters can be found in the [`Letters`](Letters) folder. Note that some letter symbols had to be modified from the standard symbols as MediaPipe has a hard time detecting when fingers are crossed.

## How it Works

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/RDK9m6hkhY0/0.jpg)](https://youtu.be/RDK9m6hkhY0)
