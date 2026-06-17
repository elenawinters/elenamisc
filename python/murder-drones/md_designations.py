from pathlib import Path
import string
import time
import json
import os

# This was made so I could figure out how many possible drones could exist in the Murder Drones universe.
# I chose to generate all possible Serial Designations/Numbers and then derive data from that. Figuring out the math on it's own was hurting my brain.
# This was easier and guaranteed to be accurate ^

valid_sd_check = ['J-10X111001', 'V-X00100000', 'N-0X0010010']
desired_length = len(valid_sd_check[0])
store = []

start_time = time.perf_counter()
for letter in string.ascii_uppercase:
    for digit in range(2 ** (desired_length - 2), 2 ** (desired_length - 1)):
        bits = list(f'{digit:b}')
        bits.pop(0)  # remove leading bit
        for position in range(0, len(bits)):
            intermediate = bits.copy()
            intermediate[position] = 'X'
            designation = f"{letter}-{''.join(intermediate)}"
            assert len(designation) == desired_length, f"Designation '{designation}' should be {desired_length} characters long. It is {len(designation)} characters long instead."
            store.append(designation)

store = list(set(store))  # prune duplicates (if any)
end_time = time.perf_counter()

if desired_length == 11: print(store)
print('---------------------------')
designations_missing = [x for x in valid_sd_check if x not in store]
if len(designations_missing) == 0:
    print(f"{', '.join(valid_sd_check[:-1])}, and {valid_sd_check[-1]} are all in the store. This is good. The data can be considered valid and canonical.")
else:
    print(f"{', and '.join(designations_missing)} {'is' if len(designations_missing) == 1 else 'are'} NOT in the store. This is bad. The data is not canonical.".upper())

pn_length = 7  # example: CYN-MYKX
print(f'Finished in {round((end_time - start_time) * 1000)}ms with a desired length of {desired_length} characters.')
print('---------------------------')
print(f'{len([x for x in store if x.startswith("J-")]):,d} Serial Designations per letter')
print(f'{len(store):,d} Total Possible Serial Designations per P/N')
print(f'{26 ** pn_length:,d} P/N combinations (Example: CYN-MYKX)')
print(f'{len(store) * 26 ** pn_length:,d} {'lore accurate ' if desired_length == 11 else ''}maximum number of drones.')
print('---------------------------')

with open(Path(os.path.dirname(os.path.realpath(__file__)), 'designations.json'), 'w') as f:
    json.dump(sorted(store), f, indent=4)


# Results:
#
# 2,304 Serial Designations per letter
# 59,904 Total Possible Serial Designations per P/N
# 8,031,810,176 P/N combinations (Example: CYN-MYKX)
# 481,137,556,783,104 lore accurate maximum number of drones.
#

# I would write code to generate SDs for all P/Ns and dump to a file, but I estimate that'd take up over 8 petabytes of storage.
