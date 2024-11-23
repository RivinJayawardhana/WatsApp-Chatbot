from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Optional: Enable cross-origin requests

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    try:
        print("Headers:", request.headers)
        print("Form Data:", request.form)  # Logs incoming form data
        
        incoming_message = request.form.get('Body', '').lower()
        sender = request.form.get('From', 'Unknown')
        print(f"Incoming Message: {incoming_message}, Sender: {sender}")

        # Default response
        response_text = "Sorry, I didn't understand that. Type 'help' for options."
        if 'hello' in incoming_message:
            response_text = "Hi! How can I assist you today?"
        elif 'pricing' in incoming_message:
            response_text = "Our pricing details are at https://example.com/pricing"
        elif 'help' in incoming_message:
            response_text = "Options: Type 'hello' or 'pricing'."

        resp = MessagingResponse()
        resp.message(response_text)
        return str(resp)
    except Exception as e:
        print(f"Error: {e}")
        return "Internal Server Error", 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
