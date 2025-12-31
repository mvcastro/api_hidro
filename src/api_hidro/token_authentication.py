import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

from .errors import CredentialsNotFoundError

EXPIRATION_MINUTES = 30


class TokenAuthHandler:
    def __init__(self):
        self.token_auth = self.get_api_token()
        self.time_expire = datetime.now() + timedelta(minutes=EXPIRATION_MINUTES)

    def get_credentials(self) -> tuple[str, str]:
        load_dotenv()  # take environment variables from .env.
        api_login = os.getenv("API_IDENTIFICADOR_HIDRO")
        api_password = os.getenv("API_SENHA_HIDRO")

        if api_login is None or api_password is None:
            raise CredentialsNotFoundError(
                "As credenciais não foram localizadas no arquio .env"
            )
        return api_login, api_password

    def get_api_token(self) -> str:
        """
        https://www.ana.gov.br/hidrowebservice/swagger-ui.html#/
        """

        api_login, api_password = self.get_credentials()
        url_oauth = (
            "https://www.ana.gov.br/hidrowebservice/EstacoesTelemetricas/OAUth/v1"
        )
        headers = {"accept": "*/*", "Identificador": api_login, "Senha": api_password}
        response = requests.get(url_oauth, headers=headers)
        if response.status_code != 200:
            response.raise_for_status()

        token_auth = response.json()["items"]["tokenautenticacao"]
        os.environ["API_TOKEN_HIDRO"] = token_auth

        return token_auth

    def refresh_token(self) -> None:
        self.token_auth = self.get_api_token()
        self.time_expire = datetime.now() + timedelta(minutes=EXPIRATION_MINUTES)

    def __enter__(self):
        if datetime.now() > self.time_expire:
            self.refresh_token()
        return self.token_auth

    def __exit__(self, exc_type, exc_value, traceback): ...


token_auth = TokenAuthHandler()
