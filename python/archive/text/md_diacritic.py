import random
import dcl

dcls = [dcl.acute, dcl.breve, dcl.caron, dcl.cedilla, dcl.grave, dcl.interpunct, dcl.macron,
        dcl.ogonek, dcl.ring, dcl.ring_and_acute, dcl.slash, dcl.stroke, dcl.stroke_and_acute,
        dcl.tilde, dcl.tittle, dcl.umlaut, dcl.umlaut_and_macron]
        

def normalize(min, max, current):
    return (current - min) / (max - min) if max != min else 0

mdtext = "I DID!! I HAD A RAILGUN POINTED AT MY CHEST, AND I TRIED!! INSTEAD, I GOT KILLED, WAS REVIVED AGAINST MY WILL, AND FORCED THE SERVE THE VERY BEING THAT KILLED THE ONE I LOVED!!"
random.seed(mdtext)

def process_md_text(test):
    out = []
    for index, entry in enumerate(test):
        # print(entry)

        char = entry
        chance = normalize(0, len(test) - 1, index)
        for x in range(len(dcls)):
            if chance < (x + 1) / len(dcls):
                random.shuffle(dcls)
                number_of_diacritics = dcls[:x // 2 + 1]
                
                for y in number_of_diacritics:
                    try:
                        char = y(char)
                    except Exception as e:
                        char = char
                    # print(f"Adding diacritic {y} to '{entry}' with chance {chance:.2f}")
                # print(f"Adding diacritic {dcls[x]} to '{entry}' with chance {chance:.2f}")
                # diacritic = dcls[x]
                break
        out.append(char)
                # break
        # print(normalize(0, len(mdtext) - 1, index))
        # print(index)
        # print(len(mdtext) - 1)
    return out

print(''.join(process_md_text(mdtext)))