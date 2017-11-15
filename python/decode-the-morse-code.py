# https://www.codewars.com/kata/decode-the-morse-code

def decodeMorse(morseCode):
    words = morseCode.lstrip(' ').split('   ')
    decoded_final = []
    for word in words:
        letters = word.split()
        decoded_word = ''
        for letter in letters:
            decoded_word += MORSE_CODE[letter]
        decoded_final.append(decoded_word)    
    return ' '.join(decoded_final)