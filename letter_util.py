import subprocess
from pathlib import Path


def compile_letter(tex_template: str) -> bytes:
    """
    Compile the letter using pdflatex
    :param tex_template: tex file
    :return: pdf as bytes
    """
    temp_tex_file = Path("out/letter_temp.tex")
    temp_tex_file.parent.mkdir(exist_ok=True, parents=True)
    with open(temp_tex_file, "w", encoding="utf-8") as f:
        f.write(tex_template)
    subprocess.run(["pdflatex", "letter_temp.tex"],
                   check=True,
                   cwd=temp_tex_file.parent)
    # Read the generated PDF file and return it as a response
    with open(temp_tex_file.with_name("letter_temp.pdf"), "rb") as f:
        pdf_bytes = f.read()
    return pdf_bytes
