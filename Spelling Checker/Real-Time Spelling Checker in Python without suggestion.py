import re  # import regular expression library
import tkinter as tk  # import GUI
from tkinter.scrolledtext import ScrolledText

import nltk
from nltk.corpus import words

nltk.download("words")  # to check the word is valid or not


class SpellingChecker:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.text = ScrolledText(self.root, font=("Arial", 14))
        # check when there is a space
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()  # Add to the GUI

        self.old_spaces = 0  # By default is 0 white spaces

        self.root.mainloop()  # Get GUI running

    def check(self, event):
        # 1.0 is the first character. 1.1 is the second character. End = Give full content of the text box
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")

        if space_count != self.old_spaces:
            self.old_spaces = space_count  # update the old_spaces to space_count

            # whenever we check, we remove all-in-text
            for tag in self.text.tag_names():
                self.text.tag_delete(tag)

            for word in content.split(" "):
                # sub: subtitute, r: regex, ^: exclude
                if re.sub(r"[^\w]", "", word.lower()) not in words.words():
                    position = content.find(word)
                    self.text.tag_add(
                        word, f"1.{position}", f"1.{position + len(word)}")
                    self.text.tag_config(word, foreground="red")


SpellingChecker()
