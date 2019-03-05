week = {
    'monday': [],
    'tuesday': [],
    'wednesday': [],
    'thursday': [],
    'friday': [],
    'saturday': [],
    'sunday': []
}

while True:
    text_input = input(
        "\nCommands:\nweek\nday\nadd\nremove\nexit\nEnter command?: ")

    if "week" in text_input:
        for (k, v) in week.items():
            print(k + "\n" + "Appointments: ", v)

    elif "day" in text_input:
        input_day = input("Day: ")
        for (k, v) in week.items():
            if k == input_day:
                print(k)
                print("Appointments:")
                for i in v:
                    print(i)

    elif "remove" in text_input:
        input_day = input("Day: ")
        input_app = input("Appointment: ")
        for (k, v) in week.items():
            if k == input_day:
                for i, j in enumerate(v):
                    j = j.split()
                    if j[0] == input_app:
                        v.pop(i)

    elif "add" in text_input:
        input_day = input("What Day: ")
        input_details = input("Details: ")
        input_time = input("Start Time: ")
        input_end = input("End Time: ")
        for (k, v) in week.items():
            if k == input_day:
                v.append(input_details + " " + input_time + " " + input_end)

    elif "exit" in text_input:
        break

    else:
        print("invalid command")
