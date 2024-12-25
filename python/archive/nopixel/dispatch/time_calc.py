# from pathlib import Path
import datetime
import re

filepath = r"C:\Users\elena\Documents\NP Dispatch Server - Dispatchers - dispatch-log [807657412898717726].txt"

# time_re = r"(\d+h)?(\d+m)?(\d+s)"
# m = r'\[.+] YAGPDB\.xyz#8760\n@.+ clocked out at .+\((.+)\)'
char_re = r'\[.+] YAGPDB\.xyz#8760\n@D-70 \| J\. Sawyer clocked out at .+\((\d+h)?(\d+m)?(\d+s)\)'
# char_re = r'\[.+] YAGPDB\.xyz#8760\n@D-72 \| M\. Shaw clocked out at .+\((\d+h)?(\d+m)?(\d+s)\)'
# jsawyer = r'\[.+] YAGPDB\.xyz#8760\n@D-70 \| J\. Sawyer clocked out at .+\((.+)\)'
# \[.+] YAGPDB\.xyz#8760\n@.+ clocked out at .+\((.+)\)
# \[.+] YAGPDB\.xyz#8760\n@.+ clocked out at .+\((\d+h)?(\d+m)?(\d+s)\)

# f = open(filepath, "r")
# for x in f:
#   print(x)
with open(filepath, encoding='utf8') as my_file:
    current_timedelta = datetime.timedelta(hours=0)
    for dutyontime in re.findall(char_re, my_file.read()):
        h = dutyontime[0].replace('h', '')
        m = dutyontime[1].replace('m', '')
        s = dutyontime[2].replace('s', '')
        if h == '': h = 0
        if m == '': m = 0
        if s == '': m = 0
        current_timedelta = current_timedelta + datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        # dutyontime[0].replace('h', ' ')
        # print(dutyontime)
        # times.append(dutyontime)
    print(current_timedelta)
    # 459 hours, 49 minutes, 2 seconds
    # print(len(times))
    # print(my_file.read())
#
# [2/6/2021 2:58 PM] YAGPDB.xyz#8760
# @935 | C. Everly clocked in at 06 February 2021 20:58
# 
# for k, v, _ in re.findall(jsawyer, my_file.read()):