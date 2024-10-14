# wpp-send-img-auto

Este projeto foi criado com o objetivo de auxiliar um restaurante na manutenção de seus clientes, permitindo o envio automático de cardápios/imagens via WhatsApp utilizando a biblioteca [pywhatkit](https://pypi.org/project/pywhatkit/https://pypi.org/project/pywhatkit/). É uma ferramenta útil para quem deseja compartilhar imagens em massa de forma prática e rápida.

## Pré-requisitos

Antes de começar, verifique se você tem as seguintes ferramentas instaladas:

- [Python](https://www.python.org/downloads/) (versão 3.6 ou superior)
- Um navegador padrão com o WhatsApp logado (https://web.whatsapp.com)

## Instalação

1. Clone este repositório:
  ```bash
     git clone https://github.com/RutyRibeiro/wpp-send-img-auto.git
  ```
2. Instale as dependências necessárias:
  ```bash
     pip install -r requirements.txt
  ```

## Uso
1. Certifique-se de que o WhatsApp Web esteja acessível em seu navegador;
2. Abra o arquivo contacts e coloque os contatos quais irão receber a mensagem, um em baixo do outro, como no exemplo a seguir
  ```
      +5511933333333
      +5511900000000
      +5511922222222
  ```
4. Abra a pasta cardapio-do-dia e altere a imagem na pasta img que deseja enviar para os contatos, nomeando como image.jpg;
5. Ainda na pasta cardapio-do-dia altere o arquivo message.txt, colocando a mensagem que deseja enviar;
6. Execute o arquivo main.py e aguarde a finalização do programa.
  ```bash
    python main.py
  ```
