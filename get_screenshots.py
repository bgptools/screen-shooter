import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Options for FireFox to enable Headless mode
firefox_options = Options()
firefox_options.add_argument("--headless")

# Define and set the user agent to override blocks based on user-agents
user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
firefox_options.set_preference("general.useragent.override", user_agent)


def get_screenshot(u_are_L):
    try:
        # Initialize webdriver for Firefox
        driver = webdriver.Firefox(options=firefox_options)

        for file in os.listdir('./extensions'):
            if file.endswith('.xpi'):
                driver.install_addon(f'./extensions/{file}', temporary=True)

        # Set the screenshot size (this is 4:3 as far as i know, can change it to whatever if you want to make it 16:9 or whatever in the future)
        driver.set_window_size(1024, 853) # 768 + 85 because unknown bug

        # Honestly, I really do not know what this does. All I know is that the script needs it.
        # According to VSCode:
        # Sets a sticky timeout to implicitly wait for an element to be found, or a command to complete. This method only needs to be called one time per session.
        # yk, after reading VSCode's definition, I think it's to wait for JS to load
        driver.implicitly_wait(10)

        # Make initial request to the webpage
        driver.get(u_are_L)

        # Wait for 5 seconds so that all JS can process and elements can properly load in
        time.sleep(5)

        # Take the screenshot
        driver.save_screenshot("temp_screenshot.png")

        done = True
    # Catch errors
    except Exception as error:
        done = False
    # Quit the driver (out of try/except due to memory leaks & instance leaks)
    driver.quit()
    if done == True:
        #Let us know that the screenshot was successfully gotten (W)
        return True, 'Success!'
    else:
        # Return a list of [False, (whatever the error is)]
        return False, error