import os
import openai  
from dotenv import load_dotenv  
from flask import Flask, render_template, request, jsonify

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Load your API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

# Define a route for handling chatbot queries
@app.route("/ask", methods=["POST"])
def ask():
    try:
        # Get user query from the request
        user_query = request.form["message"]

        # Call the NLP API (e.g., OpenAI's GPT) to get a response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_query,
            max_tokens=50,  # Adjust as needed
            n=1,
            stop=None,  # Add any stop words to prevent continued generation
        )

        # Extract and return the generated response
        chatbot_response = response.choices[0].text.strip()

        return jsonify({"response": chatbot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
