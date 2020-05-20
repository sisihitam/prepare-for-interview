from datetime import datetime
import re
import logging
import logging

FORMAT = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.NOTSET, filename="log/{}.log".format(datetime.now().strftime('%Y%m%d_%H%M%S')), datefmt="%Y-%m-%d %H:%M:%S")

def overlap(start1, end1, start2, end2):
    if end1 == None or start1 == None or start2 == None or end2 == None: 
        return False
    logging.debug("{}{}#{}{} => {}".format(str(start2), str(end2), str(start1), str(end1), str((int(end1) > int(start2)) and (int(end2) > int(start1)))))
    return (int(end1) > int(start2)) and (int(end2) > int(start1))