from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_row = None


def generate_new_word():
    global random_row
    random_row = random.choice(words_to_learn)
    canvas.itemconfig(card, image=card_font_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_row[0], fill="black")
    screen.after(4000, flip_card)


def flip_card():
    card_back_image_path = "images/card_back.png"
    card_back_image = PhotoImage(file=card_back_image_path)
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_row[1], fill="white")

def right_click():
    if random_row in words_to_learn:
        words_to_learn.remove(random_row)
    generate_new_word()


screen = Tk()
screen.title("Flashy")
screen.configure(padx=50, pady=50, background=BACKGROUND_COLOR)

wrong_image_path = "images/wrong.png"
wrong_image = PhotoImage(file=wrong_image_path)
wrong_button = Button(image=wrong_image, command=generate_new_word, highlightthickness=0)
wrong_button.grid(column=1, row=1)

right_image_path = "images/right.png"
right_image = PhotoImage(file=right_image_path)
right_button = Button(image=right_image, highlightthickness=0, command=right_click)
right_button.grid(row=1, column=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_font_image_path = "images/card_front.png"
card_font_image = PhotoImage(file=card_font_image_path)
card = canvas.create_image(400, 263, image=card_font_image)
word_text = canvas.create_text(400, 263, text="Click button to start game", font=('Times', 50))
language_text = canvas.create_text(400, 100, text="", font=('Times', 30))
canvas.grid(row=0, column=0, columnspan=2)
words_path = 'data/french_words.csv'
words = pandas.read_csv(words_path)

try:
    words_to_learn=pandas.read_csv('data/words_to_learn.csv')
except:
    words.to_csv('data/words_to_learn.csv', index=False)
    words_to_learn = pandas.read_csv('data/words_to_learn.csv')
finally:
    words_to_learn=words_to_learn.values.tolist()

screen.mainloop()
