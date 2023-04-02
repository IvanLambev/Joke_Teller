from flask import *
import requests
import json
app = Flask(__name__)


def joke_fetcher():

    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

@app.route('/', methods=['GET', 'POST'])
def main_page():  # put application's code here

 #make it so that the joke is only fetched when the button is pressed and not on page load and display it on the page in a nice way
    if request.method == 'POST':
        return render_template('index.html', joke=joke_fetcher())
    else:
        return render_template('index.html')


@app.route('/joke')
def joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = response.json()
    return jsonify({'joke': data['setup'] + ' ' + data['punchline']})

if __name__ == '__main__':
    app.run()




if __name__ == '__main__':
    app.run()
