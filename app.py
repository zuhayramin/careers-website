from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Riyadh, KSA',
        'salary': 'SR 70,000' 
    },
    {
        'id':2,
        'title': 'Frontend Engineer',
        'location': 'Dubai, UAE',
        'salary': 'AED 190,000' 
    },
    {
        'id':3,
        'title': 'Full Stack Developer',
        'location': 'Paris, France',
        'salary': 'Euro 50,000' 
    },
    {
        'id':4,
        'title': 'DevOps Engineer',
        'location': 'Stockholm, Sweden',
        'salary': 'Euro 320,000' 
    }
]

@app.route('/')
def index():
    return render_template('home.html', jobs =JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)