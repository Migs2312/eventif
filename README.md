# EventIF

Sistema de evento encomendado pela direção do campus Rio Grande

## Como desenvolver

1. clonar o repositório.
2. crie um virtualenv com python 3.10.
3. ative o seu virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone https://github.com/Migs2312/eventif
cd eventif
python3 -m venv .eventif
source .eventif/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

Eu tive uns problemas com o github, então acabei criando outro repositório