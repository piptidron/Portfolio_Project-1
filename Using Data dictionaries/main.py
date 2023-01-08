english_to_morse = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
            'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-',
            'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-',
            'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--',
            'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-',' ': '/'}

# Create new dict using dictionary comprehension with new pair key:value ("morse_code":"symbol")
morse_to_english = {v:k for k,v in english_to_morse.items()}

# Create function for translate text to Morse code
def encrypt():
    text = input("Enter your text: ")
    # Create translate using dictionary comprehension
    # Using .lower() for replace capital letters
    # Using ' '.join() for separate Morse characters and words between each other
    encrypt_text = ' '.join(english_to_morse[c] for c in text.lower())
    print(encrypt_text)

def decrypt():
    text = input("Enter your morse code: ")
    # Create translate using dictionary comprehension
    # Using ''.join() for compare symbols between each other
    # Using .split() fot separate Morse characters and words each other
    decrypt_text = "".join(morse_to_english[c] for c in text.split())
    print(decrypt_text)

is_on = True

while is_on:
    choice = input("Enter 'm' for encrypt to Morse or 'e' for decrypt to Text('exit' for stop):\n").lower()
    if choice != 'exit':
        # catch KeyError.
        # It occurs when use symbols not from the data dictionary 'english_to_morse' or 'morse_to_english'
        try:
            if choice == 'm':
                encrypt()
            elif choice == 'e':
                decrypt()
            else:
                print("Invalid data entered.")
        except KeyError:
            print("You entered the invalid symbol.Try again.")
