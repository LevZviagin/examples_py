abc_morse_to_alpha = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z" 
}

def abc(morse_str):
   # print(morse_str)
    bnm_list = morse_str.split()
    for el in bnm_list:
        print(el)
        my_letter=abc_morse_to_alpha[el]
        print(my_letter)
        
    
abc(input())

 
 
 
 
 
 
 
 
 
 
 
abc = {
    "forest" : "лес",
    "or": "или"
} 
 
 
 
    