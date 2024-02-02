# Use an official Python runtime as a parent image
FROM python:3.9.6-slim


# Install Git
RUN apt-get update && \
    apt-get install -y git
# Install necessary system packages for MySQL client



RUN apt-get update && \
    apt-get install -y \
        default-libmysqlclient-dev \
        build-essential \
        libssl-dev \
        libffi-dev
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Admin.wsgi:application"]
