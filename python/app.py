from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS  # Import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
app.secret_key = 'your_secret_key'

OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)


@app.route('/api/components', methods=['GET'])
def get_components():
    project_name = request.args.get('projectName', '').lower()
    budget = int(request.args.get('budget', 0))

    # Adjust the path to where your Excel file is stored
    df = pd.read_excel("./robotics_projects_cost_expanded.xlsx")

    # Filter based on project name and budget
    filtered_df = df[(df['Project Name'].str.lower().str.contains(project_name)) & 
                     (df['Total Cost (BDT)'] <= budget)]

    # Convert to list of dicts
    components = filtered_df[['Component Name', 'Total Cost (BDT)']].to_dict(orient='records')

    return jsonify(components)


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

# @app.after_request
# def add_security_headers(resp):
#     resp.headers['Access-Control-Allow-Origin']='*'
#     resp.headers['Access-Control-Allow-Methods']='GET, POST, PUT, OPTIONS'
#     resp.headers["Access-Control-Allow-Headers"]="Access-Control-Request-Headers,Access-Control-Allow-Methods,Access-Control-Allow-Headers,Access-Control-Allow-Origin, Origin, X-Requested-With, Content-Type, Accept"
#     return resp


if __name__ == '__main__':
    app.run(debug=True)