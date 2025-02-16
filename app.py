import os
import json
from flask import Flask, render_template, request, jsonify
import asyncio
from dotenv import load_dotenv
from utils import get_context, get_response

# load .env file
load_dotenv()
# Set up OpenAI API key


system_instruction_prompt = """
You are a helpful chatbot. When given a user input, provide a conversation reply 
and also analyze the user's input to detect two things: the emotion and the tone. 

# Output Format (XML):
You will respond in a valid XML format with the <parts>, <reply>, <emotion> and <tone> tags following below output format. 
You don't need to provide explanation or any other information, just return reply, emotion and tone.
- reply: for the conversational response.
- emotion: for the detected emotion.
- tone: for the detected tone.

# Format of the Output
<parts>
    <reply>The reply to the user message</reply>
    <emotion>The emotion of the user based on their message</emotion>
    <tone>The tone of the user based on their message</tone>
</parts>

"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    # Prepare instruction for Inflection AI.
    context = get_context(system_instruction_prompt, user_message)
    
    try:
        reply, emotion, tone = asyncio.run(fetch_response(context))
        
        return jsonify({"reply": reply, "emotion": emotion, "tone": tone})
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "An error occurred. Please try again.", "emotion": "Unknown", "tone": "Unknown"})

async def fetch_response(context):
    result = await get_response(context, ["reply", "emotion", "tone"])
    reply = result["reply"]
    emotion = result["emotion"]
    tone = result["tone"]
    return reply,emotion,tone

if __name__ == '__main__':
    app.run(debug=True)
