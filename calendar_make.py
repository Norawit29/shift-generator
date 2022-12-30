import pandas as pd


class Calendar_generate:

    def __init__(self, day_in_month, day_start):

        self.day_in_month = day_in_month
        self.day_start = day_start

        day_list = []

    def list_of_day(self):
        day_list = [i for i in range(self.day_in_month)]
        return day_list

    def create(self):

        cal = pd.DataFrame(columns=["Day", "Weekdays", "Morning_1", "Morning_2", "Afternoon & Night"])

        for i in range(self.day_in_month):
            cal = cal.append(pd.Series(), ignore_index=True)
            cal.loc[i]["Day"] = i + 1

        if self.day_start == "Mon":
            for i in range(self.day_in_month):
                if i % 7 == 0:
                    cal.loc[i]["Weekdays"] = "Mon"
                elif i % 7 == 1:
                    cal.loc[i]["Weekdays"] = "Tue"
                elif i % 7 == 2:
                    cal.loc[i]["Weekdays"] = "Wed"
                elif i % 7 == 3:
                    cal.loc[i]["Weekdays"] = "Thu"
                elif i % 7 == 4:
                    cal.loc[i]["Weekdays"] = "Fri"
                elif i % 7 == 5:
                    cal.loc[i]["Weekdays"] = "Sat"
                elif i % 7 == 6:
                    cal.loc[i]["Weekdays"] = "Sun"

        elif self.day_start == "Tue":
            for i in range(self.day_in_month):
                if i % 7 == 6:
                    cal.loc[i]["Weekdays"] = "Mon"
                elif i % 7 == 0:
                    cal.loc[i]["Weekdays"] = "Tue"
                elif i % 7 == 1:
                    cal.loc[i]["Weekdays"] = "Wed"
                elif i % 7 == 2:
                    cal.loc[i]["Weekdays"] = "Thu"
                elif i % 7 == 3:
                    cal.loc[i]["Weekdays"] = "Fri"
                elif i % 7 == 4:
                    cal.loc[i]["Weekdays"] = "Sat"
                elif i % 7 == 5:
                    cal.loc[i]["Weekdays"] = "Sun"

        elif self.day_start == "Wed":
            for i in range(self.day_in_month):
                if i % 7 == 5:
                    cal.loc[i]["Weekdays"] = "Mon"
                elif i % 7 == 6:
                    cal.loc[i]["Weekdays"] = "Tue"
                elif i % 7 == 0:
                    cal.loc[i]["Weekdays"] = "Wed"
                elif i % 7 == 1:
                    cal.loc[i]["Weekdays"] = "Thu"
                elif i % 7 == 2:
                    cal.loc[i]["Weekdays"] = "Fri"
                elif i % 7 == 3:
                    cal.loc[i]["Weekdays"] = "Sat"
                elif i % 7 == 4:
                    cal.loc[i]["Weekdays"] = "Sun"

        elif self.day_start == "Thu":
            for i in range(self.day_in_month):
                if i % 7 == 4:
                    cal.loc[i]["Weekdays"] = "Mon"
                elif i % 7 == 5:
                    cal.loc[i]["Weekdays"] = "Tue"
                elif i % 7 == 6:
                    cal.loc[i]["Weekdays"] = "Wed"
                elif i % 7 == 0:
                    cal.loc[i]["Weekdays"] = "Thu"
                elif i % 7 == 1:
                    cal.loc[i]["Weekdays"] = "Fri"
                elif i % 7 == 2:
                    cal.loc[i]["Weekdays"] = "Sat"
                elif i % 7 == 3:
                    cal.loc[i]["Weekdays"] = "Sun"

        elif self.day_start == "Fri":
            for i in range(self.day_in_month):
                if i % 7 == 3:
                    cal.loc[i]["Weekdays"] = "Mon"
                elif i % 7 == 4:
                    cal.loc[i]["Weekdays"] = "Tue"
                elif i % 7 == 5:
                    cal.loc[i]["Weekdays"] = "Wed"
                elif i % 7 == 6:
                    cal.loc[i]["Weekdays"] = "Thu"
                elif i % 7 == 0:
                    cal.loc[i]["Weekdays"] = "Fri"
                elif i % 7 == 1:
                    cal.loc[i]["Weekdays"] = "Sat"
                elif i % 7 == 2:
                    cal.loc[i]["Weekdays"] = "Sun"

        elif self.day_start == "Sat":
            for i in range(self.day_in_month):
                if i % 7 == 2:
                    cal.loc[i]["Weekdays"] = "Mon"
                elif i % 7 == 3:
                    cal.loc[i]["Weekdays"] = "Tue"
                elif i % 7 == 4:
                    cal.loc[i]["Weekdays"] = "Wed"
                elif i % 7 == 5:
                    cal.loc[i]["Weekdays"] = "Thu"
                elif i % 7 == 6:
                    cal.loc[i]["Weekdays"] = "Fri"
                elif i % 7 == 0:
                    cal.loc[i]["Weekdays"] = "Sat"
                elif i % 7 == 1:
                    cal.loc[i]["Weekdays"] = "Sun"

        elif self.day_start == "Sun":
            for i in range(self.day_in_month):
                if i % 7 == 1:
                    cal.loc[i]["Weekdays"] = "Mon"
                elif i % 7 == 2:
                    cal.loc[i]["Weekdays"] = "Tue"
                elif i % 7 == 3:
                    cal.loc[i]["Weekdays"] = "Wed"
                elif i % 7 == 4:
                    cal.loc[i]["Weekdays"] = "Thu"
                elif i % 7 == 5:
                    cal.loc[i]["Weekdays"] = "Fri"
                elif i % 7 == 6:
                    cal.loc[i]["Weekdays"] = "Sat"
                elif i % 7 == 0:
                    cal.loc[i]["Weekdays"] = "Sun"

        return cal