from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="/encrypt" method="post">
            <b>Rotate by:</b> <input type="text" name="rot" value="0"><br>
            <textarea name="text">{0}</textarea>
            <input type="submit">
        </form>
    </body>
</html>
"""


@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    rotation = int(rotation)
    message = request.form['text']
    message = str(message)
    encrypted = rotate_string(message, rotation)
    return form.format(encrypted)
    #return '<h1>' + encrypted + '</h1>'

@app.route("/")
def index():
    return form.format("")


app.run()