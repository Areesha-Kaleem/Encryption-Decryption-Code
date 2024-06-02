import random
def encrypt():
    key_dict_e = {"A": "Q", "B": "W", "C": "P", "D": "R", "E": "T", "F": "Y", "G": "U", "H": "E", "I": "O", "J": "I", "K": "A", "L": "S", "M": "D", "N": "F", "O": "G", "P": "V", "Q": "J", "R": "K", "S": "L", "T": "Z", "U": "X", "V": "C", "W": "H", "X": "B", "Y": "N", "Z": "M", "a": "q", "b": "w", "c": "p", "d": "r", "e": "t", "f": "y", "g": "u", "h": "e", "i": "o", "j": "i", "k": "a", "l": "s", "m": "d", "n": "f", "o": "g", "p": "v", "q": "j", "r": "k", "s": "l", "t": "z", "u": "x", "v": "c", "w": "h", "x": "b", "y": "n", "z": "m", ",": "-", ".": "+", "!": "=", "'": "^"}
    fb_strings = ['kl$', 'r?a', 'm%p', 'n|b', 'u{q', 'g~d', 'c`a', 's*b', 'v!a', 'y<q']
    paragraph = input("Enter a paragraph: ")
    list_of_words = paragraph.split()
    encrypted = []
    x = ""

    for alpha in list_of_words:
        alpha = list(alpha)
        for l in range(len(alpha)):
            if alpha[l] in key_dict_e:
                alpha[l] = key_dict_e[alpha[l]]
        for j in alpha:
            x += j
        f = random.choice(fb_strings)
        b = random.choice(fb_strings)
        alpha = f + x + b
        encrypted.append(alpha)
        x = ""

    for i in encrypted:
        print(i[::-1], " ", end="")


def decrypt():
    info = input("Enter message to decrypt:")
    key_dict_d = {"Q": "A", "W": "B", "P": "C", "R": "D", "T": "E", "Y": "F", "U": "G", "E": "H", "O": "I", "I": "J", "A": "K", "S": "L", "D": "M", "F": "N", "G": "O", "V": "P", "J": "Q", "K": "R", "L": "S", "Z": "T", "X": "U", "C": "V", "H": "W", "B": "X", "N": "Y", "M": "Z","q": "a", "w": "b", "p": "c", "r": "d", "t": "e", "y": "f", "u": "g", "e": "h", "o": "i", "i": "j", "a": "k", "s": "l", "d": "m", "f": "n", "g": "o", "v": "p", "j": "q", "k": "r", "l": "s", "z": "t", "x": "u", "c": "v", "h": "w", "b": "x", "n": "y", "m": "z", "-": ",", "+": ".", "=": "!", "^": "'"}
    to_decrypt = info.split()
    decrypted = []
    y = ""

    for h in to_decrypt:
        original_word = h[3:-3]
        original_word = list(original_word)
        for k in range(len(original_word)):
            if original_word[k] in key_dict_d:
                original_word[k] = key_dict_d[original_word[k]]
        for m in original_word:
            y += m
        decrypted.append(y)
        y = ""

    for n in decrypted:
        print(n[::-1], " ", end="")


print("Encryption / Decryption tool")
Ask = input("Do you want to encrypt any message:")
if Ask == "yes":
    encrypt()
else:
    ask = input("Do you want to decrypt any message")
    if ask == "yes":
        decrypt()
    else:
        print("Call me whenever you need to!")



'''It was a beautiful love story, but Alas! the ending was heart breaking.'''