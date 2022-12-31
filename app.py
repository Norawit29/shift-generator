from calendar_make import Calendar_generate
from shift_generate import ShiftGenerator
from flask import Flask, render_template, request, make_response
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
import os

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class DetailFormPage(MethodView):

    def get(self):
        detail_form = DetailsForm()
        return render_template('shift_form.html',
                           detailsform = detail_form)

    def post(self):
        detailsform = DetailsForm(request.form)
        days_in_month = int(detailsform.days_in_month.data)
        start_day = str(detailsform.start_day.data)

        names = {}

        name_1 = str(detailsform.name_1.data)
        unavailable_1_morning = str(detailsform.unavailable_1_morning.data)
        unavailable_1_morning = [int(i) for i in unavailable_1_morning.split(",") if i != ""]
        unavailable_1_afternoon = str(detailsform.unavailable_1_afternoon.data)
        unavailable_1_afternoon = [int(i) for i in unavailable_1_afternoon.split(",") if i != ""]
        unavailable_1_all = str(detailsform.unavailable_1_all.data)
        unavailable_1_all = [int(i) for i in unavailable_1_all.split(",") if i != ""]
        if name_1 != "":
            names[name_1] = {}
            for i in unavailable_1_morning:
                names[name_1].update({i : ["Morning_1", "Morning_2"]})
            for i in unavailable_1_afternoon:
                names[name_1].update({i : ["Afternoon & Night"]})
            for i in unavailable_1_all:
                names[name_1].update({i : ["Morning_1", "Morning_2", "Afternoon & Night"]})

        name_2 = str(detailsform.name_2.data)
        unavailable_2_morning = str(detailsform.unavailable_2_morning.data)
        unavailable_2_morning = [int(i) for i in unavailable_2_morning.split(",") if i != ""]
        unavailable_2_afternoon = str(detailsform.unavailable_2_afternoon.data)
        unavailable_2_afternoon = [int(i) for i in unavailable_2_afternoon.split(",") if i != ""]
        unavailable_2_all = str(detailsform.unavailable_2_all.data)
        unavailable_2_all = [int(i) for i in unavailable_2_all.split(",") if i != ""]
        if name_2 != "":
            names[name_2] = {}
            for i in unavailable_2_morning:
                names[name_2].update({i: ["Morning_1", "Morning_2"]})
            for i in unavailable_2_afternoon:
                names[name_2].update({i: ["Afternoon & Night"]})
            for i in unavailable_2_all:
                names[name_2].update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        name_3 = str(detailsform.name_3.data)
        unavailable_3_morning = str(detailsform.unavailable_3_morning.data)
        unavailable_3_morning = [int(i) for i in unavailable_3_morning.split(",") if i != ""]
        unavailable_3_afternoon = str(detailsform.unavailable_3_afternoon.data)
        unavailable_3_afternoon = [int(i) for i in unavailable_3_afternoon.split(",") if i != ""]
        unavailable_3_all = str(detailsform.unavailable_3_all.data)
        unavailable_3_all = [int(i) for i in unavailable_3_all.split(",") if i != ""]
        if name_3 != "":
            names[name_3] = {}
            for i in unavailable_3_morning:
                names[name_3].update({i: ["Morning_1", "Morning_2"]})
            for i in unavailable_3_afternoon:
                names[name_3].update({i: ["Afternoon & Night"]})
            for i in unavailable_3_all:
                names[name_3].update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        name_4 = str(detailsform.name_4.data)
        unavailable_4_morning = str(detailsform.unavailable_4_morning.data)
        unavailable_4_morning = [int(i) for i in unavailable_4_morning.split(",") if i != ""]
        unavailable_4_afternoon = str(detailsform.unavailable_4_afternoon.data)
        unavailable_4_afternoon = [int(i) for i in unavailable_4_afternoon.split(",") if i != ""]
        unavailable_4_all = str(detailsform.unavailable_4_all.data)
        unavailable_4_all = [int(i) for i in unavailable_4_all.split(",") if i != ""]
        if name_4 != "":
            names[name_4] = {}
            for i in unavailable_4_morning:
                names[name_4].update({i: ["Morning_1", "Morning_2"]})
            for i in unavailable_4_afternoon:
                names[name_4].update({i: ["Afternoon & Night"]})
            for i in unavailable_4_all:
                names[name_4].update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        name_5 = str(detailsform.name_5.data)
        unavailable_5_morning = str(detailsform.unavailable_5_morning.data)
        unavailable_5_morning = [int(i) for i in unavailable_5_morning.split(",") if i != ""]
        unavailable_5_afternoon = str(detailsform.unavailable_5_afternoon.data)
        unavailable_5_afternoon = [int(i) for i in unavailable_5_afternoon.split(",") if i != ""]
        unavailable_5_all = str(detailsform.unavailable_5_all.data)
        unavailable_5_all = [int(i) for i in unavailable_5_all.split(",") if i != ""]
        if name_5 != "":
            names[name_5] = {}
            for i in unavailable_5_morning:
                names[name_5].update({i: ["Morning_1", "Morning_2"]})
            for i in unavailable_5_afternoon:
                names[name_5].update({i: ["Afternoon & Night"]})
            for i in unavailable_5_all:
                names[name_5].update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        name_6 = str(detailsform.name_6.data)
        unavailable_6_morning = str(detailsform.unavailable_6_morning.data)
        unavailable_6_morning = [int(i) for i in unavailable_6_morning.split(",") if i != ""]
        unavailable_6_afternoon = str(detailsform.unavailable_6_afternoon.data)
        unavailable_6_afternoon = [int(i) for i in unavailable_6_afternoon.split(",") if i != ""]
        unavailable_6_all = str(detailsform.unavailable_6_all.data)
        unavailable_6_all = [int(i) for i in unavailable_6_all.split(",") if i != ""]
        if name_6 != "":
            names[name_6] = {}
            for i in unavailable_6_morning:
                names[name_6].update({i: ["Morning_1", "Morning_2"]})
            for i in unavailable_6_afternoon:
                names[name_6].update({i: ["Afternoon & Night"]})
            for i in unavailable_6_all:
                names[name_6].update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        name_7 = str(detailsform.name_7.data)
        unavailable_7_morning = str(detailsform.unavailable_7_morning.data)
        unavailable_7_morning = [int(i) for i in unavailable_7_morning.split(",") if i != ""]
        unavailable_7_afternoon = str(detailsform.unavailable_7_afternoon.data)
        unavailable_7_afternoon = [int(i) for i in unavailable_7_afternoon.split(",") if i != ""]
        unavailable_7_all = str(detailsform.unavailable_7_all.data)
        unavailable_7_all = [int(i) for i in unavailable_7_all.split(",") if i != ""]
        if name_7 != "":
            names[name_7] = {}
            for i in unavailable_7_morning:
                names[name_7].update({i: ["Morning_1", "Morning_2"]})
            for i in unavailable_7_afternoon:
                names[name_7].update({i: ["Afternoon & Night"]})
            for i in unavailable_7_all:
                names[name_7].update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        name_8 = str(detailsform.name_8.data)
        unavailable_8_morning = str(detailsform.unavailable_8_morning.data)
        unavailable_8_morning = [int(i) for i in unavailable_8_morning.split(",") if i != ""]
        unavailable_8_afternoon = str(detailsform.unavailable_8_afternoon.data)
        unavailable_8_afternoon = [int(i) for i in unavailable_8_afternoon.split(",") if i != ""]
        unavailable_8_all = str(detailsform.unavailable_8_all.data)
        unavailable_8_all = [int(i) for i in unavailable_8_all.split(",") if i != ""]
        if name_8 != "":
            names[name_8] = {}
            for i in unavailable_8_morning:
                names[name_8].update({i: ["Morning_1", "Morning_2"]})
            for i in unavailable_8_afternoon:
                names[name_8].update({i: ["Afternoon & Night"]})
            for i in unavailable_8_all:
                names[name_8].update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        name_9 = str(detailsform.name_9.data)
        unavailable_9_morning = str(detailsform.unavailable_9_morning.data)
        unavailable_9_morning = [int(i) for i in unavailable_9_morning.split(",") if i != ""]
        unavailable_9_afternoon = str(detailsform.unavailable_9_afternoon.data)
        unavailable_9_afternoon = [int(i) for i in unavailable_9_afternoon.split(",") if i != ""]
        unavailable_9_all = str(detailsform.unavailable_9_all.data)
        unavailable_9_all = [int(i) for i in unavailable_9_all.split(",") if i != ""]
        if name_9 != "":
            names[name_9] = {}
            for i in unavailable_9_morning:
                names[name_9].update({i: ["Morning_1", "Morning_2"]})
            for i in unavailable_9_afternoon:
                names[name_9].update({i: ["Afternoon & Night"]})
            for i in unavailable_9_all:
                names[name_9].update({i: ["Morning_1", "Morning_2", "Afternoon & Night"]})

        # print(names)

        # while("" in names):
        #     names.remove("")

        calendar_gen = ShiftGenerator(days_in_month, start_day, names).random_shift()

        # return render_template("result.html",
        #                        detailsform=detailsform,
        #                        calendar_show=calendar_gen.to_html(classes='data', header=True))
        return render_template("result.html", tables=[calendar_gen[0].to_html(index=False, classes='data', header=True)],
                               report_morning=calendar_gen[1], report_afternoon=calendar_gen[2], report_weekend=calendar_gen[3] )


class DetailsForm(Form):

    days_in_month = StringField("Total days in a month: ", default=31)
    start_day = StringField("First day of the month: ", default="Mon")

    name_1 = StringField("Staff Name 1: ", default="A")
    unavailable_1_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_1_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_1_all = StringField("Unavailable date - All day: ", default=None)

    name_2 = StringField("Staff Name 2: ", default="B")
    unavailable_2_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_2_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_2_all = StringField("Unavailable date - All day: ", default=None)

    name_3 = StringField("Staff Name 3: ", default="C")
    unavailable_3_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_3_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_3_all = StringField("Unavailable date - All day: ", default=None)

    name_4 = StringField("Staff Name 4: ", default="D")
    unavailable_4_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_4_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_4_all = StringField("Unavailable date - All day: ", default=None)

    name_5 = StringField("Staff Name 5: ", default="E")
    unavailable_5_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_5_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_5_all = StringField("Unavailable date - All day: ", default=None)

    name_6 = StringField("Staff Name 6: ", default="F")
    unavailable_6_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_6_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_6_all = StringField("Unavailable date - All day: ", default=None)

    name_7 = StringField("Staff Name 7: ", default="G")
    unavailable_7_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_7_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_7_all = StringField("Unavailable date - All day: ", default=None)

    name_8 = StringField("Staff Name 8: ", default="H")
    unavailable_8_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_8_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_8_all = StringField("Unavailable date - All day: ", default=None)

    name_9 = StringField("Staff Name 9: ", default="I")
    unavailable_9_morning = StringField("Unavailable date - Morning: ", default=None)
    unavailable_9_afternoon = StringField("Unavailable date - Afternoon: ", default=None)
    unavailable_9_all = StringField("Unavailable date - All day: ", default=None)

    button = SubmitField("Generate")


class ResultPage(MethodView):
    def get(self):
        return render_template('result.html')

port = int(os.environ.get('PORT', 8000))

app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/shift_form',
                 view_func=DetailFormPage.as_view('shift_form'))
app.add_url_rule('/result',
                 view_func=ResultPage.as_view('result_page'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)