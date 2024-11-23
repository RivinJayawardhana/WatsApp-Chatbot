from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Optional: Enable cross-origin requests

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    try:
        # Parse incoming message
        incoming_message = request.form.get('Body', '').lower()
        sender = request.form.get('From', 'Unknown')

        # Log for debugging
        print(f"Incoming Message: {incoming_message}, Sender: {sender}")

        # Rule-based responses
        response_text = "Sorry, I didn't understand that. Type 'help' for options."
        if 'hello' in incoming_message:
            response_text = "Hi! How can I assist you today?"
        elif 'pricing' in incoming_message:
            response_text = "Our pricing details are available at: https://example.com/pricing"
        elif 'help' in incoming_message:
            response_text = (
                "Here are some options:\n"
                "- Type 'hello' to start a conversation.\n"
                "- Type 'pricing' for our pricing details.\n"
                "- Type 'contact' to reach customer support."
            )
        elif 'contact' in incoming_message:
            response_text = "You can contact us at support@example.com or call +123456789."

        # Generate Twilio response
        resp = MessagingResponse()
        resp.message(response_text)

        return str(resp)
    except Exception as e:
        print(f"Error: {e}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
