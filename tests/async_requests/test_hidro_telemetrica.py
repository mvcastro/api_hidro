import pytest
from api_hidro.async_requests import hidro_telemetrica as ht


class DummyToken:
    def __enter__(self):
        return "fake-token"

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


def test_validation_dates():
    with pytest.raises(ValueError):
        ht.__retorna_serie_historica_telemetrica(
            1, "Detalhada", "DATA_LEITURA", "2021-01-05", "2021-01-01", "PT5M"
        )


def test_interval_exceeded():
    # more than 10 days
    with pytest.raises(ValueError):
        ht.__retorna_serie_historica_telemetrica(
            1, "Detalhada", "DATA_LEITURA", "2021-01-01", "2021-01-20", "PT5M"
        )


def test_retorna_serie_historica_telemetrica_concat(monkeypatch):
    monkeypatch.setattr(ht, "token_auth", DummyToken())

    async def fake_async(
        api_token,
        codigoestacao,
        tipo_telemetrica,
        tipo_filtro_data,
        data_busca,
        intervalo_busca,
    ):
        return [{"data": data_busca, "codigoestacao": codigoestacao}]

    monkeypatch.setattr(ht, "__retorna_serie_telemetrica_async", fake_async)

    result = ht.__retorna_serie_historica_telemetrica(
        1, "Detalhada", "DATA_LEITURA", "2021-01-01", "2021-01-03", "PT5M"
    )
    assert isinstance(result, list)
    # 3 dias -> 3 entries
    assert len(result) == 3
