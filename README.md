# CRUD Web App
Web app que cadastra usuários de acordo com suas informações pessoais.
Desenvolvido em Django 3.1 (Python 3.8.2), o app pode ser testado pelo [pythonanywhere](http://frutose.pythonanywhere.com/usuarios/).

Para uso local, é necessário realizar as seguintes etapas (caso não tenha o Python instalado, é possível baixá-lo por [aqui](https://www.python.org/downloads/)), além de assegurar que a versão do python seja 3.8.2 ou superior:

### Instalar Django em sua máquina
O django pode ser instalado utilizando o pip. Se você estiver no Windows, abra o cmd e digite o comando
```
python -m pip install django
```
e aguarde a instalação. Caso já tenha Django em sua máquina, verifique a versão, pois há alguns métodos utilizados neste projeto que são novos da versão 3.1.
Para isso, basta digitar o comando no cmd
```
python -m django --version
```
Caso a versão seja inferior à 3.1, é possível atualizá-lo com
```
python -m pip install -U Django
```

### Clonar este repositório
Para clonar este repositório com o [Git](https://git-scm.com/), basta ir à pasta em que se deseja fazer a clonagem, pelo cmd,
```
cd CAMINHO_DO_DIRETORIO
```
e utilizar o comando clone do Git:
```
git clone https://github.com/robertobetini/cadastro-web-app
```

Confira se o arquivo manage.py está presente e guarde o caminho até ele.

### Abrindo um servidor local
O Django possui internamente um comando para abrir um servidor e hostear localmente as páginas web. Para isso, vá até o diretório de manage.py, no cmd, e digite o comando
```
python manage.py check
```
para verificar se há algum erro no app clonado. Caso se verifique algum erro, confira as versões do Python e do Django instaladas.
Digite os comandos para fazer as migrações do Model para o Database
```
python manage.py makemigrations
python manage.py migrate
```

Para abrir o servidor, basta inserir o comando
```
python manage.py runserver
```
e para acessar o app, basta ir, com algum browser, ao endereço mencionado no console após o servidor abrir (usualmente o endereço é 127.0.0.0:8000).
