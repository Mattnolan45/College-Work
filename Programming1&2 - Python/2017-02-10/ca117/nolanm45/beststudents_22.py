import sys

try:
    with open(sys.argv[1], "r") as f:
        m = 0
        name = ""

        for line in f:
            try:
                if int(line.split()[0]) > m:
                    m = int(line.split()[0])
                    name = " ".join(line.split()[1:])

                elif int(line.split()[0]) == m:
                    name += ", "
                    name += " ".join(line.split()[1:])

            except ValueError:
                print("Invalid mark {} encountered. Skipping.".format(line.split()[0]))

        print("Best student(s): {}".format(name))
        print("Best mark: {}".format(m))




except FileNotFoundError:
    print("The file {} could not be opened.".format(sys.argv[1]))
