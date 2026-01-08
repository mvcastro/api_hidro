# API HIDRO - Biblioteca Python para Acesso aos dados da API HIDRO ANA

## Objetivo do Projeto

A biblioteca **api_hidro** se destina a obter os dados das estações fluviométricas e pluviométricas a partir de requisições à **API HIDRO ANA** (Agência Nacional de Águas e Saneamento Básico). Esta biblioteca oferece uma interface simplificada e eficiente para acessar informações sobre estações de monitoramento de recursos hídricos no Brasil, incluindo dados de:

- **Inventário de Estações**: Informações cadastrais das estações fluviométricas e pluviométricas
- **Séries Históricas**: Dados históricos de chuva, cota e vazão
- **Dados Telemétricos**: Medições em tempo real ou próximas ao tempo real com diferentes intervalos de amostragem

A biblioteca utiliza autenticação por token OAuth para garantir acesso seguro aos dados da API HIDRO ANA.

---

## Instalação

### Pré-requisitos

- Python 3.10 ou superior
- Credenciais de acesso à API HIDRO ANA (login e senha)

### Instalando a Biblioteca

```bash
pip install api-hidro
```

---

## Autenticação

Para utilizar a biblioteca, você precisa primeiro criar um objeto `TokenAuthHandler` com suas credenciais de acesso:

```python
from api_hidro import TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

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

Retorna o inventário (dados cadastrais) de estações de monitoramento. É possível filtrar por código da estação, unidade federativa ou código da bacia.

**Assinatura:**
```python
retorna_inventario(
    token_auth: TokenAuthHandler,
    codigoestacao: int | None = None,
    unidade_federativa: str | None = None,
    codigo_bacia: int | None = None
) -> list[dict]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: (opcional) Código único da estação
- `unidade_federativa`: (opcional) Sigla do estado (ex: "SP", "RJ", "MG")
- `codigo_bacia`: (opcional) Código da bacia hidrográfica

**Retorno:** Lista de dicionários com dados das estações

**Exceções:**
- `ArgsNotGivenError`: Lançada quando nenhum filtro é fornecido

**Exemplo de Uso:**

```python
from api_hidro import retorna_inventario, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

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
for estacao in inventario_sp:
    print(f"Código: {estacao['codigoestacao']}")
    print(f"Nome: {estacao['nomeestacao']}")
    print(f"Rio: {estacao['nomerio']}")
    print("---")

# Buscar inventário de uma estação específica
inventario_especifico = retorna_inventario(
    token_auth=token_auth,
    codigoestacao=67120000
)
```

---

#### `inventario_por_codigo_estacao()`

Retorna os dados cadastrais de uma estação específica em formato de objeto estruturado `Inventario`.

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
from api_hidro import inventario_por_codigo_estacao, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados da estação com código 67120000
inventario = inventario_por_codigo_estacao(
    token_auth=token_auth,
    codigoestacao=67120000
)

# Acessar as informações como objeto estruturado
print(f"Nome da Estação: {inventario.nomeestacao}")
print(f"Rio: {inventario.nomerio}")
print(f"Localização: {inventario.latitude}, {inventario.longitude}")
```

---

#### `inventario_completo()`

Retorna o inventário completo de todas as estações monitoradas pela API HIDRO ANA em formato de objetos estruturados.

**Assinatura:**
```python
inventario_completo(token_auth: TokenAuthHandler) -> list[Inventario]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação

**Retorno:** Lista de objetos da classe `Inventario` com dados de todas as estações no Brasil

**Exemplo de Uso:**

```python
from api_hidro import inventario_completo, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter inventário completo
todas_estacoes = inventario_completo(token_auth=token_auth)

print(f"Total de estações: {len(todas_estacoes)}")

# Iterar sobre os objetos estruturados
for estacao in todas_estacoes[:5]:  # Primeiras 5 estações
    print(f"Nome: {estacao.estacao_nome}")
    print(f"Rio: {estacao.rio_nome}")
    print(f"Código: {estacao.codigoestacao}")
    print("---")
```

---

#### `retorna_inventario_completo()`

Retorna o inventário completo de todas as estações monitoradas pela API HIDRO ANA em formato de dicionários Python.

**Assinatura:**
```python
retorna_inventario_completo(token_auth: TokenAuthHandler) -> list[dict]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação

**Retorno:** Lista de dicionários com dados de todas as estações no Brasil

**Exemplo de Uso:**

```python
from api_hidro import retorna_inventario_completo, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter inventário completo
todas_estacoes = retorna_inventario_completo(token_auth=token_auth)

print(f"Total de estações: {len(todas_estacoes)}")

# Filtrar estações por tipo (exemplo: estações de chuva)
estacoes_chuva = [
    est for est in todas_estacoes 
    if est.get('tipomedicao') == 'Chuva'
]
print(f"Estações de chuva: {len(estacoes_chuva)}")
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
) -> list[DadosDoMesChuva]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código da estação
- `data_inicial`: Data inicial no formato "YYYY-MM-DD"
- `data_final`: Data final no formato "YYYY-MM-DD"

**Retorno:** Lista de objetos `DadosDoMesChuva` contendo dados mensais de chuva

**Exceções:**
- `TimeSerieNotFoundError`: Lançada quando nenhum dado é encontrado para o período

**Exemplo de Uso:**

```python
from api_hidro import serie_historica_chuva, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados de chuva de uma estação para um período específico
dados_chuva = serie_historica_chuva(
    token_auth=token_auth,
    codigoestacao=67120000,
    data_inicial="2023-01-01",
    data_final="2023-12-31"
)

# Processar os dados
for dado in dados_chuva:
    print(f"Mês/Ano: {dado.data_hora_dado.strftime('%m/%Y')}")
    print(f"Chuva Total: {dado.chuva_total} mm")
    print(f"Dias com Chuva: {dado.dias_chuva}")
    print("---")

# Calcular precipitação total do período
precipitacao_total = sum(
    dado.chuva_total for dado in dados_chuva 
    if dado.chuva_total is not None
)
print(f"Precipitação Total: {precipitacao_total} mm")
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
) -> list[DadosDoMesCota]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código da estação
- `data_inicial`: Data inicial no formato "YYYY-MM-DD"
- `data_final`: Data final no formato "YYYY-MM-DD"

**Retorno:** Lista de objetos `DadosDoMesCota` contendo dados mensais de cota

**Exceções:**
- `TimeSerieNotFoundError`: Lançada quando nenhum dado é encontrado para o período

**Exemplo de Uso:**

```python
from api_hidro import serie_historica_cota, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados de cota (nível de água) para um período
dados_cota = serie_historica_cota(
    token_auth=token_auth,
    codigoestacao=67120000,
    data_inicial="2023-01-01",
    data_final="2023-12-31"
)

# Analisar os dados
for dado in dados_cota:
    print(f"Período: {dado.mes}/{dado.ano}")
    print(f"Cota Máxima: {dado.cota_maxima} m")
    print(f"Cota Mínima: {dado.cota_minima} m")
    print(f"Cota Média: {dado.cota_media} m")
    print("---")

# Encontrar mês com maior cota máxima
cota_maior = max(
    dados_cota,
    key=lambda x: x.cota_maxima if x.cota_maxima is not None else 0
)
print(f"Maior cota: {cota_maior.cota_maxima} m em {cota_maior.mes}/{cota_maior.ano}")
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
) -> list[DadosDoMesVazao]
```

**Parâmetros:**
- `token_auth`: Objeto TokenAuthHandler para autenticação
- `codigoestacao`: Código da estação
- `data_inicial`: Data inicial no formato "YYYY-MM-DD"
- `data_final`: Data final no formato "YYYY-MM-DD"

**Retorno:** Lista de objetos `DadosDoMesVazao` contendo dados diários de vazão para determinado mês

**Exceções:**
- `TimeSerieNotFoundError`: Lançada quando nenhum dado é encontrado para o período

**Exemplo de Uso:**

```python
from api_hidro import serie_historica_vazao, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados de vazão para um período específico
dados_vazao = serie_historica_vazao(
    token_auth=token_auth,
    codigoestacao=67120000,
    data_inicial="2022-01-01",
    data_final="2022-12-31"
)

# Analisar dados de vazão
for dado in dados_vazao:
    print(f"Mês/Ano: {dado.mes}/{dado.ano}")
    print(f"Vazão Máxima: {dado.vazao_maxima} m³/s")
    print(f"Vazão Mínima: {dado.vazao_minima} m³/s")
    print(f"Vazão Média: {dado.vazao_media} m³/s")
    print("---")

# Calcular vazão média anual
vazao_media_anual = sum(
    dado.vazao_media for dado in dados_vazao 
    if dado.vazao_media is not None
) / len([d for d in dados_vazao if d.vazao_media is not None])
print(f"Vazão Média Anual: {vazao_media_anual:.2f} m³/s")
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
from api_hidro import serie_historica_telemetrica_adotada, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados telemétricos com intervalo de 1 hora
dados_telemetrica = serie_historica_telemetrica_adotada(
    token_auth=token_auth,
    codigoestacao=67120000,
    data_inicial="2024-01-01",
    data_final="2024-01-10",
    intervalo_busca="HORA_1"
)

# Processar os dados telemétricos
for dado in dados_telemetrica:
    print(f"Data/Hora: {dado.data_leitura}")
    print(f"Cota: {dado.cota} m")
    print(f"Vazão: {dado.vazao} m³/s")
    print(f"Chuva: {dado.chuva} mm")
    print("---")

# Calcular estatísticas
cotas = [d.cota for d in dados_telemetrica if d.cota is not None]
if cotas:
    print(f"Cota Máxima: {max(cotas)} m")
    print(f"Cota Mínima: {min(cotas)} m")
    print(f"Cota Média: {sum(cotas)/len(cotas):.2f} m")
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
from api_hidro import serie_historica_telemetrica_detalhada, TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

# Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# Obter dados telemétricos detalhados com intervalo de 5 minutos
dados_telemetrica_detalhados = serie_historica_telemetrica_detalhada(
    token_auth=token_auth,
    codigoestacao=67120000,
    data_inicial="2024-01-15",
    data_final="2024-01-20",
    intervalo_busca="5MIN"
)

# Processar os dados detalhados
for dado in dados_telemetrica_detalhados:
    print(f"Data/Hora: {dado.data_leitura}")
    print(f"Cota: {dado.cota} m")
    print(f"Vazão: {dado.vazao} m³/s")
    print(f"Chuva: {dado.chuva} mm")
    print(f"Status da Medição: {dado.status}")
    print("---")

# Monitorar situações de vazão crítica
vazoes_altas = [
    d for d in dados_telemetrica_detalhados 
    if d.vazao and d.vazao > 500
]
print(f"Leituras com vazão acima de 500 m³/s: {len(vazoes_altas)}")
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
from api_hidro import TokenAuthHandler
from api_hidro.token_authentication import AuthCredentials

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
    TokenAuthHandler,
    inventario_completo,
    inventario_por_codigo_estacao,
    serie_historica_chuva,
    serie_historica_vazao,
    serie_historica_telemetrica_adotada,
)
from api_hidro.token_authentication import AuthCredentials

# 1. Configurar autenticação
credenciais = AuthCredentials(
    login="seu_login",
    password="sua_senha"
)
token_auth = TokenAuthHandler(credenciais)

# 2. Obter inventário de estações em um estado específico
print("=== Consultando Inventário de Estações ===")
todas_estacoes = inventario_completo(token_auth=token_auth)
print(f"Total de estações cadastradas: {len(todas_estacoes)}")

# 3. Selecionar uma estação específica
codigo_estacao = 67120000
inventario = inventario_por_codigo_estacao(
    token_auth=token_auth,
    codigoestacao=codigo_estacao
)
print(f"\nEstação: {inventario.nomeestacao}")
print(f"Rio: {inventario.nomerio}")

# 4. Obter dados históricos de chuva
print("\n=== Dados Históricos de Chuva ===")
dados_chuva = serie_historica_chuva(
    token_auth=token_auth,
    codigoestacao=codigo_estacao,
    data_inicial="2023-01-01",
    data_final="2023-03-31"
)
precipitacao_q1 = sum(
    d.chuva_total for d in dados_chuva 
    if d.chuva_total is not None
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
    print(f"Vazão Média {dado.mes}/{dado.ano}: {dado.vazao_media:.2f} m³/s")

# 6. Obter dados telemétricos recentes
print("\n=== Dados Telemétricos Recentes ===")
dados_telemetrica = serie_historica_telemetrica_adotada(
    token_auth=token_auth,
    codigoestacao=codigo_estacao,
    data_inicial="2024-01-01",
    data_final="2024-01-05",
    intervalo_busca="HORA_24"
)
for dado in dados_telemetrica[-3:]:  # Últimos 3 registros
    print(f"{dado.data_leitura}: Cota={dado.cota}m | Vazão={dado.vazao}m³/s")

print("\n=== Consulta Concluída ===")
```

---

## Tratamento de Erros

A biblioteca utiliza exceções personalizadas para diferentes situações:

```python
from api_hidro import (
    TokenAuthHandler,
    inventario_por_codigo_estacao,
    serie_historica_chuva,
)
from api_hidro.errors import InventoryNotFoundError, TimeSerieNotFoundError
from api_hidro.token_authentication import AuthCredentials

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
        codigoestacao=67120000,
        data_inicial="1900-01-01",
        data_final="1900-12-31"  # Período sem dados
    )
except TimeSerieNotFoundError as e:
    print(f"Erro: {e}")

# Tratamento de erro de intervalo de datas
try:
    dados = serie_historica_chuva(
        token_auth=token_auth,
        codigoestacao=67120000,
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
