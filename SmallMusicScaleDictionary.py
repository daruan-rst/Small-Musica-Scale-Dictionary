import numpy as np
import webbrowser


notes = [("A"),("A#"),("B"),("C"),("C#"),("D"),("D#"),("E"),("F"),("F#"),("G"),("G#")]
notes2 = np.copy(notes)
notes3 = list(reversed(notes2))

print("Chose your key: \n [01]A \t [02]A#\t [03]B \t [04]C \n [05]C#\t [06]D \t [07]D#\t [08]E \n [09]F \t [10]F#\t [11]G \t [12]G# \n" )
key = int(input("key:"))
key = key-1
for i in range (12):

    if i<12-key:   
        notes[i] = notes[i+key]
    elif i == 12-key:
        notes[i] = notes2[12-key-i]
    elif i>12-key:        
        notes[i] = notes3[11-key-i]


print("\nChose a scale/mode: \n [01]Ionian \t\t [02]Dorian \t\t [03]Phrygian \t\t [04]Lydian \n [05]Mixolydian \t\t [06]Aeolian \t\t [07]Locrian \t\t [08]Pentatonic \n [09]Pentablues\t\t [10]Voodooblues \t [11]Gathimic \t\t [12]Nordestina scale  \n [13]Prometheus\t\t [14]Harmonic Minor \t [15]Locrian Natural6 \t [16]Major Augmented \n [17]Lydian Diminished \t [18]Phrygian Dominant \t [19]Aeolian Harmonic \t [20]Ultralocrian")
print(" [21]Superlocrian \t [22]Melodic Minor Ascending \t\t\t [23]Dorian Flat2 \n [24]Lydian Augmented \t [25]Acoustic \t\t [26]Major-Minor \t [27]Minor Locrian")
print(" [28]Double Harmonic \t [29]Lydian #2#6 \t [30]UltraPhrygian \t [31]Double Harmonic Menor \n [32]Asian \t\t [33]Ionian Augmented #2  [34]Locrian Double 3b7b")
scale = int(input("\nscale:"))

if scale == 1:
    print("\nYou've chosen the scale of: Modo Ionian")
    scale = [notes[0],notes[2],notes[4],notes[5],notes[7],notes[9],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 2:
    print("\nYou've chosen the scale of: Modo Dorian")
    scale = [notes[0],notes[2],notes[3],notes[5],notes[7],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 3:    
    print("\nYou've chosen the scale of: Modo Phrygian")
    scale = [notes[0],notes[1],notes[3],notes[5],notes[7],notes[8],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 4:
    print("\nYou've chosen the scale of:Modo Lydian")
    scale = [notes[0],notes[2],notes[4],notes[6],notes[7],notes[9],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)
     
elif scale == 5:
    print("\nYou've chosen the scale of:Modo Mixolydian")
    scale = [notes[0],notes[2],notes[4],notes[5],notes[7],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 6:
    print("\nYou've chosen the scale of:Modo Aeolian")
    scale = [notes[0],notes[2],notes[3],notes[5],notes[7],notes[8],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 7:
    print("\nYou've chosen the scale of:Modo Locrian")
    scale = [notes[0],notes[1],notes[3],notes[5],notes[6],notes[8],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
     
elif scale == 8:
    print("\nYou've chosen the scale of:Pentatonic")
    scale = [notes[0],notes[3],notes[5],notes[7],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
     
elif scale ==9:
    print("\nYou've chosen the scale of:Pentablues")
    scale = [notes[0],notes[3],notes[5],notes[6],notes[7],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale ==10:
    print("\nYou've chosen the scale of:Voodoo-blues")
    scale = [notes[0],notes[3],notes[5],notes[6],notes[7],notes[9]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale ==11:
    print("\nYou've chosen the scale of: Gathimic \n*The inverse of the blues scale  \n \n*type \"yes\" to read about it; Press enter to continue:")
    gathimic = input()
    if gathimic == 'YES' or 'yes' or 'Yes':
        webbrowser.open("https://ianring.com/musictheory/scales/741")
    scale = [notes[0],notes[2],notes[5],notes[6],notes[7],notes[9]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale ==12:
    print("\nYou've chosen the scale of: Nordestina \n*type \"yes\" to read about it; Press enter to continue:")
    nordestina = input()
    if nordestina == 'YES' or 'yes' or 'Yes':
        webbrowser.open("https://bit.ly/31rJC2B")
    scale = [notes[0],notes[2],notes[4],notes[6],notes[7],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale ==13:
    print("\nYou've chosen the scale of: Prometheus \n*type \"yes\" to read about it; Press enter to continue:")
    prometheus = input()
    if prometheus == 'YES' or 'yes' or 'Yes':
        webbrowser.open("https://en.wikipedia.org/wiki/Mystic_chord#Use_by_Scriabin")
        webbrowser.open("https://ianring.com/musictheory/scales/1621")
    scale = [notes[0],notes[2],notes[4],notes[6],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)


elif scale == 14:
    print("\nYou've chosen the scale of: Menor Harmônica")
    scale = [notes[0],notes[2],notes[3],notes[5],notes[7],notes[8],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 15:
    print("\nYou've chosen the scale of: Locrian Natural 6")
    scale = [notes[0],notes[1],notes[3],notes[5],notes[6],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 16:
    print("\nYou've chosen the scale of: Major Augmented")
    scale = [notes[0],notes[2],notes[4],notes[5],notes[8],notes[9],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)


elif scale == 17:
    print("\nYou've chosen the scale of: Lydian Diminuto")
    scale = [notes[0],notes[2],notes[3],notes[6],notes[7],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 18:
    print("\nYou've chosen the scale of: Phrygian Dominant")
    scale = [notes[0],notes[1],notes[4],notes[5],notes[7],notes[8],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 19:
    print("\nYou've chosen the scale of: Aeolian Harmonic")
    scale = [notes[0],notes[3],notes[4],notes[6],notes[7],notes[9],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 20:
    print("\nYou've chosen the scale of: Ultralocrian")
    scale = [notes[0],notes[1],notes[3],notes[4],notes[6],notes[8],notes[9]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 21:
    print("\nYou've chosen the scale of: Superlocrian")
    scale = [notes[0],notes[1],notes[3],notes[4],notes[6],notes[8],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 22:
    print("\nYou've chosen the scale of: Melodic Minor Ascending")
    scale = [notes[0],notes[2],notes[3],notes[5],notes[7],notes[9],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 23:
    print("\nYou've chosen the scale of: Dorian Flat 2")
    scale = [notes[0],notes[1],notes[3],notes[5],notes[7],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 24:
    print("\nYou've chosen the scale of: Lydian Augmented")
    scale = [notes[0],notes[2],notes[4],notes[6],notes[8],notes[9],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 25:
    print("\nYou've chosen the scale of: Acoustic (also known as Lydian Dominant )")
    scale = [notes[0],notes[2],notes[4],notes[6],notes[7],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 26:
    print("\nYou've chosen the scale of: Major-Minor")
    scale = [notes[0],notes[2],notes[4],notes[5],notes[7],notes[8],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 27:
    print("\nYou've chosen the scale of: Minor Locrian")
    scale = [notes[0],notes[2],notes[3],notes[5],notes[6],notes[8],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)
    
elif scale == 28:
    print("\nYou've chosen the scale of: Double Harmonic Maior")
    scale = [notes[0],notes[1],notes[4],notes[5],notes[7],notes[8],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 29:
    print("\nYou've chosen the scale of: Lydian Sharp 2 Sharp 6")
    scale = [notes[0],notes[3],notes[4],notes[6],notes[7],notes[10],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 30:
    print("\nYou've chosen the scale of: UltraPhrygian")
    scale = [notes[0],notes[1],notes[3],notes[4],notes[7],notes[8],notes[9]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 31:
    print("\nYou've chosen the scale of: Double Harmonic Minor")
    scale = [notes[0],notes[2],notes[3],notes[6],notes[7],notes[8],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 32:
    print("\nYou've chosen the scale of: Asian (Also known as Oriental)")
    scale = [notes[0],notes[1],notes[4],notes[5],notes[6],notes[9],notes[10]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 33:
    print("\nYou've chosen the scale of: Ionian Augmented #2")
    scale = [notes[0],notes[3],notes[4],notes[5],notes[8],notes[9],notes[11]]
    print("The scale in the key of", notes[0], "are \n", scale)

elif scale == 34:
    print("\nYou've chosen the scale of: Locrian dupla 3 bemol 7 bemol")
    scale = [notes[0],notes[1],notes[2],notes[5],notes[6],notes[8],notes[9]]
    print("The scale in the key of", notes[0], "are \n", scale)




    
print("\n")
FIM = input("Press anything to close")
