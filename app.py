
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>HYACINTHE COUPON AI</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                background: #101827;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 30px 15px;
            }
            h1 { color: #00e676; }
            .box {
                background: #1e293b;
                padding: 25px;
                border-radius: 15px;
                margin-top: 30px;
            }
            button {
                background: #00c853;
                color: white;
                border: none;
                padding: 15px 25px;
                border-radius: 10px;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <h1>HYACINTHE COUPON AI</h1>
        <p>Votre assistant de coupons sportifs</p>
        <div class="box">
            <h2>Bienvenue !</h2>
            <p>5 à 10 matchs par jour</p>
            <p>Tous les championnats du monde</p>
            <p>Analyse des matchs à venir</p>
            <button>Générer un coupon</button>
            <p>Version 1.0</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>HYACINTHE COUPON AI</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                background: #101827;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 30px 15px;
            }
            h1 { color: #00e676; }
            .box {
                background: #1e293b;
                padding: 25px;
                border-radius: 15px;
                margin-top: 30px;
            }
            button {
                background: #00c853;
                color: white;
                border: none;
                padding: 15px 25px;
                border-radius: 10px;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <h1>HYACINTHE COUPON AI</h1>
        <p>Votre assistant de coupons sportifs</p>
        <div class="box">
            <h2>Bienvenue !</h2>
            <p>5 à 10 matchs par jour</p>
            <p>Tous les championnats du monde</p>
            <p>Analyse des matchs à venir</p>
            <button>Générer un coupon</button>
            <p>Version 1.0</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
