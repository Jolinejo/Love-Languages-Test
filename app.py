from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

questions = [
  {"question": "You're feeling stressed. Your partner offers to:",
   "options": ["A: Give you a massage and melt your worries away",
                "B: Whip up your favorite meal and listen patiently"]},

  {"question": "A thoughtful gesture that would melt your heart:",
   "options": ["A: A sweet note tucked into your bag, reminding you they care",
                "B: A small, unexpected gift that shows they know you well"]},

  {"question": "Your phone buzzes. It's your partner. What message makes you smile most?",
   "options": ["A: 'Thinking of you and how much you brighten my day!'",
                "B: 'Just grabbed tickets to that concert you mentioned!'"]},

  {"question": "What's your favorite way to connect with someone?",
   "options": ["A: Spending quality time, sharing stories and laughter",
                "B: A comforting hug or cuddle that says everything without words"]},

  {"question": "Imagine a perfect weekend getaway. Would you choose:",
   "options": ["A: A cozy cabin retreat with uninterrupted conversations",
                "B: A spontaneous trip filled with exciting activities"]},

  {"question": "How do you show someone you appreciate them?",
   "options": ["A: Lending a helping hand with a chore or errand",
                "B: Giving them a heartfelt compliment or word of encouragement"]},

  {"question": "What makes you feel most secure in a relationship?",
   "options": ["A: Knowing your partner is always there for you, ready to help",
                "B: Regular 'I love you's and expressions of affection"]},

  {"question": "Imagine a perfect gift. Would it be:",
   "options": ["A: Something personalized that shows they put thought into it",
                "B: An experience you can share and create memories together"]},

  {"question": "After a long day, what lifts your spirits most?",
   "options": ["A: A listening ear",
                "B: A funny meme or message that makes you laugh"]},

  {"question": "What's your favorite way to unwind together?",
   "options": ["A: Snuggling on the couch, watching a movie",
                "B: Engaging in a stimulating conversation or game night"]},

  {"question": "Imagine you're feeling down. What would your partner do to cheer you up?",
   "options": ["A: Offer a shoulder",
                "B: Surprise you with a small gift or take you out for a treat"]},

  {"question": "How do you express your love most readily?",
   "options": ["A: Through physical affection, hugs, and kisses",
               "B: By giving thoughtful gifts that show you care"]},

  {"question": "What's your favorite way to show appreciation?",
   "options": ["A: Cooking a special meal or doing something helpful",
               "B: Writing a heartfelt note or giving a compliment"]},

  {"question": "You've had a long day. How does your partner cheer you up?",
   "options": ["A: Offering a comforting hug or cuddle",
               "B: Bringing you your favorite treat or small surprise"]},

  {"question": "How do you prefer to spend quality time together?",
   "options": ["A: Engaging in a shared hobby or activity",
               "B: Going on a spontaneous adventure or trip"]},

  {"question": "What gesture makes you feel most loved?",
   "options": ["A: Receiving a thoughtful gift that shows they understand you",
               "B: Spending uninterrupted time together, just talking or being together"]},

  {"question": "When you're feeling uncertain, what reassures you most?",
   "options": ["A: Physical gestures that demonstrate their commitment and support",
               "B: Verbal affirmations of love and encouragement"]}
]


# Define the scoring keys with corresponding tuples of (index, option)
scoring = {
    "Words of Affirmation": [(2, 'A'), (3, 'A'), (6, 'B'), (7, 'B'), (9, 'B'), (13, 'B'), (17, 'B')],
    "Acts of Service": [(1, 'B'), (3, 'B'), (5, 'B'), (6, 'A'), (7, 'A'), (13, 'A'), (15, 'B')],
    "Receiving Gifts": [(2, 'B'), (3, 'B'), (8, 'A'), (11, 'B'), (12, 'A'), (14, 'B'), (16, 'A')],
    "Quality Time": [(4, 'A'), (5, 'A'), (8, 'B'), (9, 'A'), (10, 'B'), (15, 'A'), (16, 'B')],
    "Physical Touch": [(1, 'A'), (4, 'B'), (10, 'A'), (11, 'A'), (12, 'A'), (14, 'A'), (17, 'A')]
}

@app.route('/')
def index():
    return render_template('quiz.html', questions=questions)

@app.route('/results', methods=['POST'])
def results():
    answers = request.form
    scores = {"Words of Affirmation": 0, "Acts of Service": 0, "Receiving Gifts": 0, "Quality Time": 0, "Physical Touch": 0}
    
    for i, answer in enumerate(answers.values(), start=1):
        for language, tuples in scoring.items():
            for index, correct_option in tuples:
                if i == index:
                    if answer == correct_option:
                        scores[language] += 1
    
    total_questions = len(questions)
    percentages = {language: (score / total_questions) * 100 for language, score in scores.items()}
    
    prominent_language = max(percentages, key=percentages.get)
    descriptions = {
        "Words of Affirmation": "You value verbal acknowledgements of affection, including frequent “I love you’s,” compliments, words of appreciation, and more.",
        "Acts of Service": "For you, actions speak louder than words. You feel loved when your partner helps you with tasks or takes care of things for you.",
        "Receiving Gifts": "You feel loved when you receive thoughtful gifts that show your partner was thinking of you.",
        "Quality Time": "You feel most loved when you have undivided attention from your partner and spend meaningful time together.",
        "Physical Touch": "Physical expressions of love, such as holding hands, hugging, and kissing, are important to you."
    }
    
    return render_template('results.html', percentages=percentages, prominent_language=prominent_language, description=descriptions[prominent_language], chart_data=json.dumps(percentages))

if __name__ == '__main__':
    app.run(debug=True)
