
# Aplicação Django com Celery

## Pré-requisitos

Antes de executar a aplicação, certifique-se de ter os seguintes softwares instalados:

* [Docker](https://www.docker.com/get-started/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Configuração

1.  **Clone o repositório:**

    ```bash
    git clone git@github.com:maindan/tasks.git
    ```

2.  **Construa e execute os containers Docker:**

    Abra o terminal na pasta principal do projeto e rode o comando:
    ```bash
    docker-compose up --build
    ```
    Este comando irá construir as imagens Docker e iniciar os containers para o backend, celery e RabbitMQ. Aguarde alguns instantes até que o celery consiga se conectar ao rabbitmq, no console retornará a mensagem: 
    ```bash
    celery-1 ready
    ```

3.  **Acesse a aplicação:**

    * Django-admin: A API está disponível em `http://localhost:8000/admin`
    * Rota de task: A rota task está disponível em `http://localhost:8000/task`

    Senha e usuário padrão do django admin: admin
