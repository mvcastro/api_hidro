# API HIDRO - Biblioteca Python para Acesso aos dados da API HIDRO ANA

## Objetivo do Projeto

A biblioteca **api_hidro** se destina a obter os dados das estações fluviométricas e pluviométricas a partir de requisições à **API HIDRO ANA** (Agência Nacional de Águas e Saneamento Básico). Esta biblioteca oferece uma interface simplificada e eficiente para acessar informações sobre estações de monitoramento de recursos hídricos no Brasil, incluindo dados de:

- **Inventário de Estações**: Informações cadastrais das estações fluviométricas e pluviométricas
- **Séries Históricas**: Dados históricos de chuva, cota e vazão
- **Dados Telemétricos**: Medições em tempo real ou próximas ao tempo real com diferentes intervalos de amostragem

A biblioteca utiliza autenticação por token OAuth para garantir acesso seguro aos dados da API HIDRO ANA. Para 
solicitar acesso à API confira as instruções contidas neste [link](https://www.snirh.gov.br/hidroweb/acesso-api).

---

## Instalação

### Pré-requisitos

- Python 3.12 ou superior
- Credenciais de acesso à API HIDRO ANA (login e senha)

### Instalando a Biblioteca

```bash
pip install api-hidro
```

---

## Autenticação

Para utilizar a biblioteca, você precisa primeiro criar um objeto `TokenAuthHandler` com suas credenciais de acesso:

```python
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Criar credenciais de autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)

# Inicializar o handler de autenticação
token_auth = TokenAuthHandler(credenciais)
```

O token é automaticamente gerenciado pela biblioteca e renovado quando necessário. A validade padrão do token é de 30 minutos.

---

## Funções Disponíveis

### 1. Funções de Inventário

#### `retorna_inventario()`

Retorna o inventário (dados cadastrais) de estações de monitoramento. É possível filtrar por código da estação, unidade federativa ou código da bacia. Os campos do dicionário Python podem ser verificados na [documentação](https://www.ana.gov.br/hidrowebservice/swagger-ui/index.html#/WSEstacoesTelemetricasController/gethidroinventarioestacoes) da API.

**Assinatura:**
```python
retorna_inventario(
    token_auth: TokenAuthHandler,
    codigoestacao: int | None = None,
    unidade_federativa: str | None = None,
    codigo_bacia: int | None = None
) -> list[dict[CampoInventario, str]]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: (opcional) Código único da estação
- `unidade_federativa`: (opcional) Sigla do estado (ex: "SP", "RJ", "MG")
- `codigo_bacia`: (opcional) Código da bacia hidrográfica

**Retorno:** Lista de dicionários com dados das estações. Importante destacar que os valores dos campos estão no formato `str` por terem sido desserializados a partir do JSON da API.

**Exceções:**
- `ArgsNotGivenError`: Lançada quando nenhum filtro é fornecido

**Exemplo de Uso:**

```python
from pprint import pprint

from api_hidro import retorna_inventario
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Buscar inventário de estações no estado de São Paulo
inventario_sp = retorna_inventario(
    token_auth=token_auth,
    unidade_federativa="SP"
)

# Exibir informações das estações
for estacao in inventario_sp[:3]:
    print(f"Código: {estacao['codigoestacao']}")
    print(f"Nome: {estacao['Estacao_Nome']}")
    print(f"Rio: {estacao['Rio_Nome']}")
    print("---")
```

Resultado:
```
Código: 2249008
Nome: MARÍLIA
Rio: N/A
---
Código: 2249014
Nome: MUNDO NOVO
Rio: N/A
---
Código: 2249016
Nome: BAIRRO SÃO GERALDO
Rio: N/A
---
```

**Continuação do Exemplo de Uso:**

```python
# Buscar inventário de uma estação específica
inventario_estacao = retorna_inventario(
    token_auth=token_auth,
    codigoestacao=2249008
)

# Exibir informações da estação MARÍLIA - Código: 2249008
pprint(inventario_estacao)
```

Resultado:
```
[{'Altitude': '640.0',
  'Area_Drenagem': None,
  'Bacia_Nome': 'RIO PARANÁ',
  'Codigo_Adicional': 'D6-025',
  'Codigo_Operadora_Unidade_UF': None,
  'Data_Periodo_Climatologica_Fim': None,
  'Data_Periodo_Climatologica_Inicio': None,
  'Data_Periodo_Desc_Liquida_Fim': None,
  'Data_Periodo_Desc_liquida_Inicio': None,
  'Data_Periodo_Escala_Fim': None,
  'Data_Periodo_Escala_Inicio': None,
  'Data_Periodo_Piezometria_Fim': None,
  'Data_Periodo_Piezometria_Inicio': None,
  'Data_Periodo_Pluviometro_Fim': None,
  'Data_Periodo_Pluviometro_Inicio': '1939-07-01 00:00:00.0',
  'Data_Periodo_Qual_Agua_Fim': None,
  'Data_Periodo_Qual_Agua_Inicio': None,
  'Data_Periodo_Registrador_Chuva_Fim': None,
  'Data_Periodo_Registrador_Chuva_Inicio': None,
  'Data_Periodo_Registrador_Nivel_Fim': None,
  'Data_Periodo_Registrador_Nivel_Inicio': None,
  'Data_Periodo_Sedimento_Inicio': None,
  'Data_Periodo_Sedimento_fim': None,
  'Data_Periodo_Tanque_Evapo_Fim': None,
  'Data_Periodo_Tanque_Evapo_Inicio': None,
  'Data_Periodo_Telemetrica_Fim': None,
  'Data_Periodo_Telemetrica_Inicio': None,
  'Data_Ultima_Atualizacao': '2005-05-19 00:00:00.0',
  'Estacao_Nome': 'MARÍLIA',
  'Latitude': '-22.2167',
  'Longitude': '-49.9333',
  'Municipio_Codigo': '21292000',
  'Municipio_Nome': 'MARÍLIA',
  'Operadora_Codigo': '10',
  'Operadora_Sigla': 'SPÁGUAS-SP',
  'Operadora_Sub_Unidade_UF': None,
  'Operando': '1',
  'Responsavel_Codigo': '10',
  'Responsavel_Sigla': 'SPÁGUAS-SP',
  'Responsavel_Unidade_UF': '21',
  'Rio_Codigo': None,
  'Rio_Nome': 'N/A',
  'Sub_Bacia_Codigo': '63',
  'Sub_Bacia_Nome': 'RIOS PARANÁ,PARDO E OUTROS',
  'Tipo_Estacao': 'Pluviometrica',
  'Tipo_Estacao_Climatologica': '0',
  'Tipo_Estacao_Desc_Liquida': '0',
  'Tipo_Estacao_Escala': '0',
  'Tipo_Estacao_Piezometria': '0',
  'Tipo_Estacao_Pluviometro': '1',
  'Tipo_Estacao_Qual_Agua': '0',
  'Tipo_Estacao_Registrador_Chuva': '0',
  'Tipo_Estacao_Registrador_Nivel': '0',
  'Tipo_Estacao_Sedimentos': '0',
  'Tipo_Estacao_Tanque_evapo': '0',
  'Tipo_Estacao_Telemetrica': '0',
  'Tipo_Rede_Basica': '0',
  'Tipo_Rede_Captacao': '0',
  'Tipo_Rede_Classe_Vazao': '0',
  'Tipo_Rede_Curso_Dagua': '0',
  'Tipo_Rede_Energetica': '0',
  'Tipo_Rede_Estrategica': '0',
  'Tipo_Rede_Navegacao': '0',
  'Tipo_Rede_Qual_Agua': '0',
  'Tipo_Rede_Sedimentos': '0',
  'UF_Estacao': 'SP',
  'UF_Nome_Estacao': 'SÃO PAULO',
  'codigobacia': '6',
  'codigoestacao': '2249008'}]
```

---

#### `inventario_por_codigo_estacao()`

Retorna os dados cadastrais de uma estação específica em formato de objeto estruturado `Inventario`. Objetos da classe `Inventario` já apresentam os valores de seus atributos convertidos nos tipos corretos.

**Assinatura:**
```python
inventario_por_codigo_estacao(
    token_auth: TokenAuthHandler,
    codigoestacao: int
) -> Inventario
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código único da estação

**Retorno:** Objeto da classe `Inventario` com dados estruturados da estação

**Exceções:**
- `InventoryNotFoundError`: Lançada quando a estação não é encontrada

**Exemplo de Uso:**

```python
from api_hidro import inventario_por_codigo_estacao
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados da estação com código 67120000
inventario_estacao = inventario_por_codigo_estacao(
    token_auth=token_auth,
    codigoestacao=10100000
)

# Acessar as informações como objeto estruturado
print(f"Nome da Estação: {inventario_estacao.estacao_nome}")
print(f"Rio: {inventario_estacao.rio_nome}")
print(f"Área de Drenagem (Km²): {inventario_estacao.area_drenagem}")
print(f"Entidade Responsável: {inventario_estacao.responsavel_sigla}")
print(f"Coordenadas: ({inventario_estacao.latitude}, {inventario_estacao.longitude})")
```
Resultado:
```
Nome da Estação: TABATINGA
Rio: RIO SOLIMÕES-AMAZONAS
Área de Drenagem (Km²): 874000.0
Entidade Responsável: ANA
Coordenadas: (-4.2347, -69.9447)
```

---

#### `inventario_completo()`

Retorna o inventário completo de todas as estações monitoradas pela API HIDRO ANA em formato de objetos estruturados do tipo `Inventario`. Objetos da classe `Inventario` já apresentam os valores de seus atributos convertidos nos tipos corretos (vide exemplo acima). Portanto, recomenda-se utilizar essa função para obtenção do inventário. Porém, caso haja preferência por dicionários Python idênticos ao JSON retornado pela API, pode-se utilizar a função descrita na sequência.

**Assinatura:**
```python
inventario_completo(token_auth: TokenAuthHandler) -> list[Inventario]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação

**Retorno:** Lista de objetos da classe `Inventario` com dados de todas as estações cadastradas no HIDRO

**Exemplo de Uso:**

```python
from api_hidro import inventario_completo
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter inventário completo
todas_estacoes = inventario_completo(token_auth=token_auth)

print(f"Total de estações: {len(todas_estacoes)}")
print("---")
# Iterar sobre os objetos estruturados
for estacao in todas_estacoes[:5]:  # Primeiras 5 estações
    print(f"Nome: {estacao.estacao_nome}")
    print(f"Código: {estacao.codigoestacao}")
    print(f"Tipo de Estação: {estacao.tipo_estacao}")
    print("---")
```

Resultado:
```
Total de estações: 40069
---
Nome: TABAJARA
Código: 862000
Tipo de Estação: Pluviometrica
---
Nome: PORTO VELHO
Código: 863000
Tipo de Estação: Pluviometrica
---
Nome: PORTO VELHO
Código: 863002
Tipo de Estação: Pluviometrica
---
Nome: CACHOEIRA DO SAMUEL
Código: 863003
Tipo de Estação: Pluviometrica
---
Nome: SANTA ISABEL
Código: 863004
Tipo de Estação: Pluviometrica
---
```

---

#### `retorna_inventario_completo()`

Retorna o inventário completo de todas as estações monitoradas pela API HIDRO ANA em formato de dicionários Python. Os dicionários são idênticos ao JSON retornado pela API, ou seja, os dados dos dicionários são todos do tipo `str`

**Assinatura:**
```python
retorna_inventario_completo(token_auth: TokenAuthHandler) -> list[dict[CampoInventario, str]]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação

**Retorno:** Lista de dicionários com informações cadastrais de todas as estações do HIDRO

**Exemplo de Uso:**

```python
from api_hidro import retorna_inventario_completo
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter inventário completo
todas_estacoes = retorna_inventario_completo(token_auth=token_auth)

print(f"Total de estações: {len(todas_estacoes)}")
print("---")

# Filtrar estações por tipo (exemplo: estações pluviométricas)
estacoes_chuva = [
    est for est in todas_estacoes 
    if est.get("Tipo_Estacao") == "Pluviometrica"
]
print(f"Total de estações pluviométricas: {len(estacoes_chuva)}")
```
Resultado:
```
Total de estações: 40069
---
Total de estações pluviométricas: 22545
```

---

### 2. Funções de Séries Históricas

#### `serie_historica_chuva()`

Retorna dados históricos de precipitação (chuva) para uma estação e período específicos.

**Assinatura:**
```python
serie_historica_chuva(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    data_inicial: str,
    data_final: str
) -> list[DadosMesAnoChuva]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código da estação
- `data_inicial`: Data inicial no formato "YYYY-MM-DD"
- `data_final`: Data final no formato "YYYY-MM-DD"

**Retorno:** Lista de objetos `DadosMesAnoChuva` contendo dados diários de chuva em determinaddo mês/ano da série

**Exceções:**
- `TimeSerieNotFoundError`: Lançada quando nenhum dado é encontrado para o período

**Exemplo de Uso:**

```python
from api_hidro import serie_historica_chuva
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados de chuva de uma estação para um período específico
dados_chuva = serie_historica_chuva(
    token_auth=token_auth,
    codigoestacao=862000,
    data_inicial="2023-01-01",
    data_final="2023-12-31"
)

# Analisar os 3 primeiros registros para o período selecionado:
for dado in dados_chuva[:3]:
    print(f"Mês/Ano: {dado.data_hora_dado.strftime('%m/%Y')}")
    print(f"Chuva Total: {dado.total} mm")
    print(f"Dias com Chuva: {dado.numero_dias_de_chuva}")
    print("---")

# Calcular precipitação total do período
precipitacao_total = sum(
    dado.total for dado in dados_chuva 
    if dado.total is not None
)
print(f"Precipitação Total: {precipitacao_total:.2f} mm")
```

Resultado:
```
Mês/Ano: 01/2023
Chuva Total: 210.8 mm
Dias com Chuva: 6
---
Mês/Ano: 03/2023
Chuva Total: 440.8 mm
Dias com Chuva: 15
---
Mês/Ano: 02/2023
Chuva Total: 237.8 mm
Dias com Chuva: 13
---
Precipitação Total: 1825.60 mm
```

---

#### `serie_historica_cota()`

Retorna dados históricos de cota (nível de água) para uma estação e período específicos.

**Assinatura:**
```python
serie_historica_cota(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    data_inicial: str,
    data_final: str
) -> list[DadosMesAnoCota]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código da estação
- `data_inicial`: Data inicial no formato "YYYY-MM-DD"
- `data_final`: Data final no formato "YYYY-MM-DD"

**Retorno:** Lista de objetos `DadosMesAnoCota` contendo dados diários de cota em determinaddo mês/ano da série

**Exceções:**
- `TimeSerieNotFoundError`: Lançada quando nenhum dado é encontrado para o período

**Exemplo de Uso:**

```python
from api_hidro import serie_historica_cota
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados de cota (nível de água) para um período
dados_cota = serie_historica_cota(
    token_auth=token_auth,
    codigoestacao=10100000,
    data_inicial="2023-01-01",
    data_final="2023-12-31"
)

# Analisar os 3 primeiros registros para o período selecionado:
for dado in dados_cota[:3]:
    print(f"Período: {dado.data_hora_dado.strftime('%m/%Y')}")
    print(f"Cota Máxima: {dado.maxima} m")
    print(f"Cota Mínima: {dado.minima} m")
    print(f"Cota Média: {dado.media} m")
    print("---")

# Encontrar mês com maior cota máxima no ano de 2023
cota_maior = max(
    dados_cota,
    key=lambda x: x.maxima if x.maxima is not None else 0
)
print(f"Maior cota: {cota_maior.maxima} m em {cota_maior.data_hora_dado.strftime('%m/%Y')}")
```
Resultado:
```
Período: 01/2023
Cota Máxima: 826.0 m
Cota Mínima: 353.0 m
Cota Média: 545.0 m
---
Período: 02/2023
Cota Máxima: 924.0 m
Cota Mínima: 728.0 m
Cota Média: 816.0 m
---
Período: 03/2023
Cota Máxima: 1091.0 m
Cota Mínima: 926.0 m
Cota Média: 1027.0 m
---
Maior cota: 1205.0 m em 05/2023
```

---

#### `serie_historica_vazao()`

Retorna dados históricos de vazão para uma estação e período específicos.

**Assinatura:**
```python
serie_historica_vazao(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    data_inicial: str,
    data_final: str
) -> list[DadosMesAnoVazao]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código da estação
- `data_inicial`: Data inicial no formato "YYYY-MM-DD"
- `data_final`: Data final no formato "YYYY-MM-DD"

**Retorno:** Lista de objetos `DadosMesAnoVazao` contendo dados diários de vazão para determinado mês

**Exceções:**
- `TimeSerieNotFoundError`: Lançada quando nenhum dado é encontrado para o período

**Exemplo de Uso:**

```python
from api_hidro import serie_historica_vazao
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados de vazão para um período específico
dados_vazao = serie_historica_vazao(
    token_auth=token_auth,
    codigoestacao=10100000,
    data_inicial="2022-01-01",
    data_final="2022-12-31"
)

# Analisar os 3 primeiros registros para o período analisado
for dado in dados_vazao[:3]:
    print(f"Mês/Ano: {dado.data_hora_dado.strftime('%m/%Y')}")
    print(f"Vazão Máxima: {dado.maxima} m³/s")
    print(f"Vazão Mínima: {dado.minima} m³/s")
    print(f"Vazão Média: {dado.media} m³/s")
    print("---")

# Calcular vazão média anual
vazao_media_anual = sum(
    dado.media for dado in dados_vazao 
    if dado.media is not None
) / len([d for d in dados_vazao if d.media is not None])
print(f"Vazão Média Anual: {vazao_media_anual:.2f} m³/s")
```

Resultado:
```
Mês/Ano: 01/2022
Vazão Máxima: 46645.6 m³/s
Vazão Mínima: 28796.533 m³/s
Vazão Média: 36477.9 m³/s
---
Mês/Ano: 02/2022
Vazão Máxima: 44150.65 m³/s
Vazão Mínima: 32137.498 m³/s
Vazão Média: 39327.13 m³/s
---
Mês/Ano: 03/2022
Vazão Máxima: 56072.71 m³/s
Vazão Mínima: 43820.95 m³/s
Vazão Média: 50096.62 m³/s
---
Vazão Média Anual: 37869.51 m³/s
```

---

### 3. Funções de Dados Telemétricos

#### `serie_historica_telemetrica_adotada()`

Retorna dados telemétricos resumidos (adotados) de uma estação para um período específico. Os dados telemétricos possuem uma resolução temporal maior (até 5 minutos) comparado aos dados históricos mensais.

**Assinatura:**
```python
serie_historica_telemetrica_adotada(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    data_inicial: str,
    data_final: str,
    intervalo_busca: str = "HORA_24"
) -> list[DadoTelemetricaAdotada]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código da estação
- `data_inicial`: Data inicial no formato "YYYY-MM-DD"
- `data_final`: Data final no formato "YYYY-MM-DD" (máximo 10 dias de intervalo)
- `intervalo_busca`: (opcional) Intervalo de amostragem. Opções: "5MIN", "10MIN", "15MIN", "30MIN", "HORA_1", "HORA_6", "HORA_24". Padrão: "HORA_24"

**Retorno:** Lista de objetos `DadoTelemetricaAdotada` com medições telemátricas

**Exceções:**
- `TimeSerieNotFoundError`: Lançada quando nenhum dado é encontrado
- `ValueError`: Lançada quando o intervalo é maior que 10 dias

**Exemplo de Uso:**

```python
from api_hidro import serie_historica_telemetrica_adotada
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados telemétricos com intervalo de busca 24 horas
dados_telemetrica = serie_historica_telemetrica_adotada(
    token_auth=token_auth,
    codigoestacao=10100000,
    data_inicial="2024-01-01",
    data_final="2024-01-02",
    intervalo_busca="HORA_24"
)

# Analisar os 3 últimos registros da estação telemétrica
for dado in dados_telemetrica[:3]:
    print(f"Data/Hora: {dado.data_hora_medicao}")
    print(f"Cota: {dado.cota_adotada} m")
    print(f"Vazão: {dado.vazao_adotada} m³/s")
    print(f"Chuva: {dado.chuva_adotada} mm")
    print("---")

# Calcular estatísticas
cotas = [d.cota_adotada for d in dados_telemetrica if d.cota_adotada is not None]
if cotas:
    print(f"Cota Máxima: {max(cotas)} m")
    print(f"Cota Mínima: {min(cotas)} m")
    print(f"Cota Média: {sum(cotas)/len(cotas):.2f} m")
```

Resultado:
```
Data/Hora: 2024-01-02 23:15:00
Cota: None m
Vazão: None m³/s
Chuva: 0.0 mm
---
Data/Hora: 2024-01-02 23:30:00
Cota: None m
Vazão: None m³/s
Chuva: 0.0 mm
---
Data/Hora: 2024-01-02 23:45:00
Cota: None m
Vazão: None m³/s
Chuva: 0.0 mm
---
Cota Máxima: 953.0 m
Cota Mínima: 944.0 m
Cota Média: 949.25 m
```
---

#### `serie_historica_telemetrica_detalhada()`

Retorna dados telemétricos detalhados de uma estação para um período específico. Similar à função anterior, mas com informações mais completas.

**Assinatura:**
```python
serie_historica_telemetrica_detalhada(
    token_auth: TokenAuthHandler,
    codigoestacao: int,
    data_inicial: str,
    data_final: str,
    intervalo_busca: str = "HORA_24"
) -> list[DadoTelemetricaDetalhada]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código da estação
- `data_inicial`: Data inicial no formato "YYYY-MM-DD"
- `data_final`: Data final no formato "YYYY-MM-DD" (máximo 10 dias de intervalo)
- `intervalo_busca`: (opcional) Intervalo de amostragem. Opções: "5MIN", "10MIN", "15MIN", "30MIN", "HORA_1", "HORA_6", "HORA_24". Padrão: "HORA_24"

**Retorno:** Lista de objetos `DadoTelemetricaDetalhada` com medições detalhadas

**Exceções:**
- `TimeSerieNotFoundError`: Lançada quando nenhum dado é encontrado
- `ValueError`: Lançada quando o intervalo é maior que 10 dias

**Exemplo de Uso:**

```python
from api_hidro import serie_historica_telemetrica_detalhada
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados telemétricos detalhados com intervalo de bbbusca de 24 horas (default)
dados_telemetrica_detalhados = serie_historica_telemetrica_detalhada(
    token_auth=token_auth,
    codigoestacao=10100000,
    data_inicial="2024-12-30",
    data_final="2024-12-31"
)

# Analisar somente os horários com vazão adotada existente
for dado in dados_telemetrica_detalhados:
    if dado.vazao_adotada:
        print(f"Data/Hora: {dado.data_hora_medicao}")
        print(f"Cota: {dado.cota_adotada} m")
        print(f"Vazão: {dado.vazao_adotada} m³/s")
        print(f"Chuva: {dado.chuva_acumulada} mm")
        print("---")

# Monitorar situações de vazão crítica
vazoes_altas = [
    d for d in dados_telemetrica_detalhados 
    if d.vazao_adotada and d.vazao_adotada > 42500
]
print(f"Número de leituras filtadas com vazão acima de 42.500 m³/s: {len(vazoes_altas)}")
```
Resultado:
```
Data/Hora: 2024-12-30 08:15:00
Cota: 834.0 m
Vazão: 42305.27 m³/s
Chuva: 961.6 mm
---
Data/Hora: 2024-12-30 18:15:00
Cota: 835.0 m
Vazão: 42346.03 m³/s
Chuva: 961.6 mm
---
Data/Hora: 2024-12-31 08:15:00
Cota: 842.0 m
Vazão: 42631.7 m³/s
Chuva: 995.6 mm
---
Data/Hora: 2024-12-31 18:15:00
Cota: 844.0 m
Vazão: 42713.41 m³/s
Chuva: 996.2 mm
---
Número de leituras filtadas com vazão acima de 42.500 m³/s: 2
```
---

### 4. Classe de Autenticação

#### `TokenAuthHandler`

Classe responsável por gerenciar a autenticação com a API HIDRO ANA através de tokens OAuth.

**Características:**
- Gerenciamento automático de tokens
- Renovação automática quando o token expira (validade de 30 minutos)
- Compatível com context manager (with statement)

**Exemplo de Uso:**

```python
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# Criar credenciais
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)

# Inicializar o handler
token_auth = TokenAuthHandler(credenciais)

# O token é automaticamente gerenciado
# Usar em qualquer função que requeira autenticação
resultado = retorna_inventario(token_auth=token_auth, unidade_federativa="SP")

# Renovar token manualmente se necessário
token_auth.refresh_token()
```

---

## Exemplo Completo de Uso

Este exemplo demonstra um fluxo completo de uso da biblioteca:

```python
from api_hidro import (
    inventario_completo,
    inventario_por_codigo_estacao,
    serie_historica_chuva,
    serie_historica_vazao,
    serie_historica_telemetrica_adotada,
)
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

# 1. Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# 2. Obter inventário de uma estação específica
print("=== Consultando Inventário de Estações ===")

codigo_estacao_flu = 10100000 # Estação TABATINGA
codigo_estacao_plu = 470005 # SANTA TERESA NOVA (PARAÍSO)
codigo_estacao_plu_telemetrica = 469001 # Estação TABATINGA

inventario = inventario_por_codigo_estacao(
    token_auth=token_auth,
    codigoestacao=codigo_estacao_flu
)
print(f"\nEstação: {inventario.estacao_nome}")
print(f"Rio: {inventario.rio_nome}")

# 4. Obter dados históricos de chuva
print("\n=== Dados Históricos de Chuva ===")
dados_chuva = serie_historica_chuva(
    token_auth=token_auth,
    codigoestacao=codigo_estacao_plu,
    data_inicial="2023-01-01",
    data_final="2023-03-31"
)
precipitacao_q1 = sum(
    d.total for d in dados_chuva 
    if d.total is not None
)
print(f"Precipitação Q1/2023: {precipitacao_q1} mm")

# 5. Obter dados históricos de vazão
print("\n=== Dados Históricos de Vazão ===")
dados_vazao = serie_historica_vazao(
    token_auth=token_auth,
    codigoestacao=codigo_estacao,
    data_inicial="2023-01-01",
    data_final="2023-03-31"
)
for dado in dados_vazao[:3]:  # Primeiros 3 meses
    print(f"Vazão Média {dado.data_hora_dado.strftime('%m/%Y')}: {dado.media:.2f} m³/s")

# 6. Obter dados telemétricos recentes
print("\n=== Dados Telemétricos Recentes ===")
dados_telemetrica = serie_historica_telemetrica_detalhada(
    token_auth=token_auth,
    codigoestacao=codigo_estacao_plu_telemetrica,
    data_inicial="2023-03-30",
    data_final="2023-03-31",
    intervalo_busca="HORA_24"
)
for dado in dados_telemetrica[-5:]:  # Últimos 5 registros
    print(
        f"{dado.data_hora_medicao.strftime('%d/%m/%Y %T')}: "\
        + f"Chuva={dado.chuva_adotada or 0.0:.2f}m - "\
        + f"Chuva Acumulada={dado.chuva_acumulada or 0.0:.2f}m"
    )

print("\n=== Consulta Concluída ===")
```
Resultado:
```
=== Dados Históricos de Chuva ===
Precipitação Q1/2023: 1966.0 mm

=== Dados Históricos de Vazão ===
Vazão Média 04/2023: 55600.93 m³/s
Vazão Média 05/2023: 57018.84 m³/s 
Vazão Média 06/2023: 50722.69 m³/s 

=== Dados Telemétricos Recentes ===
31/03/2023 22:45:00: Chuva=0.00m - Chuva Acumulada=2297.80m
31/03/2023 23:00:00: Chuva=0.20m - Chuva Acumulada=2298.00m
31/03/2023 23:15:00: Chuva=0.20m - Chuva Acumulada=2298.20m
31/03/2023 23:30:00: Chuva=0.40m - Chuva Acumulada=2298.60m
31/03/2023 23:45:00: Chuva=0.00m - Chuva Acumulada=2298.60m

=== Consulta Concluída ===
```
---

## Tratamento de Erros

A biblioteca utiliza exceções personalizadas para diferentes situações:

```python
from api_hidro import (
    inventario_por_codigo_estacao,
    serie_historica_chuva,
)
from api_hidro.errors import InventoryNotFoundError, TimeSerieNotFoundError
from api_hidro.token_authentication import AuthCredentials, TokenAuthHandler

credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Tratamento de erro ao buscar inventário
try:
    inventario = inventario_por_codigo_estacao(
        token_auth=token_auth,
        codigoestacao=99999999  # Código inexistente
    )
except InventoryNotFoundError as e:
    print(f"Erro: {e}")

# Tratamento de erro ao buscar série histórica
try:
    dados = serie_historica_chuva(
        token_auth=token_auth,
        codigoestacao=10100000,
        data_inicial="1900-01-01",
        data_final="1900-12-31"  # Período sem dados
    )
except TimeSerieNotFoundError as e:
    print(f"Erro: {e}")

# Tratamento de erro de intervalo de datas
try:
    dados = serie_historica_chuva(
        token_auth=token_auth,
        codigoestacao=10100000,
        data_inicial="2024-01-01",
        data_final="2023-12-31"  # Data final menor que inicial
    )
except ValueError as e:
    print(f"Erro de validação: {e}")
```

---

## Documentação da API HIDRO ANA

Para mais informações sobre os dados e endpoints disponíveis, visite a documentação oficial:

- [API HIDRO ANA - Swagger](https://www.ana.gov.br/hidrowebservice/swagger-ui.html)
- [Agência Nacional de Águas](https://www.ana.gov.br/)

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests para melhorias.
