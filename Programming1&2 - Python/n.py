import sys
from word_length import get_counts_dict

def main():
    # read the list of words from stdin
    line = sys.stdin.readline()
    line = line.strip()
    words = line.split()

    # call the student's function
    counts = get_counts_dict(words)
    print(type(counts))

    lengths = counts.keys()
    for length in sorted(lengths):
        print(str(length) + ": " + str(counts[length]))

if __name__ == "__main__":
    main()