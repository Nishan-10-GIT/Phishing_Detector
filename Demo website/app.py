from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Route to handle requests and log user dataa
@app.route('/')
def index():
    # Get user's IP address and user-agent (device details)
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    # Log the data into a text file (log.txt)
    log_data = f"IP: {user_ip}, Device: {user_agent}\n"

    with open("log.txt", "a") as log_file:
        log_file.write(log_data)

    # Respond to the client with an HTML message
    return render_template('index.html', message="Your data has been logged!")

if __name__ == '__main__':
    # Run the Flask application
    if not os.path.exists("log.txt"):
        with open("log.txt", "w"): pass  # Create the log.txt file if it doesn't exist
    app.run(debug=True)
