import os
import matplotlib.pyplot as plt
path = 'E:/ACADEMICS/Assignments/Year III/NET311/data/text/ciphertext.txt'

encrypted_message = " "
stored_letters = {}
total_charcount = 0

def plotgraph(setdictionary):
    plt.bar(range(len(setdictionary)), list(setdictionary.values()), align='center')
    plt.xticks(range(len(setdictionary)), list(setdictionary.keys()))
    plt.grid(zorder=5)
    plt.show()
    
   

#Write contents of ciphertext to variable
with open(path,'r') as ciphered:
    encrypted_message = ciphered.read().upper()
    
#Populate frequency table
for char in encrypted_message:
    if char not in stored_letters:
        stored_letters[char] = 1
    else:
        stored_letters[char] += 1

for char in stored_letters:
    total_charcount += stored_letters[char]

for char in stored_letters:
    stored_letters[char] = (stored_letters[char] / total_charcount) * 100

#Writing output to text file
if not os.path.exists(os.path.abspath(path) + 'frequency_report.txt'):
    with open('frequency_report.txt','w') as freq:
        #Print frequency chart
        for char in sorted(stored_letters.keys()):
            freq_report = 'This character {} has {:.2f}% frequency \n'.format(char,stored_letters[char]) 
            freq.write(freq_report)

plotgraph(stored_letters)

#Intention is to make this script an export module for returning elements in the stored_letters dictionary
#class Result():


#if __name__ == '__main__':


