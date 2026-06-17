# I am overengineering answers to CodeAcademy's classes because my girlfriend is learning.
# Project: Magic 8-Ball

import random

RESPONSES = ['Yes - definitely', 'It is decidedly so', 'Without a doubt', 'Reply hazy, try again', 
             'Ask again later', 'Better not tell you now', 'My sources say no', 'Outlook not so good', 'Very doubtful']

NAME = 'Elena'
QUESTION = 'Does Emma love me'

if NAME == "":
    NAME = 'This person'
 
if QUESTION != '' and QUESTION[-1] not in ['.', '?']:
    QUESTION += '?'


if QUESTION != '':
    print(f'{NAME} asks: {QUESTION}')
    print(f"Magic 8-Ball's answer: {RESPONSES[random.randint(1, len(RESPONSES) - 1)]}")
else:
    print('You need to ask me a question!')
