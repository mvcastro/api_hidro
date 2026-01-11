from api_hidro.async_requests import hidro_serie as hs


class DummyToken:
    def __enter__(self):
        return "fake-token"

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


def test_retorna_serie_historica_concat(monkeypatch):
    # patch token_auth
    monkeypatch.setattr(hs, "token_auth", DummyToken())

    async def fake_anual(
        api_token, codigoestacao, tipo_estacao, data_inicial, data_final
    ):
        return [{"year": data_inicial[:4], "codigoestacao": codigoestacao}]

    monkeypatch.setattr(hs, "__retorna_serie_anual", fake_anual)

    data = hs.retorna_serie_historica(10, "Chuva", "2020-01-01", "2021-12-31")
    assert isinstance(data, list)
    # dois anos => 2 items
    assert len(data) == 2
