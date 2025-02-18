import jwt
import extensions
import flask as fk
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import exceptions
class Token:
    
    def create_token(self,payload):
        token = jwt.encode(payload,extensions.app.config['JWT_SECRET_KEY'], algorithm='HS256')
        return token
    
    def verify_token(self):
        try:
            Auth_token = fk.request.headers.get('Authorization')
            token = Auth_token.split(" ")
            return jwt.decode(token[1], extensions.app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        except ExpiredSignatureError:
            raise exceptions._InvalidInputError("Token has expired")
        except InvalidTokenError:
            raise exceptions._InvalidInputError("Token is invalid")