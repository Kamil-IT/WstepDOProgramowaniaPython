import json

from flask import Flask

app = Flask(__name__)


class Window:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.busy = False

    def to_dictionary(self):
        return {
            "name": str(self.name),
            "type": str(self.type),
            "petitioner": str(self.busy),
        }


windows = [Window('A', [1]), Window('B', [1]), Window('C', [1, 2]), Window('D', [2])]


@app.route('/window/<id>', methods=['GET'])
def get(id):
    return json.dumps(windows[int(id)].to_dictionary())


@app.route('/window/<id>', methods=['POST'])
def post(id):
    windows[int(id)].busy = False
    return "success"


@app.route('/petitioner/add/<type>', methods=['POST'])
def post_add_to_window(type):
    for window in windows:
        if (int(type) in window.type) and (window.busy == False):
            window.busy = True
            return "success"
    return "all window busy", 404


@app.route('/window/busy', methods=['GET'])
def get_busy():
    sum_ = 0
    for window in windows:
        if window.busy:
            sum_ += 1
    if sum_ == 0:
        return str(sum_), 404
    return str(sum_)


if __name__ == '__main__':
    app.run()
