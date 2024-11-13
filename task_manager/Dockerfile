# Use official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 (Flask default port)
EXPOSE 5000

# Set the environment to production for Gunicorn
ENV FLASK_ENV=production

# Command to run the Flask app with Gunicorn (replaces Flask’s default development server)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
