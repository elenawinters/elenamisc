import logging
import string
import sys

log = logging.getLogger(__name__)
_level = logging.DEBUG
log.setLevel(_level)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(_level)
log.addHandler(handler)


indicators = tuple(range(0x1F1E6, 0x1F1FF + 1))


class FancyTexts_Discord:
    def __init__(self, text: str) -> None:
        self.text = text.lower()

    def conv_indicator(self) -> str:
        # log.debug(indicators)
        # log.debug(len(indicators))
        for n in range(len(string.ascii_lowercase)):
            # log.debug(string.ascii_lowercase[n])
            # log.debug(indicators[n])

            self.text = self.text.replace(string.ascii_lowercase[n], f'\\{chr(indicators[n])}')
        #     self.new = self.text.replace(letter, f'\\:regional_indicator_{letter}:')
        return self.text


# TODO: Move this to generators.py
if __name__ == '__main__':
    if len(sys.argv) > 1:
        log.info(f'{FancyTexts_Discord(sys.argv[1]).conv_indicator()}\n')
    else:
        while True:
            text = input('\nEnter text to convert: ')
            log.info(f'{FancyTexts_Discord(text).conv_indicator()}\n')
