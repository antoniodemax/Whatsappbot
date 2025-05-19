from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from gogglesearch import search

app = Flask(__name__) #creates an instance of the flask 

# route for handling incoming messages from Twilio
@app.route("/", methods=["POST"]) #twilio will send message to this route
def bot():

    # extracts the users message from the incoming request. body contains the message text
    user_msg = request.values.get('Body', '').lower()


    # if the user message is empty, return a default response
    if not user_msg:
        return "Please send a message."
    else:
        print(user_msg)
    response = MessagingResponse()

    # appends "geeksforgeeks.org" to the user message and searches for it
    # using the search function from the googlesearch module
    q = user_msg + " geeksforgeeks.org"
    search_results = []

    for i in search(q, num_results=5):
        search_results.append(i)

    msg = response.message(f"--- Results for '{user_msg}' ---")

    # loops and sends each url as a separate message to the user
    for result in search_results:
        msg = response.message(result)

    # sends the response back to Twilio
    # Twilio will send the response to the user
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)