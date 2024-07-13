# Use the official Python 3.12 slim image as the base image
FROM python:3.12-slim

# Add a non-root user and group to run the application
RUN addgroup --system discord-app-example && \
  adduser --system --ingroup discord-app-example discord-app-example

# Set the working directory
WORKDIR /app

# Copy the wheel file and main.py, set permissions to read-only for the non-root user
COPY --chown=discord-app-example:discord-app-example --chmod=0400 dist/*.whl main.py ./

# Install the wheel file and clean up to reduce image size
RUN pip install --no-cache-dir *.whl && \
  rm *.whl

# Switch to the non-root user
USER discord-app-example

# Run the application
ENTRYPOINT ["python", "main.py"]
