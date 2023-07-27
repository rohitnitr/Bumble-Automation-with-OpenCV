# Bumble Face - Smile Detection and Auto Swiping Bot

Bumble Face is a Python application that combines smile detection and an auto-swiping bot to automate the swiping process on the Bumble dating app. The application uses facial landmark detection to determine whether the user is smiling or not, and based on the result, it automatically likes or passes on profiles. The bot also supports superswiping when it detects a specific eye blink signal.

## How It Works

The application consists of three main components:
1. **Smile Detection (smile.py):** This module utilizes the dlib library to detect facial landmarks in images captured from a webcam. It calculates the ratio of lips width to jaw width, and if the ratio exceeds a threshold, it determines that the user is smiling. The result is saved in a "smile_signal.txt" file.

2. **Auto Swiping Bot (bot.py):** This component utilizes the Selenium library to control a Chrome web browser and interact with the Bumble website. The bot logs in to the Bumble app, captures webcam images, and performs actions based on the signals from the smile detection and eye blink detection modules. It supports liking profiles when a smile is detected and superswiping when a specific eye blink signal ("Right Eye Blinked") is received.

3. **Main Script (main.py):** The main script orchestrates the execution of smile detection and the auto-swiping bot in parallel using the `multiprocessing` module. It runs "smile.py" and "bot.py" as separate processes.

## Requirements

To run the Bumble Face application, ensure you have the following installed:

- Python 3.x
- Chrome web browser
- ChromeDriver executable (compatible with your Chrome version)

## How to Use

1. Clone this repository to your local machine.

2. Download the shape predictor model file ("shape_predictor_68_face_landmarks.dat") and place it in the same directory as "smile.py" and "bot.py". You can download the model from [here](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat).

3. Install the required Python dependencies by running the following command in your terminal or command prompt:
   ```
   pip install -r requirements.txt
   ```

4. Ensure that your ChromeDriver executable path is correctly set in "bot.py" under the `chromedriver_path` variable.

5. Run the "main.py" script to start the application. The script will run "smile.py" and "bot.py" in parallel.

6. Before running the bot, log in to the Bumble app on the Chrome browser that the bot will control. The bot will automatically proceed after successful login.

7. The bot will detect smiles in the webcam images and automatically like profiles when a smile is detected. It will also superswipe when the eye blink signal ("Right Eye Blinked") is received.

8. The bot will continue swiping until you manually interrupt the execution by pressing Ctrl+C.

## Important Notes

- The smile detection module relies on accurate facial landmark detection. Make sure your webcam is correctly positioned to capture your face properly.

- The application is intended for educational and demonstrative purposes only. Using automated bots on dating apps may violate the app's terms of service and lead to account suspension.

- The eye blink signal ("Right Eye Blinked") is currently set to trigger superswiping. Adjust the signal detection logic in "smile.py" and "bot.py" as needed for your specific use case.

- Smile detection accuracy can vary based on lighting conditions and facial expressions. Consider fine-tuning the smile detection threshold in "smile.py" to suit your preferences.

## Contributions

Contributions to improve the application are welcome. If you find any issues or have suggestions, feel free to open an issue or create a pull request.

## Disclaimer

This project is provided as-is without any warranties. The developer is not responsible for any misuse or consequences caused by using this application.

Happy dating and coding! 😄🤖