# Use the official Python 3.12 slim image as the base image
FROM python:3.12-slim

# Add a non-root user
RUN adduser --system discord-app-example

# Set the working directory
WORKDIR /app

# Copy the wheel file to the working directory
COPY dist/*.whl ./

# Install the wheel file and clean up to reduce image size
RUN pip install --no-cache-dir *.whl && \
  rm *.whl

# Switch to the non-root user
USER discord-app-example

# Run the application
ENTRYPOINT ["python", "-m", "discord_app_example"]
