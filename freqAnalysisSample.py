import os
import matplotlib.pyplot as plt

pathname = os.path.join("data/text/",'sample.txt')
message = " "

stored_letters = {}
total_charcount = 0

def plotgraph(setdictionary):
    plt.bar(range(len(setdictionary)), list(setdictionary.values()), align='center')
    plt.xticks(range(len(setdictionary)), list(setdictionary.keys()))
    plt.grid(zorder=3)
    plt.show()

#Write contents of ciphertext to variable
with open(pathname,'r',encoding='utf-8') as ciphered:
    message = ciphered.read().upper()
    
#Populate frequency table
for char in message:
    if char not in stored_letters:
        stored_letters[char] = 1
    else:
        stored_letters[char] += 1

#Taking total character count
for char in stored_letters:
    total_charcount += stored_letters[char]

#Finding and assigning percentage for each character
for char in stored_letters:
    stored_letters[char] = (stored_letters[char] / total_charcount) * 100

#Writing output to text file
if not os.path.exists(os.path.abspath(pathname) + 'frequency_report2.txt'):
    with open('frequency_report2.txt','w') as freq:
        #Print frequency chart
        for char in sorted(stored_letters.keys()):
            freq_report = 'This character {} has {:.2f}% frequency \n'.format(char,stored_letters[char]) 
            freq.write(freq_report)


plotgraph(stored_letters)
