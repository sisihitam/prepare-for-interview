#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter= dict(collections.Counter(ar))
    result = 0
    for c in counter:
        result += int(counter[c] / 2)
    return result
