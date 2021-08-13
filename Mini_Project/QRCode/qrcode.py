# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:12:44 2021

@author: thanh
"""

import pyqrcode

input_data = "https://www.youtube.com/channel/UC9L5_YMFz8JfBeQtUic8-3A"

qr = pyqrcode.create(input_data)

qr.svg('qr_code.svg', scale = 8)

qr.png('qr_code.png', scale = 12)
