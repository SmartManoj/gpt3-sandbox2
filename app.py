import os
from flask import Flask, request, render_template
from gpt import set_openai_key, GPT, Example
KEY_NAME = "OPENAI_KEY"

app = Flask(__name__)
set_openai_key(os.environ[KEY_NAME])

@app.route('/')
def index():
    return render_template('index.html',title=title,context=context)

@app.route('/query', methods=['POST'])
def request_query():
    query = request.form['query']
    response = gpt.submit_request(query)
    return {'text': response['choices'][0]['text'][7:]}             



title = 'Simple Math'
context = 'The following is a conversation with a math assistant.'

examples={
'5+5':'Ten',
'5+6':'Eleven'
}

gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100,
          context=context)

gpt.add_examples(examples)


if __name__ == "__main__":
    app.run(debug=1)