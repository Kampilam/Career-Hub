from flask import Flask,render_template

app = Flask(__name__)

Jobs =[
  {"Company":"Lotus Tech Company",
   "Title":"Junior Software Developer",
   "Location":"Hyderabad, India",
   "Salary":"Rs. 6 LPA"
},
  {"Company":"Giant PVT Limited",
   "Title":"Java Developer",
   "Location":"Banglore, India",
   "Salary":"Rs. 10 LPA"
},
{"Company":"Weekeeden",
   "Title":"Data Analyst",
   "Location":"Hyderabad, India",
   "Salary":"Rs. 4 LPA"
},
{"Company":"Den Markets",
   "Title":"Data Science",
   "Location":"Chennai, India",
   "Salary":"Rs. 12 LPA"
},
{"Company":"Derive Content",
   "Title":"AI Prompt Generator",
   "Location":"Kolkatta, India",
   "Salary":"Rs. 3 LPA"
},
]


@app.route("/")
def career_hub():
  return render_template("home.html")

@app.route("/jobs")
def jobs_career_hub():
  return render_template("jobs.html",jobs=Jobs)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
