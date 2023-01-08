from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://morsecode.world/international/translator.html"
# create object of class Options and add add_experimental_option for keep the page open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


is_on = True

# enter 'exit' for stop program
while is_on:
    # ask the user what he wants to do
    chose = input("Enter 'm' for encrypt text in Morse, and 'e' for decrypt Morse: ").lower()
    if chose == "exit":
        is_on = False
    else:
        # ask the user to type text
        text_for_translate = input("Enter your text: ")

        if chose == 'm':
            # create webdriver object
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
            # GET method more open page browser
            driver.get(URL)
            # finding element for input text
            input_text = driver.find_element(By.ID, "input")
            # input text
            input_text.send_keys(f"{text_for_translate}")
            # click enter button
            input_text.send_keys(Keys.ENTER)
            # time for execute the request
            time.sleep(1)
            # finding translated text in Morse
            output_text = driver.find_element(By.ID, "output").text
            print(output_text)
            # close page
            driver.quit()
        elif chose == 'e':
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
            driver.get(URL)
            input_text = driver.find_element(By.ID, "input")
            input_text.send_keys(f"{text_for_translate}")
            input_text.send_keys(Keys.ENTER)
            time.sleep(1)
            output_text = driver.find_element(By.ID, "output").text.lower()
            print(output_text)
            driver.quit()
        else:
            print("Please, enter correct data! ")
