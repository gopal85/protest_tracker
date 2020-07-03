from flask import Flask
from flask import render_template
from flask import request
import model

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        user_zip = dict(request.form)
        print(user_zip)
        protest_guide = {
          {"date": "July 4, 2020", "time": "5:00—7:00 pm", "location" : "Grand Army Plaza", "leadership": "BLM"},
          {"date": "July 7, 2020", "time": "6:00—9:00 pm", "location" : "McCarren Park", "leadership": "SURJ"},
          {"date": "July 10, 2020", "time": "9:00 am—9:00 pm", "location" : "Prospect Park", "leadership": "NAACP"},
          {"date": "July 12, 2020", "time": "4:00—8:00 pm", "location" : "Coney Island", "leadership": "Color of Change"}
        }
        protestInfo = model.events(protest_guide)
        return render_template("index.html", protestInfo = protestInfo)
        # user_zip = dict(request.form)
        # print(user_zip)
        # find_protest = model.events()
        # date = find_protest["date"][1]
        # time = find_protest["time"][1]
        # location = find_protest["location"][1]
        # leadership = find_protest["leadership"][1]
        # return render_template("index.html", date=date, time=time, location=location, leadership=leadership)
    else:
        return render_template("index.html")