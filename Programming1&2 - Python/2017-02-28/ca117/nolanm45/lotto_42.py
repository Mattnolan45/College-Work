import sys
import random

matchnums=sys.argv[1:]


lottosample=random.sample(range(1,48),6)
lotto=random.sample(range(1,48),6)*1000000

for n in lotto:
    
