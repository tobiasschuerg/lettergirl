FROM python:3.9.16

RUN apt-get update && apt-get install -y \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-lang-german \
    texlive-latex-base \
    texlive-latex-extra \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
