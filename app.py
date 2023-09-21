from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data analyst",
    "location": "Kratie, Cambodia",
    "Salary": "800$"
  },
  {
    "id": 2,
    "title": "Data Science",
    "location": "Phnom Penh, Cambodia",
    "Salary": "1600$"
  },
  {
    "id": 3,
    "title": "Software Developer",
    "location": "Siem Reap, Cambodia",
    "Salary": "500$"  
  },
  {
    "id": 4,
    "title": "Cyber Security",
    "location": "Sihanouk Vile, Cambodia",
    "Salary": "450$"
  }]


@app.route("/")
def hello_world():
  return render_template('home.html', Job = JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
