# Bumble Automation with OpenCV

Bumble Automation with OpenCV is a Python project that combines facial recognition using OpenCV and automation with the Bumble dating app. The application uses OpenCV's smile detection to determine whether the user is smiling or not and performs automated swiping actions on profiles accordingly.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Features](#features)
- [Contributions](#contributions)
- [Disclaimer](#disclaimer)

## Introduction

Bumble is a popular dating app where users swipe through profiles to find potential matches. This project aims to automate the swiping process by detecting smiles in real-time using OpenCV's facial recognition capabilities. When a smile is detected, the application automatically likes the profile. Additionally, the bot supports superswiping when a specific eye blink signal is received.

## Requirements

To run the Bumble Automation with OpenCV project, you need the following:

- Python 3.x
- Chrome web browser
- ChromeDriver executable (compatible with your Chrome version)

Ensure that you have the necessary dependencies installed by running the following command:

```bash
pip install -r requirements.txt
```

## How to Use

Follow these steps to use the Bumble Automation with OpenCV:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/rohitnitr/Bumble-Automation-with-OpenCV.git
```

2. Download the shape predictor model file ("shape_predictor_68_face_landmarks.dat") and place it in the same directory as "smile.py" and "bot.py". You can download the model from [here](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat).

3. Set the correct path for the ChromeDriver executable in "bot.py" under the `chromedriver_path` variable.

4. Run the main script "main.py" to start the application:

```bash
python main.py
```

5. Log in to the Bumble app on the Chrome browser controlled by the bot. The bot will automatically proceed after successful login.

6. The application will detect smiles in the webcam images and automatically like profiles when a smile is detected. It will also perform superswiping when the specific eye blink signal ("Right Eye Blinked") is received.

7. The bot will continue swiping until you manually interrupt the execution by pressing Ctrl+C.

## Features

- Smile detection using OpenCV's facial recognition.
- Automated profile swiping on Bumble based on smile detection.
- Superswiping on specific eye blink signal ("Right Eye Blinked").
- Parallel execution of smile detection and auto-swiping bot using `multiprocessing`.

## Contributions

Contributions to improve the application are welcome. If you find any issues or have suggestions, feel free to open an issue or create a pull request.

## Disclaimer

This project is intended for educational and demonstrative purposes only. The use of automated bots on dating apps may violate the app's terms of service and lead to account suspension. The developer is not responsible for any misuse or consequences caused by using this application.

Happy dating and coding! 😄🤖