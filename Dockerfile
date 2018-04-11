# Use an official Python runtime as a parent image
FROM python:3.6
# Set the working directory to /app
WORKDIR /snap

# Copy the current directory contents into the container at /app
ADD . /snap
ADD ./snap/spiders/snap_spider.py /snap/spiders/snap_spider.py
ADD ./snap/settings.py /snap/settings.py
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "./snap/spiders/snap_spider.py"]