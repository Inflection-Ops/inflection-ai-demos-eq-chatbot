# Use a base image with Python 3.12
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the necessary port for the Flask application
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
