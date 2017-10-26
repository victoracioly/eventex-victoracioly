# SIGEMH - Sistema Integrado de Gestão de Equipamentos Médico-Hospitalares

Projeto __Open Source__ para Gestão de Equipamentos Médico-Hospitalares.

Um projeto piloto está sendo desenvolvido no Hospital Universitário Onofre Lopes - Natal/RN

## Sou desenvolvedor, como posso contribuir?

1. Clone o repositório do GitHub no botão verde;
2. Crie um ambiente virtual com o Python 3.6 e o Django==1.9.6
3. Ative o virtualenv;
4. Instale as dependências;
5. Configure a instância com o `.env`
6. Execute os testes.

```
git clone https://github.com/victoracioly/sigemh.git
cd sigemh
python3 -m venv .venv
source .venv/bin/activate (Se for no Windows .venv\Scripts\activate)
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
Configure o e-mail;
git push heroku master --force.
```





