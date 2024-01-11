from flask import Flask, render_template, request

from translator import translate_to_en
from sentiment import is_good, calc_sentiment_score


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    adj = None
    score = -99

    if request.method == 'POST':
        adj = request.form.get('adj')
        score = calc_sentiment_score(translate_to_en(f'Gleiciane é {adj}'))

    return render_template('index.html', adj=adj, score=score, is_good=is_good, translate_to_en=translate_to_en)


@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)