from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Website</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                text-align: center;
                padding-top: 100px;
            }

            h1 {
                color: #333;
                font-size: 40px;
            }

            p {
                color: #666;
                font-size: 20px;
            }

            button {
                background-color: #333;
                color: white;
                border: none;
                padding: 12px 25px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }

            button:hover {
                background-color: #555;
            }
        </style>
    </head>

    <body>

        <h1>Hello, Vaibhav!</h1>

        <p>Welcome to my first Python website.</p>

        <button onclick="alert('Hello from Python!')">
            Click Me
        </button>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
