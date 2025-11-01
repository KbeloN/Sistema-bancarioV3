from datetime import datetime,date,time,timedelta

date_trans_now = datetime(2025,5,5)
date_trans_before = datetime(2025,5,4)
date_now = datetime(2025,5,5)

res1 = date_trans_now - date_now
res2 = date_now - date_trans_before
res3 = date_trans_now - date_trans_before

print(res1.__class__)