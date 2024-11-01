# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask’s port
EXPOSE 5000

# Run the Flask app with docker run -p <local port>:5000 jobminer (if thats name we gave when we build it with docker build -t jobminer .)
CMD ["python", "app.py"]

#docker exec -it <container_name_or_id> /bin/bash

#use -v when running container to mount local project directory to container, for real-time updates to show up in container
#docker run -p 8000:5000 -v "$(pwd):/app" your_image_name
