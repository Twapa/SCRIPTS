import os

#Ciphertext file path
pathname = os.path.join("data/text/",'ciphertext.txt')

#Reading ciphertext file
with open(pathname,'r') as ciphered:
    encrypted_message = ciphered.read()


#List of valid symbols
VALID_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Key acquisition- A more complex solution would involve comparing results of frequency analysis
#key = 5
key = VALID_LETTERS.find('F') - VALID_LETTERS.find('A')

#Store the decrypted message
translated_message = ''

#Loop through each symbol in message
for symbol in encrypted_message.upper():
    if symbol in VALID_LETTERS:
        symbolIndex = VALID_LETTERS.find(symbol)
        translatedIndex = symbolIndex - key

        #Handle wraparound due to find()'s logic
        if translatedIndex < 0:
            translatedIndex += len(VALID_LETTERS)

        #Append decrypted symbol to translated message
        translated_message += VALID_LETTERS[translatedIndex]

    else:
        translated_message += symbol

#Writing deciphered message to file
pathname_plain = os.path.join(os.path.dirname(pathname),'plaintext.txt')
if not os.path.exists(pathname_plain):
    with open(pathname_plain,'w') as freq:
        freq.write(translated_message)


