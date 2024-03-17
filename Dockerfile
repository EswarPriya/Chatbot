# Use the official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src
# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .
COPY ./app /usr/src/app


# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port Flask runs on
# ENV LISTEN_PORT 3000
# EXPOSE 3000

# Command to run the Flask application
CMD ["python", "app/main.py"]

