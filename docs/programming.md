# Programming procedure

## Prerequisites

1. A main board assembled according to the [instructions](Electronic_assembling.md)
2. Download [Visual Studio Code](https://code.visualstudio.com/download)
3. Install [PlatfomIO](https://docs.platformio.org/en/stable/integration/ide/vscode.html#installation)
4. Clone the [rfid.m0.code](vscode://vscode.git/clone?url=https%3A%2F%2Fgitlab.in2p3.fr%2Frfid.m0%2Frfid.m0.code.git) repository
5. Get a [USB Micro B cable](https://en.wikipedia.org/wiki/USB_hardware#/media/File:MicroB_USB_Plug.jpg)
6. Set your computer in UTC time zone

## Programming

1. Open the code folder in Visual Studio Code. Give some time for the dependencies to be automatically downloaded once the code repository is cloned if it is a first time use.
2. Check and modify if necessary the values of **BATTERY_MIN_VOLTAGE** and **POWER_BOARD_BATT_RATIO** parameters at the beginning of the code (main.cpp file)
3. Connect the Feather M0 to the computer using a USB cable
4. Click on [PlatformIO: Clean](https://docs.platformio.org/en/stable/integration/ide/vscode.html#platformio-toolbar) or Clean via the [PIO Menu](https://docs.platformio.org/en/stable/_images/platformio-ide-vscode-task-explorer-refresh.png). This will refresh the compilation date to update the RTC if needed.
5. Click on 'PlatformIO: Upload' and then open the 'PlatformIO: Serial Monitor' or 'Upload and Monitor' via the [PIO Menu](https://docs.platformio.org/en/stable/_images/platformio-ide-vscode-task-explorer-refresh.png) to view the initialisation messages
