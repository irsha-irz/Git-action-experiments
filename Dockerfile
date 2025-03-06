# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script into the container
COPY print_args.py .

# Install dependencies (for dotenv)
RUN pip install python-dotenv

# Accept build-time arguments
ARG ARGS="default_arg1 default_arg2"

# Write arguments to .env file
RUN echo "ARGS='${ARGS}'" > .env

# Define the command to run the script
CMD ["python", "print_args.py"]
