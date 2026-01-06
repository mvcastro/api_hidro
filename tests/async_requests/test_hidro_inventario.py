import pytest

from api_hidro.async_requests import hidro_inventario as hi
from api_hidro.errors import ArgsNotGivenError, InventoryNotFoundError


def test_retorna_inventario_raises_when_no_args():
    with pytest.raises(ArgsNotGivenError):
        hi.retorna_inventario()


def test_retorna_inventario_returns_items(monkeypatch):
    async def fake_inventory_return(
        codigoestacao=None, unidade_federativa=None, codigo_bacia=None
    ):
        return {
            "items": [{"codigoestacao": 123, "bacia_nome": "X", "estacao_nome": "Y"}]
        }

    monkeypatch.setattr(hi, "__retorna_inventario", fake_inventory_return)

    items = hi.retorna_inventario(codigoestacao=123)
    assert isinstance(items, list)
    assert items[0]["codigoestacao"] == 123


def test_inventario_por_codigo_estacao_returns_model(monkeypatch):
    monkeypatch.setattr(
        hi,
        "retorna_inventario",
        lambda codigoestacao: [
            {
                "Altitude": None,
                "Area_Drenagem": None,
                "Bacia_Nome": "B",
                "Codigo_Adicional": None,
                "Codigo_Operadora_Unidade_UF": None,
                "Data_Periodo_Climatologica_Fim": None,
                "Data_Periodo_Climatologica_Inicio": None,
                "Data_Periodo_Desc_Liquida_Fim": None,
                "Data_Periodo_Desc_Liquida_Inicio": None,
                "Data_Periodo_Escala_Fim": None,
                "Data_Periodo_Escala_Inicio": None,
                "Data_Periodo_Piezometria_Fim": None,
                "Data_Periodo_Piezometria_Inicio": None,
                "Data_Periodo_Pluviometro_Fim": None,
                "Data_Periodo_Pluviometro_Inicio": None,
                "Data_Periodo_Qual_Agua_Fim": None,
                "Data_Periodo_Qual_Agua_Inicio": None,
                "Data_Periodo_Registrador_Chuva_Fim": None,
                "Data_Periodo_Registrador_Chuva_Inicio": None,
                "Data_Periodo_Registrador_Nivel_Fim": None,
                "Data_Periodo_Registrador_Nivel_Inicio": None,
                "Data_Periodo_Sedimento_Inicio": None,
                "Data_Periodo_Sedimento_Fim": None,
                "Data_Periodo_Tanque_Evapo_Fim": None,
                "Data_Periodo_Tanque_Evapo_Inicio": None,
                "Data_Periodo_Telemetrica_Fim": None,
                "Data_Periodo_Telemetrica_Inicio": None,
                "Data_Ultima_Atualizacao": None,
                "Estacao_Nome": "E",
                "Latitude": 0.0,
                "Longitude": 0.0,
                "Municipio_Codigo": 1,
                "Municipio_Nome": "M",
                "Operadora_Codigo": 1,
                "Operadora_Sigla": 1,
                "Operadora_Sub_Unidade_UF": None,
                "Operando": 1,
                "Responsavel_Codigo": 1,
                "Responsavel_Sigla": "R",
                "Responsavel_Unidade_Uf": 1,
                "Rio_Codigo": None,
                "Rio_Nome": "R",
                "Sub_Bacia_Codigo": 1,
                "Sub_Bacia_Nome": "Sb",
                "Tipo_Estacao": "Pluviometrica",
                "Tipo_Estacao_Climatologica": False,
                "Tipo_Estacao_Desc_Liquida": False,
                "Tipo_Estacao_Escala": False,
                "Tipo_Estacao_Piezometria": False,
                "Tipo_Estacao_Pluviometro": False,
                "Tipo_Estacao_Qual_Agua": False,
                "Tipo_Estacao_Registrador_Chuva": False,
                "Tipo_Estacao_Registrador_Nivel": False,
                "Tipo_Estacao_Sedimentos": False,
                "Tipo_Estacao_Tanque_Evapo": False,
                "Tipo_Estacao_Telemetrica": False,
                "Tipo_Rede_Basica": False,
                "Tipo_Rede_Captacao": False,
                "Tipo_Rede_Classe_Vazao": False,
                "Tipo_Rede_Curso_Dagua": False,
                "Tipo_Rede_Energetica": False,
                "Tipo_Rede_Estrategica": False,
                "Tipo_Rede_Navegacao": False,
                "Tipo_Rede_Qual_Agua": False,
                "Tipo_Rede_Sedimentos": False,
                "UF_Estacao": "AC",
                "UF_Nome_Estacao": "Acre",
                "codigobacia": 1,
                "codigoestacao": 321,
            }
        ],
    )

    inv = hi.inventario_por_codigo_estacao(321)
    from api_hidro.async_requests.models import Inventario
    assert isinstance(inv, Inventario)
    assert inv.codigoestacao == 321


def test_inventario_por_codigo_estacao_raises_when_empty(monkeypatch):
    monkeypatch.setattr(hi, "retorna_inventario", lambda codigoestacao: [])

    with pytest.raises(InventoryNotFoundError):
        hi.inventario_por_codigo_estacao(999)


def test_retorna_inventario_completo_concat(monkeypatch):
    # reduzir BACIAS para duas entradas
    monkeypatch.setattr(hi, "BACIAS", [{"codigobacia": 1}, {"codigobacia": 2}])

    async def fake_retorn(
        codigoestacao=None, unidade_federativa=None, codigo_bacia=None
    ):
        return {"items": [{"codigoestacao": codigo_bacia}]}

    monkeypatch.setattr(hi, "__retorna_inventario", fake_retorn)

    result = hi.retorna_inventario_completo()
    assert isinstance(result, list)
    assert any(item["codigoestacao"] == 1 for item in result)
    assert any(item["codigoestacao"] == 2 for item in result)
