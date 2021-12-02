from typing import re
import re

from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST' and 'search'in request.form:
        search = request.form.get('search')
        if xxs_attack_validation(search) is False:
            return render_template('empty.html', search_term=search)
        else:
            return render_template('main.html', )
    return render_template('main.html')



def xxs_attack_validation(text):
    regrex = re.compile('[#%&*()<>/\|}{~:]')
    if regrex.search(text) is None:
        return False
    else:
        return True
if __name__ == '__main__':

    import os
    HOST = os.environ.get('SEVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SEVER_PORT', '5555'))
    except:
        PORT = 5555
    app.run(HOST, PORT)