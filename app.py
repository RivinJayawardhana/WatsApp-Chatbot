from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from flask_cors import CORS




app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/bot', methods=['POST'])
def bot():
    try:
        # Log headers for debugging
        print("Headers:", request.headers)
        print("Form Data:", request.form)

        # Extract message and sender
        incoming_message = request.form.get('Body', '').lower()
        sender = request.form.get('From', 'Unknown')
        print(f"Incoming Message: {incoming_message}, Sender: {sender}")

        # Rule-based responses
        if 'hello' in incoming_message:
            response_text = "Hi! How can I assist you today?"
        elif 'pricing' in incoming_message:
            response_text = "Our pricing plans are available at: https://example.com/pricing"
        else:
            response_text = "Sorry, I didn't understand that. Please type 'help' for options."

        # Create Twilio response
        resp = MessagingResponse()
        resp.message(response_text)

        return str(resp)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
