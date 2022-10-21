# loginproject
Uma simples interface flask de cadastro e login de usuario


Projeto Web de cadastro de usuario 
Autor: Pablo Henrique (BCC)
Concluido em 21/10/2022
Breve descrição:
    Esta interface web faz o cadastro de usuarios para que efetuem o login com seu email e senha.

A ideia era ir além do cadastro/login e confirmar o email do usuario mandando um link de confirmação
porém decidi não arriscar quebrar o prazo limite de entrega do Projeto

executando o main.py usando o proprio pc de host interno para desenvolver

Flask é um framework web escrito em python, é um toolkit WSGI


importando uma classe (Flask) implementa uma Web Server Gateway Interface , quando criado funciona
como um registro central para as funções de visualização, as regras de URL, template, configuração 
 e outros.

sobre os templates usados
Essa parte de codigo é o jinja2 o mecanismo que o flask usa para templates

Esse codigo ta criando um bloco no template 
{%block  title %}

e é nesse bloco que a gente vai colocar o codigo
com todas as outras paginas que usam ele

{% endblock %}
 
