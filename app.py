from flask import Flask, request
from send_email import *
import json

app = Flask("__servico_email__")

@app.route("/servico_email", methods=['POST'])
def email():
    data = request.json
    send_email(data["receiver"], data["subject"], data["message"])
    return "Successfully sent email!"
app.run()