# trabalho2-redes
Este repositório contém os arquivos necessários para implementar o Trabalho 2 da disciplina de Laboratório de Redes, o qual estabelece uma comunicação multicasting entre clientes (chat).

Para rodar o programa, deve-se primeiro realizar a instalação do Docker.
Por gentileza siga os passos a seguir de acordo com o seu sistema operacional.

Para instalar no Ubuntu-> https://docs.docker.com/engine/install/ubuntu/

Para instalar no Windows-> https://docs.docker.com/desktop/windows/install/

Após a realização da instalação e verificação do correto funcionamento do Docker, utilize o comando abaixo para colocar o servidor em funcionamento:

sudo docker run -it --rm --network=host tarsisn/servidor python3 servidor.py (ip do servidor aqui sem parenteses)

Pronto, se tudo der certo, você verá uma mensagem que o servidor está funcionando.

Para a utilização do cliente, execute o comando abaixo:

sudo docker run -it --rm --network=host tarsisn/cliente python3 cliente.py (ip do servidor aqui sem parenteses)

Pronto! A aplicação já está em funcionamento.

Desenvolvido por Taris Nogueira e José Neto.
