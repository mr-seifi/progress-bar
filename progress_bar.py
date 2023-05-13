import sys
from math import ceil


def normal_prg(prg, all):
    sys.stdout.write('\r')
    sys.stdout.write('[%-19s] %d%%' % ('=' * int(prg / ceil(all / 20)), 
                                             int(prg / ceil(all / 100)) + 1))
    sys.stdout.flush()
