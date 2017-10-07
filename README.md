# Eventex
Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório;
2. Crie um virtualenv com o Python - 3.6.2;
3. Ative o virtualenv;
4. Instale as dependências;
5. Configure a instância com o .env
6. Execute os testes.

``` Console

git clone git@github.com:victoracioly/eventex-victoracioly.git wttd
cd wttd
python -m venv .wttd
(Windows: .wttd/scripts/activate)(source .wttd/bin/activate)
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie ums instância no Heroku;
2. Envie as configurações para o Heroku;
3. Defina uma SECRET_KEY seguda para a instância;
4. Defina DEBUG=False;
5. Configure p serviço de e-mail;
6. Envie o codigo para o Heroku.

``` Console

heroku create minhainstancia;
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`(p/ Unix)
heroku config:set DEBUG=False;
# Configuro o e-mail;
git push heroku master --force.
```