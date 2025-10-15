from flask import Flask, request

app = Flask(__name__)

# This is our only route. It will render different HTML based on a URL parameter.
@app.route('/progress')
def show_progress():
    # Get the 'stage' from the URL, e.g., ?stage=1
    stage = request.args.get('stage', default=1, type=int)

    status_text = ""
    next_stage_link = ""

    if stage == 1:
        status_text = "Status: Uploading..."
        next_stage_link = "<a href='/progress?stage=2'>Check Again</a>"
    elif stage == 2:
        status_text = "Status: Analyzing..."
        next_stage_link = "<a href='/progress?stage=3'>Check Again</a>"
    elif stage == 3:
        status_text = "Status: Generating..."
        next_stage_link = "<a href='/progress?stage=4'>Check Again</a>"
    else:
        status_text = "Status: Complete!"
        next_stage_link = "Process finished."

    # Return a full HTML page. Notice how the entire page is sent on every request.
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Prototype 4 - Manual Refresh</title>
        <style>
            body {{
                background-color: #111827; color: white;
                display: flex; align-items: center; justify-content: center;
                min-height: 100vh; font-family: sans-serif;
            }}
            .card {{
                background-color: #1f2937; padding: 2rem;
                border-radius: 0.5rem; text-align: center;
            }}
            a {{ color: #3b82f6; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Processing Lecture</h1>
            <p style="font-size: 1.2rem; margin: 1rem 0;">{status_text}</p>
            {next_stage_link}
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
