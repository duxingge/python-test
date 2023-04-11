#!/usr/bin/python3
import pymysql




channels = ["MITRA","TCASH"]


partner_order_count_dict = {channel: 0 for channel in channels}

if "MITRA" in channels:
    print()
elif "TCASH" in channels:

    print("in....")

for c, v in partner_order_count_dict.items():
    print(c , v)



