#!/bin/python3

import math
import os
import random
import re
import sys
import math

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    incl = 0
    excl = 0
     
    for i in arr: 
        new_excl = excl if excl>incl else incl 
         
        # Current max including i 
        incl = excl + i 
        excl = new_excl 
      
    # return max of incl and excl 
    return (excl if excl>incl else incl) 