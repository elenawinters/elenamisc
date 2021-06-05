from random_word import RandomWords
import pyperclip
import keyboard
import sys


# This is to help with guessing the word on Kyliebitkin's Discord
class EasyGuessTheWordHack:
    def __init__(self):
        self.invalids = set('-,_ ')
        self.prefix = '!'

    def win(self) -> str:
        while True:
            word = RandomWords().get_random_word()
            if self.validate(word):
                return self.prefix + str(word).lower()

    def is_english(self, word: str) -> bool:
        try:
            word.encode('utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        return True

    def invalid_characters(self, word: str) -> bool:
        if any((c in self.invalids) for c in word):
            return True
        return False

    def validate(self, word: str) -> bool:
        if word is None:
            sys.exit('Please restart the script. The connection is not valid.')
        if word.islower() and not self.invalid_characters(word) and self.is_english(word):
            return True


if __name__ == '__main__':
    hack = EasyGuessTheWordHack()
    while True:
        command = hack.win()
        pyperclip.copy(command)
        print(f"The following word is now on the clipboard: \"{command}\"")
        keyboard.wait('ctrl+v')  # wait for enter
