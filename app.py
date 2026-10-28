from flask import Flask, render_template
from controllers.auth_controller import auth 
from controllers.sistema_controller import sistema

app = Flask(__name__)

app.secret_key = "chave-secreta"


app.register_blueprint(auth)
app.register_blueprint(sistema)
@app.errorhandler
def error_403(error):
    return render_template("erro403.html")

app.run(debug=True)