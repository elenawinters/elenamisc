import pyperclip
import keyboard
import web


# This is to help with guessing the word on Kyliebitkin's Discord
class EasyGuessTheWordHack:
    def __init__(self, prefix) -> None:
        self.wordapi = 'https://random-words-api.vercel.app/word'
        self.invalids = set('-')
        self.prefix = prefix

    def win(self) -> str:
        while True:
            word = web.Client(self.wordapi).get().json()[0]['word'].lower()
            if self.validate(word):
                return self.prefix + str(word)

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
        if not self.invalid_characters(word) and self.is_english(word):
            return True


if __name__ == '__main__':
    hack = EasyGuessTheWordHack('!')
    while True:
        command = hack.win()
        pyperclip.copy(command)
        print(f"The following word is now on the clipboard: \"{command}\"")
        keyboard.wait('ctrl+v')  # wait for paste
