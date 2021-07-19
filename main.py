import random
import PySimpleGUI as sg

sg.theme('GrayGrayGray')
wordlist = ["jump", "run", "cat", "dog", "log",
            "duck", "red", "and", "is", "sat", "ran", "fun"]


def run():
    font = ("Inter", 14)
    rand_word_index = random.randint(0, len(wordlist) - 1)
    word = wordlist[rand_word_index]
    rand_letter_missing = random.randint(0, 2)
    word2 = list(word)
    letter = word2[rand_letter_missing]
    word2[rand_letter_missing] = " _ "
    word2out = "".join(word2)
    layout = [
        [sg.Text("Your Word Is " + word2out, font=font)],
        [sg.Text('Enter the missing letter', font=font), sg.InputText()],
        [sg.Button('Ok', font=font), sg.Button('Quit', font=font)]
    ]

    window = sg.Window('Word Game', layout)
    window.DEFAULT_FONT = ("inter", 100)
    events, values = window.read()
    window.close()

    fixed_letter = values[0]

    if fixed_letter == letter:
        sg.popup("You were correct, the word is " + word, font=font)
    else:
        sg.popup("you were wrong, the word is " + word, font=font)
    run()


run()
