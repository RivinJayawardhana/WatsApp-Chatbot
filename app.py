from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get incoming message details
        incoming_message = request.form.get('Body', '').lower()
        sender = request.form.get('From')

        # Rule-based responses
        if 'hello' in incoming_message:
            response_text = "Hi! How can I assist you today?"
        elif 'pricing' in incoming_message:
            response_text = "Our pricing plans are available at: https://example.com/pricing"
        else:
            response_text = "Sorry, I didn't understand that. Please type 'help' for options."

        # Create a Twilio MessagingResponse
        resp = MessagingResponse()
        resp.message(response_text)

        return str(resp)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
