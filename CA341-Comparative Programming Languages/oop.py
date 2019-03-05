import calendar as c


class Day:

    def __init__(self, weekday):
        self.weekday = weekday
        self.apps = []

    def show_apps(self):
        if len(self.apps) == 0:
            print("No appointments")

        for i, j in enumerate(self.apps):
            print("Appointment no "+str(i+1)+": ", j)

    def __str__(self):
        return '{} {}'.format(self.weekday, self.apps)


class week(Day):

    def __init__(self):
        Day.__init__(self, weekday="")
        self.current_week = [Day("monday"), Day("tuesday"), Day("wednesday"), Day("thursday"), Day("friday"), Day("saturday"), Day("sunday")]

    def print_current_week(self):
        print("\nThis week\n")
        for i in self.current_week:
            print(i.weekday, "\n")
            i.show_apps()
            print()

    def print_day(self, d):
        for i in self.current_week:
            if i.weekday == d:
                print(d)
                i.show_apps()

    def add_app(self, app_day, name, input_time, end):
        for i in self.current_week:
            if i.weekday == app_day:
                i.apps.append(Appointment(name, input_time, end))

    def remove_app(self, app_day, app_name):
        for i in self.current_week:
            if app_day == i.weekday:
                for counter, v in enumerate(i.apps):
                    if v.name == app_name:
                        i.apps.pop(counter)


class Appointment:

    def __init__(self, name, app_time, end):
        self.name = name
        self.app_time = app_time
        self.end = end

    def __str__(self):
        return "Details: {} Time: {}-{} ".format(self.name, self.app_time, self.end)


def run():

    ca = week()
    print(c.calendar(2018))

    print("\nCommands:\nweek\nday\nadd\nremove\n")
    while True:
        n = input("Enter your command: ")
        if "week" in n:
            ca.print_current_week()

        elif "day" in n:
            d = input("which day:")
            ca.print_day(d)

        elif "add" in n:
            input_day = input("Day: ")
            input_time = input("Time: ")
            end = input("End: ")
            details = input("Details: ")
            ca.add_app(input_day, details, input_time, end)

        elif "remove"in n:
            input_day = input("Which Day: ")
            input_app = input("Which appointment:")
            ca.remove_app(input_day, input_app)

        elif "quit" in n:
            break


if __name__ == '__main__':
    run()
