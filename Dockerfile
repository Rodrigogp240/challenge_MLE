# syntax=docker/dockerfile:1.2
FROM python:latest
# put you docker configuration here

# Set the working directory in the container
WORKDIR /challenge

# Copy the current directory contents into the container at /app
COPY . /challenge

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
