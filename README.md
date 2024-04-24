# Projeto MyTasks com API Rest Django 📝✅

Este é um projeto de exemplo que demonstra como criar um sistema CRUD de tarefas utilizando uma API REST Django para o backend e jQuery para consumir essa API no frontend.

## Descrição ℹ️

O projeto consiste em uma aplicação web simples para gerenciar tarefas. Ele permite aos usuários criar, visualizar, atualizar e excluir tarefas. A API REST Django é responsável por fornecer endpoints para realizar essas operações CRUD, enquanto o jQuery é usado no frontend para interagir com esses endpoints e exibir os dados na interface do usuário.

![image](https://github.com/djherondhy/task-django-crud/assets/35778998/22a3f5d9-ea17-4e79-ba5c-96e6056e9f30)
![image](https://github.com/djherondhy/task-django-crud/assets/35778998/63edce00-08c7-4a0a-9977-ae17e7877145)

## Funcionalidades 🛠️

- Criar uma nova tarefa
- Visualizar todas as tarefas existentes
- Atualizar o título de uma tarefa existente
- Marcar uma tarefa como concluída ou pendente
- Excluir uma tarefa existente

## Tecnologias Utilizadas 🚀

- Django: Framework web para o backend
- Django Rest Framework (DRF): Biblioteca para construção de APIs RESTful em Django
- jQuery: Biblioteca JavaScript para manipulação de documentos HTML e interação com APIs
- HTML e CSS: Para a estrutura e o estilo da interface do usuário

## Como Utilizar 📋

1. **Clonar o Repositório**: Clone este repositório em seu computador local.

2. **Configurar o Ambiente Virtual (Opcional)**: Crie e ative um ambiente virtual Python para instalar as dependências do projeto.

    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```

3. **Instalar Dependências**: Instale as dependências do projeto listadas no arquivo `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4. **Executar as Migrações**: Aplique as migrações para configurar o banco de dados SQLite.

    ```bash
    python manage.py migrate
    ```

5. **Iniciar o Servidor Django**: Inicie o servidor Django.

    ```bash
    python manage.py runserver
    ```

6. **Acessar o Frontend**: Navegue até a pasta do frontend e abra o arquivo HTML principal em seu navegador para acessar a aplicação.


