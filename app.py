from flask import Flask, request
from flask_mail import Mail, Message
import json

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.hostinger.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'info@durbin.live'
app.config['MAIL_PASSWORD'] = 'Durbin@2022'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/sendmail', methods=['GET', 'POST'])
def send_mail():
    # the input json file needs to have the following structure
    #{
     #   recipient : recipient@company.com,
     #   title : title,
     #   sender : sender@company.com,
     #   body: body
    # }

    data = request.json
    sender_mail = data['sender']
    title = data['title']
    recipient = data['recipient']
    body = data['body']

    msg = Message (
        title,
        sender = sender_mail,
        recipients = recipient
    )
    msg.body = body 
    mail.send(msg)
    return 'Sent'

if __name__ == '__main__':
    app.run(debug=True)