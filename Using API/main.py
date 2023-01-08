import requests

# endpoint for translate text to Morse
API_TO_MORSE = "https://api.funtranslations.com/translate/morse"
# endpoint for translate Morse data to text
API_TO_ENGLISH = "https://api.funtranslations.com/translate/morse2english"

# function for encrypt text
def tran_to_morse(text):
    #request POST
    response = requests.post(url=API_TO_MORSE,data={"text": f"{text}"}).json()
    morse_text = response['contents']["translated"]
    print(morse_text)

# function for decrypt Morse
def tran_to_english(text):
    #request POST
    response = requests.post(url=API_TO_ENGLISH,data={"text": f"{text}"}).json()
    english_text = response['contents']["translated"]
    print(english_text)

is_on = True

# if you want to stop program just enter 'exit'
while is_on:
    # ask the user what he wants to do
    chose = input("Enter 'm' for encrypt text in Morse, and 'e' for decrypt Morse: ").lower()
    if chose == "exit":
        is_on = False

    else:
        # ask the user to type text
        text_for_translate = input("Enter your text: ")
        try:
            if chose == 'm':
                tran_to_morse(text_for_translate)
            elif chose == 'e':
                tran_to_english(text_for_translate)
            else:
                print("Please enter correct data!")
        # catch the error related to request limits
        except KeyError:
            print("You can 60 API calls a day with distribution of 5 call an hour. Come back after an hour.")


