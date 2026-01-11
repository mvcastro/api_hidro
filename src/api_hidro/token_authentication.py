from datetime import datetime, timedelta
from types import TracebackType

import requests
from pydantic.main import BaseModel
from pydantic.types import SecretStr

EXPIRATION_MINUTES = 30


class AuthCredentials(BaseModel):
    login: SecretStr
    password: SecretStr


class TokenAuthHandler:
    def __init__(self, auth_credentials: AuthCredentials):
        self.__auth_credentials = auth_credentials
        self.__token_auth = self.get_api_token()
        self.time_expire = datetime.now() + timedelta(minutes=EXPIRATION_MINUTES)

    def __get_credentials(self) -> tuple[str, str]:
        api_login = self.__auth_credentials.login.get_secret_value()
        api_password = self.__auth_credentials.password.get_secret_value()
        return api_login, api_password

    def get_api_token(self) -> str:
        """
        https://www.ana.gov.br/hidrowebservice/swagger-ui.html#/
        """

        api_login, api_password = self.__get_credentials()
        url_oauth = (
            "https://www.ana.gov.br/hidrowebservice/EstacoesTelemetricas/OAUth/v1"
        )
        headers = {"accept": "*/*", "Identificador": api_login, "Senha": api_password}
        response = requests.get(url_oauth, headers=headers)
        if response.status_code != 200:
            response.raise_for_status()

        token_auth = response.json()["items"]["tokenautenticacao"]
        # os.environ["API_TOKEN_HIDRO"] = token_auth

        return token_auth

    def refresh_token(self) -> None:
        self.__token_auth = self.get_api_token()
        self.time_expire = datetime.now() + timedelta(minutes=EXPIRATION_MINUTES)

    def __enter__(self):
        if datetime.now() > self.time_expire:
            self.refresh_token()
        return self.__token_auth

    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ): ...
