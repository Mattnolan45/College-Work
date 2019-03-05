import sys
table=sys.stdin.readlines()


def main():
    i=0
    while i<len(table):
        pos=table[i][1]
        club=table[i][2]
        p=table[i][3]
        w=table[i][4]
        d=table[i][5]
        l=table[i][6]


    h1 = 'POS'
    h2 = 'CLUB'
    h3 = 'P'
    h4 = 'W'
    h5 = 'D'
    h6 = 'L'
    
     print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3, h4, h5, h6))
