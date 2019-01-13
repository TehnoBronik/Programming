import winsound
import time
def Code_Morze(in_S):
    dict = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' }
    out_S = []
    for ch in in_S.upper():
        if ch == ' ':
            out_S.append(' ')
        else:
            out_S.append(dict[ch])
    return(out_S)

def Play_Morze(in_S):
    unit = 150
    dot = [220, 1*unit]
    dash = [440, 3*unit]
    for i in range(len(in_S)):
        if in_S[i] == ' ':
            time.sleep(7*unit/1000)
        else:
            for ch in in_S[i]:
                if ch == '-':
                    winsound.Beep(dash[0],dash[1])
                elif ch == '.':
                    winsound.Beep(dot[0],dot[1])
            time.sleep(3*unit/1000)

Play_Morze(Code_Morze('muha ha'))
