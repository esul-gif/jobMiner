# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app 
#if we mount as volume, dont really need to copy, but can leave it

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

#mount project directory as volume so local changes = changes in container
#docker run -p 8000:5000 -v "$(pwd):/app" your_image_name

#/app because thats where workdir is set in app

#work inside docker container w/ docker exec -it <container id> /bin/bash