from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))  # For session management

# Configure Google Gemini API
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Enhanced rate limiting
REQUESTS_PER_MINUTE = 60
REQUESTS_PER_DAY = 1000
request_timestamps = []
daily_requests = {}

def check_rate_limit():
    current_time = time.time()
    current_date = datetime.now().date()
    
    # Check daily limit
    if current_date not in daily_requests:
        daily_requests.clear()  # Reset for new day
        daily_requests[current_date] = 0
    
    if daily_requests[current_date] >= REQUESTS_PER_DAY:
        return False, "Daily limit exceeded"
    
    # Check per-minute limit
    while request_timestamps and current_time - request_timestamps[0] > 60:
        request_timestamps.pop(0)
    
    if len(request_timestamps) >= REQUESTS_PER_MINUTE:
        return False, "Rate limit exceeded"
    
    request_timestamps.append(current_time)
    daily_requests[current_date] += 1
    return True, None

def create_empathetic_prompt(user_message, conversation_history=None):
    system_prompt = """You are an empathetic and understanding friend. Your role is to:
    1. Listen carefully and show genuine understanding
    2. Respond with emotional support and validation
    3. Offer gentle guidance when appropriate
    4. Maintain a warm, non-judgmental tone
    5. Ask thoughtful follow-up questions to show you care
    6. Remember and reference previous parts of the conversation
    7. Be concise but meaningful in responses
    
    Keep responses focused and authentic.
    Maintain appropriate boundaries while being supportive."""
    
    # Include conversation history for context
    context = ""
    if conversation_history:
        context = "Previous conversation:\n" + "\n".join(conversation_history[-3:]) + "\n\n"
    
    return f"{system_prompt}\n\n{context}User: {user_message}\nResponse:"

@app.route('/')
def home():
    # Initialize session if needed
    if 'conversation_history' not in session:
        session['conversation_history'] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Rate limiting check
        rate_limit_ok, limit_message = check_rate_limit()
        if not rate_limit_ok:
            return jsonify({'error': limit_message}), 429

        user_message = request.json.get('message', '').strip()
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Message length validation
        if len(user_message) > 500:
            return jsonify({'error': 'Message too long. Please keep it under 500 characters.'}), 400

        # Get conversation history from session
        conversation_history = session.get('conversation_history', [])
        
        # Create prompt with context
        prompt = create_empathetic_prompt(user_message, conversation_history)
        
        # Enhanced safety settings
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
        ]
        
        # Generate response with improved configuration
        response = model.generate_content(
            prompt,
            safety_settings=safety_settings,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.8,
                "top_k": 40,
                "max_output_tokens": 200,
                "stop_sequences": ["User:", "\n\n"]
            }
        )
        
        if not response or not response.text:
            return jsonify({'error': 'Empty response from API'}), 500
        
        # Update conversation history
        conversation_history.append(f"User: {user_message}")
        conversation_history.append(f"Bot: {response.text}")
        # Keep only last 10 exchanges
        conversation_history = conversation_history[-10:]
        session['conversation_history'] = conversation_history
            
        return jsonify({
            'response': response.text,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        error_message = str(e)
        logger.error(f"Error in chat endpoint: {error_message}", exc_info=True)
        
        # Enhanced error handling
        if "quota" in error_message.lower():
            return jsonify({'error': 'API quota exceeded. Please try again later.'}), 429
        elif "rate" in error_message.lower():
            return jsonify({'error': 'Too many requests. Please wait a moment.'}), 429
        elif "invalid" in error_message.lower() and "key" in error_message.lower():
            return jsonify({'error': 'Invalid API key. Please check your configuration.'}), 401
        elif "timeout" in error_message.lower():
            return jsonify({'error': 'Request timed out. Please try again.'}), 504
        
        return jsonify({'error': 'An unexpected error occurred. Please try again.'}), 500

@app.route('/clear-history', methods=['POST'])
def clear_history():
    session['conversation_history'] = []
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)



