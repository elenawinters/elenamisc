


import random

i = "No. I’ve wanted to apologize for around a year now. I’ve been telling myself I’d apologize before I died, though, that’s happening much sooner than I anticipated."


def murder_my_drone_till_i_(text):
    words = text.split(' ')
    random.seed(text)
    accumulator = []
    for word in words:
        mode = 'startforced'
        repeats = 1
        if len(word) >= 2:
            mode = random.choice(['start', 'rand', 'rand'])
            # repeats = random.choice([1, 1, 1, 1, 2])
        print(mode)
        match mode:
            case 'start' | 'startforced':
                first = word[0]
                part = first + "-"

                part += (first.lower() + "-") * (repeats - 1) + first.lower()

                # part += first.lower() + "-" * repeats
                # for x in range(repeats):
                #     part += "-" + first.lower()

                accumulator.append(part + word[1:])
            case 'rand':
                pos = random.randint(0, len(word) - 1)
                print(pos)
                accumulator.append(word)


    return ' '.join(accumulator)

glitched = murder_my_drone_till_i_(i)
print(glitched)




# def stutter_word(word, repeats=2):
#     if not word:
#         return word
#     first = word[0]
#     stutter_part = (first + "-") * repeats + first
#     return stutter_part + word[1:]

# def glitch_word(word):
#     if len(word) <= 1:
#         return word
#     # Randomly stutter at start
#     if random.random() < 0.3:
#         repeats = random.randint(1, 2)
#         word = stutter_word(word, repeats)
#     # Randomly stutter mid-word
#     if random.random() < 0.4 and len(word) > 3:
#         pos = random.randint(1, len(word)-2)
#         letter = word[pos]
#         repeats = random.randint(1, 2)
#         stutter = (letter + "-") * repeats + letter
#         word = word[:pos] + stutter + word[pos+1:]
#     return word

# def glitch_text(text):
#     words = text.split()
#     glitched_words = [glitch_word(word) for word in words]
#     return ' '.join(glitched_words)
