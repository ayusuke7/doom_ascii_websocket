# DOOM em ASCII via WebSocket

Este projeto roda o jogo DOOM em ASCII utilizando um servidor WebSocket para capturar a tela do jogo e um cliente WebSocket para exibir os frames em ASCII no terminal.

![Sample Screenshot](screens/sample.gif)

## Requisitos

- Python 3.7 ou superior
- `pip` (gerenciador de pacotes do Python)
- DOOM (prboom) instalado or makge [doomgeneric](https://github.com/ozkl/doomgeneric)
- `wmctrl` instalado (para obter as coordenadas da janela do DOOM)

## Instalação de Dependências

1. Clone o repositório:

   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Instale as dependências Python:

   ```sh
   pip install -r requirements.txt
   ```

   Certifique-se de que o arquivo `requirements.txt` contenha as seguintes dependências:

   ```
   asyncio
   opencv-python
   mss
   numpy
   websockets
   ```

3. Instale o `wmctrl`:

   ```sh
   sudo apt-get install wmctrl
   ```

## Executando o Servidor

1. Inicie o servidor WebSocket:

   ```sh
   python server.py
   ```

   O servidor irá iniciar o DOOM em modo janela e começar a capturar a tela, convertendo os frames para ASCII e enviando-os via WebSocket.

## Executando o Cliente

1. Em outro terminal, inicie o cliente WebSocket:

   ```sh
   python client.py
   ```

   O cliente irá se conectar ao servidor WebSocket e exibir os frames em ASCII no terminal.

## Estrutura do Projeto

- [client.py](http://_vscodecontentref_/1): Código do cliente WebSocket que recebe e exibe os frames em ASCII.
- [server.py](http://_vscodecontentref_/2): Código do servidor WebSocket que captura a tela do DOOM, converte para ASCII e envia os frames.
- [doomgeneric](https://github.com/ozkl/doomgeneric): Port do DOOM utilizado para obter os frames do jogo

## Observações

- Certifique-se de que o DOOM esteja instalado e configurado e executando corretamente no seu sistema.
- O script server.py utiliza o comando `wmctrl` para obter as coordenadas da janela do DOOM. Certifique-se de que o `wmctrl` esteja instalado e funcionando corretamente.

Divirta-se jogando DOOM em ASCII no terminal!
