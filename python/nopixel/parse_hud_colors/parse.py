from pathlib import Path
import json


test = []
with open(Path(Path(__file__).parent, 'hud_colors.txt')) as hc_file:
    for x in hc_file:
        y = x.replace('rgba(', '').replace(')', '').replace('\n', '').split('\t')
        test.append({
            'name': y[2].split('HUD_COLOUR_')[1],
            'rgba': y[3].replace(' ', '').split(','),
            'hex': '#ffffff'
        })
        try:  # some of them are references to other colors :)
            test[-1]['rgba'] = list(map(int, test[-1]['rgba']))
            test[-1]['hex'] = f"#{test[-1]['rgba'][0]:02x}{test[-1]['rgba'][1]:02x}{test[-1]['rgba'][2]:02x}"
        except Exception:
            test[-1]['rgba'] = test[-1]['rgba'][0]
            pass


        # print(test[-1]['rgba'])
        # test[-1]['rgba'] = list(map(int, test[-1]['rgba']))

print(test)

with open(Path(Path(__file__).parent, 'hud_colors.json'), "w") as outfile: 
    json.dump(test, outfile, indent=4)