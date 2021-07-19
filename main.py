import random
import PySimpleGUI as sg

sg.theme('GrayGrayGray')
wordlist = [("jump", "images/1.gif")]


while True:
    font = ("Inter", 14)
    bold_font = ("impact", 22)
    rand_word_index = random.randint(0, len(wordlist) - 1)
    img = wordlist[rand_word_index][1]
    word = wordlist[rand_word_index][0]
    rand_letter_missing = random.randint(0, 2)
    word2 = list(word)
    letter = word2[rand_letter_missing]
    word2[rand_letter_missing] = " _ "
    word2out = "".join(word2)
    layout = [
        [sg.Text("Your Word Is ", font=font),
         sg.Text(word2out, font=bold_font)],
        [sg.Image(filename=img)],
        [sg.Text('Enter the missing letter', font=font), sg.InputText()],
        [sg.Button('Ok', font=font), sg.Button('Quit', font=font)]
    ]

    window = sg.Window('Word Game', layout)
    window.DEFAULT_FONT = ("inter", 100)
    events, values = window.read()
    window.close()

    fixed_letter = values[0]

    if fixed_letter == letter:
        sg.popup("You were correct, the word is " + word,
                 font=bold_font, text_color="#00ff00")
    else:
        sg.popup("you were wrong, the word is " + word,
                 font=bold_font, text_color="#ff0000")
