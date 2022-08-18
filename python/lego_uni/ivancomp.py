# This script compares a CDClient.fdb (1.10.64) verses an ivantest.fdb (1.4.49),
# Specifically for any extra data in ivantest compared to CDClient.

import sqlite3

itv = 'ivantest.sqlite'
cdc = 'CDClient.sqlite'

# cdc_conn = sqlite3.connect('CDClient.sqlite')
# cdc = cdc_conn.cursor()
# itv_conn = sqlite3.connect('ivantest.sqlite')
# itv = itv_conn.cursor()

conn = sqlite3.connect(itv)
conn.execute(conn.execute("ATTACH ? AS cdc", [cdc]))

res1 = conn.execute("""SELECT * FROM main.fdetail
                       WHERE keyid NOT IN
                         (SELECT keyid FROM cdc.fdetail)
                    """).fetchall()
res2 = conn.execute("""SELECT * FROM cdc.fdetail
                       WHERE keyid NOT IN
                         (SELECT keyid FROM main.fdetail)
                    """).fetchall()


result = set(res1).symmetric_difference(set(res2))

print(result)