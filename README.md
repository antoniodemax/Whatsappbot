# 📱 WhatsApp Bot with Flask and Twilio

This project is a lightweight WhatsApp chatbot built with **Flask**, **Twilio**, and the **Google Search API**. The bot interacts with users over WhatsApp by providing personalized greetings and returning Google search results based on user queries.

---

## ✨ Features

* 🤖 Responds to greetings like `"hello"` or `"hi"` with a friendly message.
* 🔍 Performs Google searches for user-provided queries.
* 📩 Returns the top 5 relevant search results via WhatsApp.
* 🔧 Utilizes Twilio's API for managing WhatsApp message interactions.

---

## 📋 Prerequisites

Ensure the following tools and services are installed and configured before running the project:

* Python 3.7 or higher
* `pip` (Python package manager)
* A Twilio account with WhatsApp Sandbox access
* [`ngrok`](https://ngrok.com/) for exposing your local server to the internet

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Whatsappbot.git
cd Whatsappbot
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask App

```bash
python app.py
```

### 5. Expose Your Local Server Using ngrok

In a new terminal window, run:

```bash
ngrok http 5000
```

Copy the HTTPS forwarding URL provided by ngrok (e.g., `https://a378-105-29-165-234.ngrok-free.app`).

---

## 🔧 Twilio Webhook Configuration

1. Log in to your Twilio Console.
2. Navigate to **Messaging > Try it Out > Send a WhatsApp message**.
3. Set the **Webhook URL** to your `ngrok` forwarding address, e.g.:

```
https://a378-105-29-165-234.ngrok-free.app/
```

4. Save your settings.

---

## 🚀 Usage

* Send a WhatsApp message to your Twilio sandbox number.
* If the message is `"hello"` or `"hi"`, you'll receive a personalized response.
* For any other input, the bot will perform a Google search and reply with the top 5 results.

---

## 📁 Project Structure

```
Whatsappbot/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (Twilio credentials, etc.)
└── README.md               # Project documentation
```

---

## 🛠 Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'twilio'`
**Solution:** Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

---

**Issue:** Flask app not accessible
**Solution:** Make sure `ngrok` is running and the correct forwarding URL is set in your Twilio webhook.

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute it as needed.
Please note that this is a basic implementation and may require additional setup for production use.