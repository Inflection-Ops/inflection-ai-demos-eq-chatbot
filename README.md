# Python Chatbot with Inflection AI Pi Model

This repository contains a Python-based chatbot that uses Inflection AI Pi for conversation. The chatbot also analyzes the sentiment and tone of the user's messages and displays them using cool graphics.

## Running the Chatbot Locally

### Prerequisites

- Python 3.12
- To run this application you will need an **Inflection AI Developers Account** and an API key. Follow these steps to get started:

1️⃣ **Sign Up & Get Your API Key** 🔑  
👉 [Sign up here](https://developers.inflection.ai/login) using Google or GitHub.  
👉 Navigate to the **API Keys** section and create a new key. 

2️⃣ **Read the API Docs** 📖  
👉 Check out the official [Inflection AI API Docs](https://developers.inflection.ai/docs) and [Cookbook](https://github.com/Inflection-Ops/inflection-ai-cookbook/) to understand usage and best practices.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Inflection-Ops/inflection-ai-demos-eq-chatbot.git
    cd inflection-ai-demos-eq-chatbot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3.12 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a .env file and asign your key to INFLECTION_API_KEY:
    ```sh
    BASE_URL=https://layercake.pubwestus3.inf7ks8.com
    INFLECTION_API_KEY=XXXXX
    ```

5. Run the Flask application:
    ```sh
    python app.py
    ```

6. Open your web browser and go to `http://localhost:5000` to start chatting with the bot.

## Running the Chatbot in Docker

### Prerequisites

- Docker

### Building the Docker Image

1. Clone the repository:
    ```sh
    git clone https://github.com/Inflection-Ops/inflection-ai-demos-eq-chatbot.git
    cd inflection-ai-demos-eq-chatbot
    ```

2. Build the Docker image:
    ```sh
    docker build -t python-pi-chatbot .
    ```

### Running the Docker Container

1. Run the Docker container:
    ```sh
    docker run -it -p 5050:5050 python-pi-chatbot
    ```

2. Open your web browser and go to `http://localhost:5000` to start chatting with the bot.

## Running the deployed chatbot remotely
The chatbot is available temporarily on the web through this [link](https://inflection-ai-demos-eq-chatbot.onrender.com) 

## Dependencies

- Flask==3.1.0
- openai==0.10.2
- requests==2.25.1
- python_dotenv
