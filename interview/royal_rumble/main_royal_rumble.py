from process.royal_rumble import transform_name
from datetime import datetime
import sys

if __name__ == "__main__":
    all = []
    original_name = {}

    for line in sys.stdin:
        name = line.split()
        _name = []
        
        for l in name:
            _name.append(transform_name(l))
        
        pseudo_name = " ".join(_name)
        original_name.setdefault(pseudo_name, line)
        all.append(pseudo_name)

    result = list(map(lambda x: original_name[x].replace('\n',''), sorted(all)))
    print("Output {}".format(result))

    for arg in sys.argv[1:]:
        if arg == '-o':
            with open('output/output_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S')), 'w') as f:
                f.write("\n".join(result))

