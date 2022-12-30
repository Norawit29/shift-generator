import pandas as pd
import random
from calendar_make import Calendar_generate
import time


class ShiftGenerator(Calendar_generate):

    def __init__(self, day_in_month, day_start, staff_names):
        super().__init__(day_in_month, day_start)
        self.staff_names = staff_names

    def random_shift(self):

        day_list = Calendar_generate.list_of_day(self)
        cal = Calendar_generate.create(self)

        ## WEEKDAYS ##

        # Create copy calendar to count shift request
        cal_copy = cal.copy()
        cal_copy.fillna(0, inplace=True)

        # Count shift request
        unavailable = self.staff_names
        for i in unavailable:
            for j in unavailable[i]:
                for k in (unavailable[i][j]):
                    cal_copy.loc[j - 1, k] += 1

        # Index of weekday sort by number of request
        weekday = list(cal_copy.loc[(cal_copy["Weekdays"] != "Sat") & (cal_copy["Weekdays"] != "Sun")]["Day"])
        weekday_sort_index = list(
            cal_copy.loc[(cal_copy["Weekdays"] != "Sat") & (cal_copy["Weekdays"] != "Sun")].sort_values(
                ["Morning_1", "Afternoon & Night"], ascending=[False, False]).index)

        # Sort staff name based on number of request
        unavailable_sort = sorted(unavailable, key=lambda key: len(unavailable[key]), reverse=True)

        # Empty dict for weefday_slot
        weekday_dict = {}
        for i in weekday:
            weekday_dict.update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        # Shift count
        shift_count_morning = dict.fromkeys(unavailable, 0)
        limit_shift_morning = (((len(weekday_sort_index) // len(unavailable)) + 1) * 2) - 2

        shift_count_afternoon = dict.fromkeys(unavailable, 0)
        limit_shift_afternoon = ((len(weekday_sort_index) // len(unavailable)) + 1) - 1

        # First Round
        shuffle_weekday = []
        shuffle_weekday.extend(random.sample(weekday_sort_index[0:4], 4))
        shuffle_weekday.extend(random.sample(weekday_sort_index[4:8], 4))
        shuffle_weekday.extend(random.sample(weekday_sort_index[8:12], 4))
        shuffle_weekday.extend(random.sample(weekday_sort_index[12:16], 4))
        shuffle_weekday.extend(random.sample(weekday_sort_index[16:], len(weekday_sort_index[16:])))

        for i in shuffle_weekday:

            for name in unavailable_sort:

                if shift_count_morning[name] < limit_shift_morning:
                    if (i + 1) not in list(unavailable[name].keys()):
                        cal.loc[i, "Morning_1"] = name
                        weekday_dict[i + 1].remove("Morning_1")
                        shift_count_morning[name] += 1
                        break

                    elif (i + 1) in list(unavailable[name].keys()):
                        if "Morning_1" not in unavailable[name][i + 1]:
                            cal.loc[i, "Morning_1"] = name
                            weekday_dict[i + 1].remove("Morning_1")
                            shift_count_morning[name] += 1
                            break

            for name in unavailable_sort:

                if shift_count_morning[name] < limit_shift_morning:
                    if ((i + 1) not in list(unavailable[name].keys())) & (cal.loc[i, "Morning_1"] != name):
                        cal.loc[i, "Morning_2"] = name
                        weekday_dict[i + 1].remove("Morning_2")
                        shift_count_morning[name] += 1
                        break

                    elif (i + 1) in list(unavailable[name].keys()):
                        if "Morning_2" not in unavailable[name][i + 1]:
                            cal.loc[i, "Morning_2"] = name
                            weekday_dict[i + 1].remove("Morning_2")
                            shift_count_morning[name] += 1
                            break

            for name in unavailable_sort:

                if shift_count_afternoon[name] < limit_shift_afternoon:
                    if (i + 1) not in list(unavailable[name].keys()):
                        cal.loc[i, "Afternoon & Night"] = name
                        weekday_dict[i + 1].remove("Afternoon & Night")
                        shift_count_afternoon[name] += 1
                        break

                    elif (i + 1) in list(unavailable[name].keys()):
                        if ("Afternoon & Night" not in unavailable[name][i + 1]):
                            cal.loc[i, "Afternoon & Night"] = name
                            weekday_dict[i + 1].remove("Afternoon & Night")
                            shift_count_morning[name] += 1
                            break

        # Second Round
        reversed_list = unavailable_sort[::-1]
        weekday_dict2 = weekday_dict.copy()

        # index of rest slot
        rest_day = [i for i in weekday_dict if weekday_dict[i] != []]
        rest_index = [i - 1 for i in rest_day]

        for i in rest_index:

            for shift in weekday_dict[i + 1]:

                if shift == "Morning_1":
                    for name in reversed_list:

                        if shift_count_morning[name] < (limit_shift_morning + 1):
                            if ((i + 1) not in list(unavailable[name].keys())) & (cal.loc[i, "Morning_2"] != name):
                                cal.loc[i, shift] = name
                                shift_count_morning[name] += 1
                                weekday_dict2[i + 1] = [i for i in weekday_dict2[i + 1] if i != "Morning_1"]
                                break



                elif shift == "Morning_2":
                    for name in reversed_list:

                        if shift_count_morning[name] < (limit_shift_morning + 1):
                            if ((i + 1) not in list(unavailable[name].keys())) & (cal.loc[i, "Morning_1"] != name):
                                cal.loc[i, shift] = name
                                shift_count_morning[name] += 1
                                weekday_dict2[i + 1] = [i for i in weekday_dict2[i + 1] if i != "Morning_2"]
                                break


                elif shift == "Afternoon & Night":
                    for name in reversed_list:
                        if shift_count_afternoon[name] < (limit_shift_afternoon + 1):
                            if (i + 1) not in list(unavailable[name].keys()):
                                cal.loc[i, shift] = name
                                shift_count_afternoon[name] += 1
                                weekday_dict2[i + 1] = [i for i in weekday_dict2[i + 1] if i != "Afternoon & Night"]
                                break

        # Third Round

        # index of rest slot
        rest_day = [i for i in weekday_dict2 if weekday_dict2[i] != []]
        rest_index = [i - 1 for i in rest_day]

        random.shuffle(reversed_list)

        for i in rest_index:

            for shift in weekday_dict2[i + 1]:

                if shift == "Morning_1":
                    for name in reversed_list:

                        if shift_count_morning[name] < (limit_shift_morning + 2):
                            if ((i + 1) not in list(unavailable[name].keys())) & (cal.loc[i, "Morning_2"] != name):
                                cal.loc[i, shift] = name
                                shift_count_morning[name] += 1
                                break



                elif shift == "Morning_2":
                    for name in reversed_list:

                        if shift_count_morning[name] < (limit_shift_morning + 2):
                            if ((i + 1) not in list(unavailable[name].keys())) & (cal.loc[i, "Morning_1"] != name):
                                cal.loc[i, shift] = name
                                shift_count_morning[name] += 1
                                break


                elif shift == "Afternoon & Night":
                    for name in reversed_list:
                        if shift_count_afternoon[name] < (limit_shift_afternoon + 2):
                            if (i + 1) not in list(unavailable[name].keys()):
                                cal.loc[i, shift] = name
                                shift_count_afternoon[name] += 1
                                break

        ## WEEKEND ##
        weekend_index = [i for i in cal.loc[(cal["Weekdays"] == "Sat") | (cal["Weekdays"] == "Sun")].index]
        weekend = [i + 1 for i in weekend_index]
        shift_count_weekend = dict.fromkeys(unavailable, 0)

        unavailable_sort = sorted(self.staff_names, key=lambda key: len(self.staff_names[key]), reverse=True)

        for i in unavailable_sort:
            if len(weekend) != 0:

                timeout = time.time() + 5

                while True:
                    rand = random.choice(weekend)
                    if time.time() > timeout:
                        break
                    elif rand not in list(self.staff_names[i].keys()):
                        break

            if len(weekend) != 0:
                cal.loc[rand - 1]["Morning_1"] = i
                cal.loc[rand - 1]["Morning_2"] = ""
                cal.loc[rand - 1]["Afternoon & Night"] = i
                shift_count_weekend[i] += 1
                weekend.remove(rand)

        for i in weekend:
            for j in unavailable_sort:
                if i not in list(self.staff_names[j].keys()):
                    cal.loc[i - 1]["Morning_1"] = j
                    cal.loc[i - 1]["Morning_2"] = ""
                    cal.loc[i - 1]["Afternoon & Night"] = j
                    shift_count_weekend[j] += 1
                    break

        return (cal, shift_count_morning, shift_count_afternoon, shift_count_weekend)


