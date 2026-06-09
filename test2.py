from flask import Flask
import random
app = Flask(__name__)

facts_list = ["Most people suffering from technology addiction experience severe stress when they are out of network coverage or unable to use their devices.",
              "According to a survey conducted in 2018, over 50 per cent of people aged between 18 and 34 consider themselves dependent on their smartphones.",
              "The study of technological interdependencies is one of the most important areas of contemporary scientific research.",
              "According to a 2019 survey, over 60 per cent of people reply to work-related messages on their smartphones within 15 minutes of leaving work.",
              "One way to combat technology addiction is to look for activities that you enjoy and that lift your spirits.",
              "Elon Musk claims that social media platforms are designed to keep us on the platform so that we spend as much time as possible browsing content.",
              "Social media has its pros and cons, and we should be aware of them when using these platforms."]

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>' '<a href="/random_fact">Read an interesting fact!</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'


if __name__ == "__main__":
    app.run(debug=True)
