
def palabra(signo="",numero="3"):
    word = str(input("Inserte palabra\n"))
    salto = int(signo + numero)
    new_word = ""
    for i in word:
        if i.isupper() == True:
            new_word += chr((((ord(i.lower) + salto) - 97) % 26) + 97).upper()
        else:
            new_word += chr((((ord(i) + salto) - 97) % 26) + 97)
    print(new_word)
palabra()
palabra(signo="-")