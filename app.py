from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from googlesearch import search

app = Flask(__name__)  # creates an instance of the flask app

# route for handling incoming messages from Twilio
@app.route("/", methods=["POST"])  # Twilio will send messages to this route
def bot():
    # Create a Twilio MessagingResponse object
    response = MessagingResponse()

    # Extract the user's message from the incoming request
    user_msg = request.values.get('Body', '').lower()

    # Respond to "hello" or "hi"
    if user_msg == "hello" or user_msg == "hi":
        msg = response.message("Hello Anthony, what's up?")
    else:
        # Append "geeksforgeeks.org" to the user's message and search for it
        q = user_msg + " geeksforgeeks.org"
        search_results = [result for result in search(q, num_results=5)]

        # Add a header message
        response.message(f"--- Results for '{user_msg}' ---")

        # Loop and send each URL as a separate message
        for result in search_results:
            response.message(result)

    # Send the response back to Twilio
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
    