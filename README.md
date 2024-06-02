# Encryption-Decryption-Code
This code is an encryption and decryption tool using a substitution cipher. It encrypts a paragraph by replacing each letter with a predefined character, adding random padding strings, and reversing the result. For decryption, it removes the padding, reverses the string, and substitutes characters back to the original.

This code is an encryption and decryption tool using a simple substitution cipher with additional random padding strings.

Encryption Process:
Substitution Dictionary: A dictionary (key_dict_e) maps each letter to a different letter or symbol.
User Input: The user is prompted to enter a paragraph.
Word Split: The paragraph is split into individual words.
Character Substitution: Each character in the word is replaced with its corresponding character from the dictionary.
Padding: Random padding strings from fb_strings are added before and after each word.
Reverse and Display: Each padded and encrypted word is reversed and displayed.
Decryption Process:
Substitution Dictionary: A dictionary (key_dict_d) maps each encrypted character back to the original character.
User Input: The user is prompted to enter an encrypted message.
Word Split: The encrypted message is split into individual words.
Remove Padding: The first three and last three characters (padding) are removed from each word.
Character Substitution: Each character in the word is replaced with its corresponding character from the dictionary.
Reverse and Display: Each decrypted word is reversed and displayed.
User Interaction:
The user chooses whether to encrypt or decrypt a message.
Based on the choice, the respective function (encrypt or decrypt) is called.
Example:
Encrypting "Hello!" might result in something like qwsyeviwdqa.
Decrypting qwsyeviwdqa will return to "Hello!".
