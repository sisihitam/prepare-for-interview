from datetime import datetime
import re
import logging
import logging

FORMAT = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.NOTSET, filename="log/{}.log".format(datetime.now().strftime('%Y%m%d_%H%M%S')), datefmt="%Y-%m-%d %H:%M:%S")

def string_to_roman_number(text):
    chars = {'i': 1, 'v': 5, 'x': 10, 'l': 50}
    result = 0
    text = text.lower()
    is_valid_input = bool(re.match(r'(x{,3}|xl|lx{,3})(i{,3}|iv|vi{,3}|ix)$', text))
    if not is_valid_input:
        logging.error('Invalid Roman character {}'.format(text))
        raise ValueError("Invalid Roman character {}".format(text))

    logging.debug('Word: {}'.format(text))
    for i in range(len(text)):
        logging.debug('Step {}: pick i-th char {}'.format(i, text[i]))
        temp_val = chars[text[i]]
        logging.debug('Step {}: temp_val {}'.format(i, temp_val))
        if i+1 < len(text) and chars[text[i+1]] > temp_val:
            result -= temp_val
            logging.debug('Step {}: -{}'.format(i, temp_val))
        else:
            result += temp_val
            logging.debug('Step {}: +{}'.format(i, temp_val))
        logging.debug('Step {}: result {}'.format(i, result))
    return result

def transform_name(name):
    _name = name.split()
    result = []
    for name in _name:
        try:
            name = str(string_to_roman_number(name))
        except ValueError:
            pass
        finally:
            result.append(name)
    logging.debug('transform name {} to pseudoname {}'.format(" ".join(_name), " ".join(result)))
    return " ".join(result)
