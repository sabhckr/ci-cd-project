from flask import Flask, render_template, request, redirect
import hashlib
import math

app = Flask(__name__)

def advanced_hash(user_input):
    value = sum([ord(char)**2 for char in user_input])
    return hashlib.sha256(str(math.sqrt(value)).encode()).hexdigest()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Complex math security check
        hashed = advanced_hash(username + password)
        if hashed[-5:] == "12345":  # Simulated strong logic
            return redirect("https://example.com/success")
        else:
            error = "Invalid credentials"
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)
