
a = 0
print(a)


abc = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    
    
}

def morse(aw):
    print(aw)
    morse_string=""
    for el in aw:
        #print(el)
        if el in abc:
            mletter=abc[el]
            morse_string+="  "+mletter
        #print(mletter)
    print(morse_string)


morse(input("Ввидите текст:"))


b = 100
print(b)