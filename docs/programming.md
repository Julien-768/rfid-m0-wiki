# Programming procedure

## Prerequisites

1. Download [Visual Studio Code](https://code.visualstudio.com/download)
2. Install [PlatfomIO](https://docs.platformio.org/en/stable/integration/ide/vscode.html#installation)
3. Clone the [rfid_m0.code](vscode://vscode.git/clone?url=https%3A%2F%2Fgitlab.in2p3.fr%2Frfid_m0%2Frfid_m0.code.git) repository
4. Get a [USB Micro B cable](https://en.wikipedia.org/wiki/USB_hardware#/media/File:MicroB_USB_Plug.jpg)

## Programming

1. Open the code folder in Visual Studio Code. Give some time for the dependencies to be automatically downloaded once the code repository is cloned if it is a first time use.
2. Connect the Feather M0 to the computer using a USB cable
3. Click on [PlatformIO: Clean](https://docs.platformio.org/en/stable/integration/ide/vscode.html#platformio-toolbar) or Clean via the [PIO Menu](https://docs.platformio.org/en/stable/_images/platformio-ide-vscode-task-explorer-refresh.png). This will refresh the compilation date to update the RTC if needed.
4. Click on 'PlatformIO: Upload' and then open the 'PlatformIO: Serial Monitor' or 'Upload and Monitor' via the [PIO Menu](https://docs.platformio.org/en/stable/_images/platformio-ide-vscode-task-explorer-refresh.png) to view the initialisation messages
