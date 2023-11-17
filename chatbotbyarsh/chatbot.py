from flask import Flask, render_template, request

app = Flask(__name__)

cta_elements = {
    "Welcome": "Welcome! Feel free to ask me anything.",
    "Options": "You can ask:\n1. What is your name?\n2. How can you help?",
    "Goodbye": "Goodbye! If you have more questions, feel free to ask."
}

def respond_to_action(action):
    if action.lower() == "what is your name?":
        return "I am a magical bot."
    elif action.lower() == "how can you help?":
        return "Hey, I can provide information and answer questions. Just ask!"
    else:
        return "I'm not sure how to respond to that. Please choose from the options."

@app.route('/')
def index():
    return render_template('index.html', welcome_message=cta_elements["Welcome"])

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    if "exit" in user_input.lower():
        return cta_elements["Goodbye"]

    response = respond_to_action(user_input)
    return render_template('index.html', welcome_message=cta_elements["Options"], user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)
