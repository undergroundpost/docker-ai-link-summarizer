FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Create templates directory
RUN mkdir templates

# Copy application files
COPY app.py .
COPY gunicorn.conf.py .
COPY templates/ templates/

# Expose port
EXPOSE 5000

# Set environment variable for unbuffered output
ENV PYTHONUNBUFFERED=1

# Run the Flask app with Gunicorn
CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]