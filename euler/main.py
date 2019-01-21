import sys
import time

from euler5 import *
from euler10 import *
from euler15 import *

for i in range(1, 15+1):
    aug_func = 'euler' + str(i)
    try:
        start_time = time.time()
        question, answer = getattr(sys.modules[__name__], '%s' % aug_func)()
        if answer is not None:
            print('(%i) %s' % (i, question))
            elapsed_time = time.time() - start_time
            print('Time %.4f secs \t Ans: %s' % (np.round(elapsed_time, 4), str(answer)))
            print('')
    except AttributeError:
        raise RuntimeWarning("Method %s not found", aug_func)
