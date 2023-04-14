# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Download repository
RUN apt-get update && apt-get install -y git
RUN git clone -b cot https://github.com/Lainupcomputer/pycord-bb

# Create a virtual environment
RUN python -m venv venv

# Activate virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Install requirements
RUN pip install -r /app/pycord-bb/requirements.txt

# Set bot token
RUN python /app/pycord-bb/helper/set_bot_token.py YOUR_TOKEN_HERE

# Set bot prefix
RUN python /app/pycord-bb/helper/set_bot_prefix.py YOUR_PREFIX_HERE

# Set the working directory to /app/pycord-bb
WORKDIR /app/pycord-bb

# Start the bot
CMD ["python", "bot.py"]