#!/bin/bash

# Get the subject and body from the command line arguments
subject=$1
body=$2

# Replace placeholders in the LaTeX template with the subject and body
sed "s/\$subject/$subject/g" app/letter.tex | sed "s/\$body/$body/g" > letter_temp.tex

# Compile the letter using pdflatex
pdflatex letter_temp.tex

