import dill
import numpy as np
import xgboost as xgb
from flask import Flask, render_template, request
import random
import string

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = dill.load(vectorizer_file)

with open('xgb_classifier.pkl', 'rb') as classifier_file:
    classifier = dill.load(classifier_file)

app = Flask(__name__)


def suggest_stronger_password(user_input):
    suggestions = []

  
    for _ in range(5):
        suggestion = list(user_input)
        special_chars = '!@#$%&*'
        digits = '1234567890'

       
        for i in range(len(suggestion)):
            transformation_type = random.randint(1, 3)

            if transformation_type == 1:
                if suggestion[i].isalpha():
                    suggestion[i] = random.choice(suggestion[i].upper() + suggestion[i].lower())
            elif transformation_type == 2:
                suggestion.insert(i, random.choice(special_chars + digits))
            elif transformation_type == 3:
                suggestion[i] = suggestion[i].upper()

        password = ''.join(suggestion)[:10]  
        suggestions.append(password)

    return suggestions

def predict_class_and_probability(user_input):
    if user_input.isdigit():
        return 0, 0.0  


    user_input_vector = vectorizer.transform([user_input])


    predicted_class = classifier.predict(user_input_vector)
    predicted_probability = classifier.predict_proba(user_input_vector)[0][predicted_class[0]]

    return predicted_class[0], predicted_probability

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        if len(user_input) < 8:
            result = "Password must be at least 8 characters."
            color = "red"
            suggestions = []
        else:
            predicted_class, predicted_probability = predict_class_and_probability(user_input)
            if predicted_class == 0:
                result = "Weak"
                color = "red"
                suggestions = suggest_stronger_password(user_input)
            elif predicted_class == 1:
                result = "Medium"
                color = "orange"
                suggestions = suggest_stronger_password(user_input)
            else:
                result = "Strong"
                color = "green"
                suggestions = []
        return render_template('index.html', result=result, color=color, suggestions=suggestions)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
