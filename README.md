# Python Chatbot with OpenAI GPT-4

This repository contains a Python-based chatbot that uses OpenAI GPT-4 for conversation. The chatbot also analyzes the sentiment and tone of the user's messages and displays them using cool graphics.

## Running the Chatbot Locally

### Prerequisites

- Python 3.12
- OpenAI API key

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/githubnext/workspace-blank.git
    cd workspace-blank
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

4. Set up the OpenAI API key:
    ```sh
    export OPENAI_API_KEY='your_openai_api_key'
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
    git clone https://github.com/githubnext/workspace-blank.git
    cd workspace-blank
    ```

2. Build the Docker image:
    ```sh
    docker build -t python-chatbot .
    ```

### Running the Docker Container

1. Run the Docker container:
    ```sh
    docker run -d -p 5000:5000 -e OPENAI_API_KEY='your_openai_api_key' python-chatbot
    ```

2. Open your web browser and go to `http://localhost:5000` to start chatting with the bot.

## Dependencies

- Flask==3.1.0
- openai==0.10.2
- requests==2.25.1
- python_dotenv
