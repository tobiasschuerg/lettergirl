import subprocess


def compile_letter(tex_template: str) -> bytes:
    """
    Compile the letter using pdflatex
    :param tex_template: tex file
    :return: pdf as bytes
    """
    with open('letter_temp.tex', 'w', encoding="utf-8") as f:
        f.write(tex_template)
    subprocess.run(['pdflatex', 'letter_temp.tex'], check=True)
    # Read the generated PDF file and return it as a response
    with open('letter_temp.pdf', 'rb') as f:
        pdf_bytes = f.read()
    return pdf_bytes
