FROM mitmproxy/mitmproxy

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY ./*.py .

# start the server
CMD ["mitmdump", "-s","main.py"]

# For development use this:
# CMD ["mitmweb", "--web-host", "0.0.0.0"]
# Then run: docker build -t mitmproxy . && docker run -p 8080:8080 -p 127.0.0.1:8081:8081 -it mitmproxy