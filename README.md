# Sistemas-de-Recomenda-o
Configurando o ambiente para rodar o sistema

Faça o download do sdk apropriado para o seu sistema neste link https://cloud.google.com/sdk/docs

Abra o terminal e execute os seguintes comandos:

cd [diretório onde o sdk foi salvo]

tar -zvxf [nome do .tar.gz baixado]

cd google-cloud-sdk…

mv google-cloud-sdk ~/

cd

./google-cloud-sdk/install.sh (siga as dicas que o instalador dará)

bash

gcloud init (Siga as dicas que serão dadas pelo inicializador)

Inicializando aplicação

Faça um clone deste repositório
No terminal, navegue até o diretório do projeto onde está localizado o arquivo app.yaml
digite o comando dev_appserver.py .

Acesse o localhost:8080 para ver o sistema em funcionamento. 
