FROM python:3.9.16

RUN apt-get update && apt-get install -y \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-lang-german \
    texlive-latex-base \
    texlive-latex-extra \
    && rm -rf /var/lib/apt/lists/*

RUN pip install flask
RUN pip install PyYAML

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
