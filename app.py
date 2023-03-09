import os
import traceback

import yaml
from flask import Flask, request, make_response, jsonify, render_template

from letter_util import compile_letter
from template import prepare_template

app = Flask(__name__, template_folder='html')


@app.route('/')
def index():
    folder_path = './templates'
    files = [os.path.splitext(f)[0] for f in os.listdir(folder_path)]
    return render_template('index.html', title='lettergirl', files=files)


@app.route('/details', methods=['GET'])
def details():
    filename = request.args.get('filename')
    dfsakjhkl = f"templates/{filename}.yaml"
    with open(dfsakjhkl, "r", encoding="utf-8") as file:
        # Load the YAML data
        template = yaml.safe_load(file)
    # display the form
    return render_template('/form.html', name=template['metadata']['name'], params=template["params"], file=dfsakjhkl)


@app.route('/generate-letter', methods=['POST'])
def generate_letter():
    data = request.form.to_dict()
    try:
        template = prepare_template(data["filename"], data)
    except Exception as e:
        traceback.print_exc()
        # return abort(400, str(e))
        return jsonify({'error': str(e)}), 400

    pdf_bytes = compile_letter(template)

    # Set the content type to PDF and the content disposition to inline
    response = make_response(pdf_bytes)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=letter.pdf'

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
