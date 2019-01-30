from flask import Flask, render_template      ## render_template import 해줄 것

app = Flask(__name__)

@app.route('/')                    ##기본 페이지
def index():
    return '안녕하세요!!!'

@app.route('/html')                 ## /html 주소
def html():
    return render_template('chiken.html')      ## render_templates 를 통해 chiken.html로       
#chiken.html 페이지를 띄워주세요

@app.route('/html_name/<string:name>')
def html_name(name):
    return render_template('chiken.html', your_name = name)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    word_dict = {'apple':'사과', 'banana':'바나나'}
    return render_template('dictionary.html', word = word, word_dict = word_dict)

# if __name__ == "__main__":
#     app.run()

