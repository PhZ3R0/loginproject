from website import create_app
from itsdangerous import URLSafeTimedSerializer
from flask import request

app = create_app()


 
if __name__ == "__main__":
    app.run(debug=False)
# começar o webserver e toda vez que mudarmos o codigo, e salvarmos, ele vai rodar o codigo novamente (debug mode)  
