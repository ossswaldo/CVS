# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:19:22 2019

@author: C092320
"""


import datetime
from datetime import datetime

now = datetime.now() # current date and time

timeF= ("%m-%d-%Y %H:%M:%S:%f")

date_time = now.strftime(timeF)



print(datetime.now(),'Opening Google')

print(date_time)





now2 = datetime.datetime.now()
now2.strftime('%m-%d-%y %H:%M:%S')

