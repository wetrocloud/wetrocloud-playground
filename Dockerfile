# Use the official Python image as a base
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the Chainlit app on 0.0.0.0
CMD ["chainlit", "run", "app.py", "--watch", "--host", "0.0.0.0", "--port", "8000"]
