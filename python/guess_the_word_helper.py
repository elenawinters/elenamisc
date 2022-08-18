import pyperclip
import keyboard
import web


# This is to help with guessing the word on Kyliebitkin's Discord
# This challenge ended, I don't remember what the word was, but I didn't get it
class EasyGuessTheWordHack:
    def __init__(self) -> None:
        self.wordapi = 'https://random-words-api.vercel.app/word'
        self.invalids = set('-')

    def win(self) -> str:
        while True:
            word = web.Client(self.wordapi).get().json()[0]
            word = [word['word'].lower(), word['definition']]
            if self.validate(word[0]):
                return word

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


class GuessTheWordLoop(EasyGuessTheWordHack):
    def __init__(self, speak=False) -> None:
        super().__init__()

        self.speak = speak
        self.prefix = '!'

        while True:
            self.process()

    def process(self):
        word = self.win()
        self.speak_up(word)
        command = self.prefix + word[0]
        pyperclip.copy(command)
        print(f"The following word is now on the clipboard: \"{command}\"")
        keyboard.wait('ctrl+v')  # wait for paste

    def speak_up(self, l_word):
        if not self.speak: return


if __name__ == '__main__':
    GuessTheWordLoop(True)
