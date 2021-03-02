import os
from datetime import datetime

import pytz
from flask import Flask, request

app = Flask(__name__)
path = "/SecondYearDoneCurses/PythonJava(InternetOfThings)/list1/python/times"
os.chdir(path)


@app.route('/time', methods=['GET'])
def get_time():
    tz = request.args.get('tz')
    return datetime.now(tz=pytz.timezone(tz)).__str__()


@app.route('/mqtt', methods=['POST'])
def post_time():
    length = 1
    for root, dirs, names in os.walk(path):
        length = len(names)
    time = request.get_data()
    print(str(time))
    file = open("time_{}.json".format(length + 1), "w")
    file.write(str(time))
    return "success"


app.run(port=5002)
