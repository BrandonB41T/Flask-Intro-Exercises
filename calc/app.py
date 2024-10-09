# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def handle_add():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def handle_subtract():
    """Subtract 'b' param from 'a' param."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def handle_multiply():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def handle_divide():
    """Divide 'a' param by 'b' param."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

@app.route("/math/<operation>")
def math(operation):
    operations = {
        "add": add,
        "Add": add,
        "sub": sub,
        "Sub": sub,
        "mult": mult,
        "Mult": mult,
        "div": div,
        "Div": div
    }
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations[operation](a, b)
    return str(result)
