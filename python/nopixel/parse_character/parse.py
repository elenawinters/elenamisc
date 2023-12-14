from pathlib import Path
import json
import glob
import os



# character_datas = ['lara_vandusk.json', 'maeve_shaw.json', 'zoe_zaleski_4.json']

os.chdir(Path(Path(__file__).parent))
for character in glob.glob("*.json"):
    print(character)
    json_data = {}
    with open(Path(Path(__file__).parent, character)) as json_file:
        json_data = json.load(json_file)
    char_details = ''
    # print(json_data)
    # for 

    head_blend = json_data['face']['headBlend']
    char_details += f"Face 1 | {head_blend['shapeFirst']}\n"
    char_details += f"Skin 1 | {head_blend['skinFirst']}\n\n"

    char_details += f"Face 2 | {head_blend['shapeSecond']}\n"
    char_details += f"Skin 2 | {head_blend['skinSecond']}\n\n"

    char_details += f"Face 3 | {head_blend['shapeThird']}\n"
    char_details += f"Skin 3 | {head_blend['skinThird']}\n\n"

    char_details += f"Skin Mix | {head_blend['skinMix']} ({head_blend['skinMix']:.0%})\n"
    char_details += f"Shape Mix | {head_blend['shapeMix']} ({head_blend['shapeMix']:.0%})\n"
    char_details += f"Third Face Mix | {head_blend['thirdMix']} ({head_blend['thirdMix']:.0%})\n"
    char_details += f"hasParent | {head_blend['hasParent']} (dunno what this means)\n"

    # char_details += f"Skin 1 | ${head_blend['skinFirst']}\n"
    # char_details += f"Skin 2 | ${head_blend['skinSecond']}\n"
    # char_details += f"Skin 3 | ${head_blend['skinThird']}\n"
    # char_details += f"Skin Mix | {head_blend['skinMix']} ({head_blend['skinMix']:.0%})\n"
    char_details += '## Fine Details\n'
    char_details += '#### PARSING IN THIS SECTION MAY BE WRONG\n'
    char_details += "-1 is all the way left, 0 is center point, 1 is all the way right\n"

    head_struct = json_data['face']['headStructure']
    char_details += '### NOSE\n'
    char_details += f"Nose Width | {head_struct[0]} ({head_struct[0]:.0%})\n"
    char_details += f"Peak Height | {head_struct[1]} ({head_struct[1]:.0%})\n"
    char_details += f"Peak Lowering | {head_struct[2]} ({head_struct[2]:.0%})\n"
    char_details += f"Bone Height | {head_struct[3]} ({head_struct[3]:.0%})\n"
    char_details += f"Peak Length | {head_struct[4]} ({head_struct[4]:.0%})\n"
    char_details += f"Bone Twist | {head_struct[5]} ({head_struct[5]:.0%})\n"

    # char_details += '### NOSE - parse variation 2\n'
    # char_details += f"Nose Width | {head_struct[0]} ({head_struct[0]:.0%})\n"
    # char_details += f"Bone Height | {head_struct[1]} ({head_struct[1]:.0%})\n"
    # char_details += f"Peak Height | {head_struct[2]} ({head_struct[2]:.0%})\n"
    # char_details += f"Peak Length | {head_struct[3]} ({head_struct[3]:.0%})\n"
    # char_details += f"Peak Lowering | {head_struct[4]} ({head_struct[4]:.0%})\n"
    # char_details += f"Bone Twist | {head_struct[5]} ({head_struct[5]:.0%})\n"

    char_details += '### EYEBROWS\n'
    char_details += f"Eyebrow Height | {head_struct[6]} ({head_struct[6]:.0%})\n"
    char_details += f"Eyebrow Depth | {head_struct[7]} ({head_struct[7]:.0%})\n"

    char_details += '### CHEEKS\n'
    char_details += f"Cheek Bone Height | {head_struct[8]} ({head_struct[8]:.0%})\n"
    char_details += f"Cheek Bone Width | {head_struct[9]} ({head_struct[9]:.0%})\n"
    char_details += f"Cheek Width | {head_struct[10]} ({head_struct[10]:.0%})\n"

    char_details += '### JAW BONE\n'
    char_details += f"Jaw Bone Width | {head_struct[11]} ({head_struct[11]:.0%})\n"
    char_details += f"Jaw Bone Length | {head_struct[12]} ({head_struct[12]:.0%})\n"
    
    char_details += '### CHIN\n'
    char_details += f"Chin Bone Height | {head_struct[13]} ({head_struct[13]:.0%})\n"
    char_details += f"Chin Bone Width | {head_struct[14]} ({head_struct[14]:.0%})\n"
    char_details += f"Chin Bone Length | {head_struct[15]} ({head_struct[15]:.0%})\n"
    char_details += f"Chin Cleft | {head_struct[16]} ({head_struct[16]:.0%})\n"

    # char_details += '### CHIN - parse variation 2\n'
    # char_details += f"Chin Bone Height | {head_struct[13]} ({head_struct[13]:.0%})\n"
    # char_details += f"Chin Bone Length | {head_struct[14]} ({head_struct[14]:.0%})\n"
    # char_details += f"Chin Bone Width | {head_struct[15]} ({head_struct[15]:.0%})\n"
    # char_details += f"Chin Cleft | {head_struct[16]} ({head_struct[16]:.0%})\n"

    char_details += '### MISC\n'
    char_details += f"Eyes Squint | {head_struct[17]} ({head_struct[17]:.0%})\n"
    char_details += f"Neck Thickness | {head_struct[18]} ({head_struct[18]:.0%})\n"
    char_details += f"Lips Thickness | {head_struct[19]} ({head_struct[19]:.0%})\n"

    # char_details += '### MISC - parse variation 2\n'
    # char_details += f"Eyes Squint | {head_struct[17]} ({head_struct[17]:.0%})\n"
    # char_details += f"Lips Thickness | {head_struct[18]} ({head_struct[18]:.0%})\n"
    # char_details += f"Neck Thickness | {head_struct[19]} ({head_struct[19]:.0%})\n"


    headOverlay = {}
    body_blemish_hit_twice = False
    for x in json_data['face']['headOverlay']:
        name = x['name']
        if x['name'] == 'AddBodyBlemishes':
            name = 'AddBodyBlemishes_01'
            if body_blemish_hit_twice == True:
                name = 'AddBodyBlemishes_02'
            body_blemish_hit_twice = True

        y = x
        del y['name']
        headOverlay[name] = y
    headOverlayOrdered = dict(sorted(headOverlay.items()))

    char_details += '## MAKEUP AND IMPERFECTIONS\n'
    for key in headOverlayOrdered:
        value = headOverlayOrdered[key]
        disclaimer = ''
        if str(key).startswith('AddBodyBlemishes'):
            disclaimer = "\n#### Body Blemishes differ from Blemishes, and there are 2 of these values. Only one of them is used."

        char_details += f"### {key}{disclaimer}\n"
        char_details += f"Overlay Value | {value['overlayValue'] + 1 if value['overlayValue'] != 255 else 0}\n"
        char_details += f"Opacity | {value['overlayOpacity']} ({value['overlayOpacity']:.0%})\n"
        char_details += f"Color Type | {value['colourType']}\n"
        char_details += f"First Color | {value['firstColour']}\n"
        char_details += f"Second Color | {value['secondColour']}\n"
        

    # print(headOverlayOrdered)

    # print(char_details)
    with open(f"{Path(Path(__file__).parent, character.split('.')[0])}.md", 'w') as f:
        f.write(f"# Character file: {character.split('.')[0]}<br>\n")
        f.write(char_details.replace('\n', '<br>\n'))
    # for idx, x in enumerate(json_data['face']['headStructure']):

    #     print(idx, x)

    # skinMix
    # shapeThird
    # shapeMix
    # shapeFirst
    # shapeSecond
    # thirdMix
    # hasParent
    # skinThird
    # skinFirst
    # skinSecond