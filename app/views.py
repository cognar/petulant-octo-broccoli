from flask import render_template, request
from app import app
from random import randint
from SudSolve import sudoku as solveSud

@app.route('/')
@app.route('/index')
def index():
    title = 'oh shit'
    ran = [str(randint(0,9)) for i in range(20)]
    return render_template('index.html',
                           title=title)

@app.route('/fuck')
def fuck():
    return 'fuck you'

@app.route('/sudoku')
def sudoku():
    return render_template('sudoku.html',
                            title='sudoku',
                            n=9,
			    backgroundColor = ['FFFFE1', 'C4C9BB'])
@app.route('/sudoku', methods=['POST'])
def solveSudoku():
    numbers = ''.join([request.form[str(i)] for i in range(1,82)])
    return solveSud(numbers)
