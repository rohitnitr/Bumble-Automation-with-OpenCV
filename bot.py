from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

# Specify the path to chromedriver executable
chromedriver_path = "/Users/rohitpoddar/Documents/Artificial Intelligence Projetcs/Bumble-face/chromedriver"

# Configure ChromeOptions
chrome_options = Options()
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (necessary on some systems)

# Set the path to the chromedriver executable
chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')

def click_like_button():
    try:
        # Locate and click the like button using XPath
        like_button = driver.find_element("xpath", "//span[@data-qa-role='icon' and @data-qa-icon-name='floating-action-yes']")
        like_button.click()

        # Display "Liked the profile" message on the browser using JavaScript
        message = "Liked the profile!"
        driver.execute_script(f"alert('{message}');")

        # Wait for 1 seconds for the alert to be displayed and then dismissed
        time.sleep(1)

        # Switch to the alert and accept/dismiss it (this will close the alert)
        driver.switch_to.alert.accept()

        time.sleep(2)
        scrolling()

    except Exception as e:
        print(f"Error: Unable to locate or click the like button. {e}")

def click_pass_button():
    try:
        # Locate and click the "Pass" button using XPath
        pass_button = driver.find_element("xpath", "//span[@data-qa-role='icon' and @data-qa-icon-name='floating-action-no']")
        pass_button.click()

        # Display "Passed the profile" message on the browser using JavaScript
        message = "Passed the profile!"
        driver.execute_script(f"alert('{message}');")

        # Wait for 1 seconds for the alert to be displayed and then dismissed
        time.sleep(1)

        # Switch to the alert and accept/dismiss it (this will close the alert)
        driver.switch_to.alert.accept()

        time.sleep(2)

        scrolling()

    except Exception as e:
        print(f"Error: Unable to locate or click the Pass button. {e}")

def click_superswipe_button():
    try:
        # Locate and click the like button using XPath
        superswipe_button = driver.find_element("xpath", "//span[@data-qa-role='icon' and @data-qa-icon-name='floating-action-superswipe']")
        superswipe_button.click()
        os.remove("eye_signal.txt")


        # Display "Liked the profile" message on the browser using JavaScript
        message = "Superswiped the profile!"
        driver.execute_script(f"alert('{message}');")

        # Wait for 1 seconds for the alert to be displayed and then dismissed
        time.sleep(1)

        # Switch to the alert and accept/dismiss it (this will close the alert)
        driver.switch_to.alert.accept()

        time.sleep(2)

        scrolling()

    except Exception as e:
        print(f"Error: Unable to locate or click the like button. {e}")

# Define the scrolling function
def scrolling():

    if os.path.exists("smile_signal.txt"):
        os.remove("smile_signal.txt")
    if os.path.exists("eye_signal.txt"):
        os.remove("eye_signal.txt")


    # Scroll down using down arrow key multiple times (4 times in this example)
    actions = ActionChains(driver)
    for _ in range(4):
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(1)  # Adjust the duration to control the scroll speed (0.5 seconds in this example)

    # Scroll up using up arrow key multiple times (4 times in this example)
    actions = ActionChains(driver)
    for _ in range(4):
        actions.send_keys(Keys.ARROW_UP)
        actions.perform()
        time.sleep(1)  # Adjust the duration to control the scroll speed (0.5 seconds in this example)
            # Check if the smile signal file exists
    if os.path.exists("smile_signal.txt"):
        with open("smile_signal.txt", "r") as f:
            signal = f.read().strip()
            if signal == "Smiling":
                click_like_button()
    # Check if the eye signal file exists
    elif os.path.exists("eye_signal.txt"):
        with open("eye_signal.txt", "r") as f:
            signal = f.read().strip()
            if signal == "Right Eye Blinked":
                click_superswipe_button()
    elif not os.path.exists("smile_signal.txt" or "eye_signal.txt"):
        click_pass_button()

                

if __name__ == "__main__":
    try:
        # Create a new Chrome browser session
        driver = webdriver.Chrome(options=chrome_options)

        # Open the Bumble website
        driver.get("https://bumble.com/get-started")

        # Wait for the user to manually log in (ensure you are logged in before proceeding)
        # No need to use input() anymore, just wait for the successful login URL to be detected
        while driver.current_url != "https://bumble.com/app":
            time.sleep(1)

        # Display "you are logged in" alert for 2 seconds after successful login
        script = 'alert("You are logged in");'
        driver.execute_script(script)
        time.sleep(2)  # Wait for 2 seconds for the alert to be displayed and then dismissed

        # Accept the alert
        driver.switch_to.alert.accept()

        # Wait for an additional 5 seconds after displaying the alert
        time.sleep(5)


        # Call the scrolling function
        scrolling()






    except KeyboardInterrupt:
        print("User interrupted the execution.")
    except Exception as e:
        print(f"Error occurred: {e}")






        
    finally:
        # Close the browser
        driver.quit()
