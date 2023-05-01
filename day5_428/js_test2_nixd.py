'''
Author: yanxiao333 yanxiao_333@126.com
Date: 2023-04-30 15:08:09
LastEditors: yanxiao333 yanxiao_333@126.com
LastEditTime: 2023-04-30 15:16:58
FilePath: \t2023_new_one\day5_428\js_test2_nixd.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import math
import time
import base64

time1 = math.floor(time.time() )
print(time1)
mcode = base64.b64encode(str(time1).encode()).decode()
print(mcode)
