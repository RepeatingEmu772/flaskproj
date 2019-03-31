from flask import Flask,render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def idk():
	return render_template("index1.html",now)

@app.route("/dada")
def hello():
	print(request.args)
	naam = 'manan'
	data = [['Name','isAwesome','Spreadingfrom'],
			['Manan',True,2002],
			['dada',False, 9000]]
	color= ['red','blue','green']
	return render_template('index1.html', name = naam,
		now=datetime.now().strftime("%d %B,%y %I:%M %p")
		,data=data,colors=color)

@app.route("/form", methods=['GET','POST'])
def submit():
	if request.method=='GET':
		return render_template('form.html')
	else:
		print(request.form)
		name = request.form.get('name')
		trump = request.form.get('trump')
		image = request.files.get('image')
		ext = image.filename.split('.')[-1]
		image.save('static/images/{}.{}'.format(name,ext))
		return '''YOU WONT GET KILLED!!,btw whose 
		name is {} and when some one says u like trump 
		you say {}...imma suprised'''.format(name,trump)

if __name__ == "__main__":
	app.run(use_reloader=True, port=4747, debug=True)