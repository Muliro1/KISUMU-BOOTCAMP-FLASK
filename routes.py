from flask import Flask, render_template, url_for, flash, redirect, request, session

app = Flask(__name__)



@app.route('/api/v1/register', methods = ['GET', 'POST'])
def register():
	'''
	This view function displays a registration form for users to register a new account
	'''
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)