#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Dependencies installed!"
echo "Running..."
python aula1.py
echo "Finished! Check 'relatorio.txt' file"
