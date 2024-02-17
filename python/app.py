from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
client = OpenAI(
    api_key="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",
)

# Define a route to handle questions
@app.route('/ask', methods=['POST'])
def ask_question():
    # Get the question from the request data
    question = request.json.get('question')
    conversation = []
    # Call the OpenAI API to generate an answer
    conversation.append({"role": "user", "content": question})
    completion = client.chat.completions.create(
      model="gpt-4",
      messages=conversation
    )
    # print(q)
    answer = completion.choices[0].message.content

    # Return the answer as JSON
    return jsonify({'answer': answer})

@app.route('/ask', methods=['OPTIONS'])
def handle_preflight():
    # Add any necessary headers to the response
    response = jsonify({'message': 'Preflight request received'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response

if __name__ == '__main__':
    app.run(debug=True)
