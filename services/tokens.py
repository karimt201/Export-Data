import jwt
import extensions
import flask as fk
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import helpers.exceptions as exceptions


class Token:

    def create_token(self, payload):
        """
        Creates a JWT token.

        :param payload: The data to encode in the token.
        
        :return: The encoded token.
        """
        token = jwt.encode(
            payload, extensions.app.config["JWT_SECRET_KEY"], algorithm="HS256"
        )
        return token

    def verify_token(self):
        """
        Verifies a JWT token.

        :return: The decoded token payload.
        
        :raises exceptions.InvalidInputError: If the token is expired or invalid.
        """
        try:
            Auth_token = fk.request.headers.get("Authorization")
            token = Auth_token.split(" ")
            return jwt.decode(
                token[1], extensions.app.config["JWT_SECRET_KEY"], algorithms=["HS256"]
            )
        except ExpiredSignatureError:
            raise exceptions.InvalidInputError("Token has expired")
        except InvalidTokenError:
            raise exceptions.InvalidInputError("Token is invalid")
