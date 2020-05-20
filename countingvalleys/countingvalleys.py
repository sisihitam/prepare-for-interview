#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    goValey = 0
    result = 0
    for x in s:
        if x == 'D':
            level -= 1
        else:
            level += 1
            
        if level < 0 and goValey < 1:
            goValey = 1
        else:
            if goValey > 0 and level >= 0:
                result += 1
                goValey = 0
    return result        