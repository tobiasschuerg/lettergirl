import yaml
from flask import Flask, request, make_response, abort, jsonify

from letter_util import compile_letter
from template import prepare_template

app = Flask(__name__)


@app.route('/generate-letter', methods=['POST'])
def generate_letter():
    data = yaml.safe_load(request.data)
    try:
        template = prepare_template(r"templates/kündigung_vodafone.yaml", data)
    except Exception as e:
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
