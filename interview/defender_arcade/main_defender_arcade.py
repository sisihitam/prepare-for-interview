from process.defender_arcade import overlap
from datetime import datetime
import sys

if __name__ == "__main__":
    previous_start = None
    previous_end = None
    overlap_list = []
    
    for line in sys.stdin:
        curr_start, curr_end = line.split()
        overlap_ = overlap(curr_start, curr_end, previous_start, previous_end)
        if overlap_:
            if not (previous_start, previous_end) in overlap_list:
                overlap_list.append((previous_start, previous_end))
            
            if not (curr_start, curr_end) in overlap_list:
                overlap_list.append((curr_start, curr_end))
        else:
            overlap_list.append(None)
        previous_start = curr_start
        previous_end = curr_end

    temp_counter = 0
    max_counter = 0
    for ov in overlap_list:
        if ov == None:
            if max_counter <= temp_counter:
                max_counter = temp_counter
            temp_counter = 0
        else:
            temp_counter += 1
    
    print("Output {}".format(max_counter))

    for arg in sys.argv[1:]:
        if arg == '-o':
            with open('output/output_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S')), 'w') as f:
                f.write(str(max_counter))

