Agenda Online IFRN

1. Descrição do projeto

O Agenda Online IFRN é um sistema web desenvolvido com o objetivo de auxiliar professores na organização e no gerenciamento de suas atividades acadêmicas.

A proposta é oferecer um ambiente digital no qual os professores possam organizar seus compromissos, acompanhar avaliações e gerenciar informações relacionadas às suas turmas.

O projeto busca facilitar o planejamento das atividades docentes, centralizando informações em uma única plataforma e contribuindo para uma rotina acadêmica mais organizada.

2. Objetivos

- Desenvolver uma aplicação web para auxiliar na organização das atividades dos professores.
- Permitir o cadastro e a autenticação de usuários.
- Disponibilizar um painel principal para acesso às funcionalidades do sistema.
- Possibilitar o gerenciamento de turmas.
- Organizar compromissos e avaliações em um ambiente centralizado.
- Facilitar o acompanhamento das atividades acadêmicas.

3. Funcionalidades

O projeto encontra-se em desenvolvimento. Suas funcionalidades estão divididas entre recursos já implementados e recursos previstos.

Funcionalidades implementadas

- Autenticação de usuários: acesso ao sistema por meio de e-mail e senha.
- Cadastro de usuários: interface destinada ao registro de novos usuários.
- Encerramento de sessão: permite que o usuário saia de sua conta.
- Painel do professor: página inicial com acesso às principais áreas do sistema.
- Minhas turmas: listagem das turmas cadastradas no sistema.

Funcionalidades em desenvolvimento ou previstas

- Novo compromisso: formulário para registrar atividades e compromissos acadêmicos, integrado ao banco de dados.
- Meus compromissos: área destinada à visualização dos compromissos cadastrados.
- Avaliações: organização de provas, trabalhos avaliativos e reposições.
- Gerenciamento de compromissos: possibilidade futura de editar e excluir registros.

Observação: as aulas regulares não são consideradas compromissos cadastráveis. A associação de uma turma será opcional para compromissos gerais e necessária para avaliações.

4. Tecnologias utilizadas

As principais tecnologias adotadas no desenvolvimento são:

- Python: linguagem de programação utilizada no desenvolvimento do sistema.
- Django: framework web utilizado para estruturar a aplicação, gerenciar rotas, autenticação e integração com o banco de dados.
- HTML5: estruturação das páginas.
- CSS3: estilização e organização visual das interfaces.
- SQLite: banco de dados utilizado na configuração padrão de desenvolvimento, caso mantido no projeto.
- Git: ferramenta de controle de versão.
- GitHub: plataforma utilizada para hospedagem do repositório e compartilhamento do código-fonte.

5. Pré-requisitos

Para executar o projeto em uma máquina local, é necessário possuir:

- Python 3.12 ou versão compatível com as dependências do projeto.
- Git instalado.
- Pip, gerenciador de pacotes do Python.
- Um editor de código, como Visual Studio Code (opcional).

O projeto foi desenvolvido e executado em um ambiente com Python 3.12.3 e Django 6.1.

6. Instalação e execução

Siga as etapas abaixo para obter e executar o projeto em sua máquina.

6.1. Clonar o repositório

Abra o terminal e execute:

    git clone [URL_DO_REPOSITORIO](https://github.com/papageno02/Projecto-de-Agenda-Escolar-IFRN.git)

Substitua "URL_DO_REPOSITORIO" pelo endereço do repositório no GitHub.

6.2. Acessar a pasta do projeto

    cd PROJECTO-AGENDA

6.3. Criar um ambiente virtual

    python -m venv venv

6.4. Ativar o ambiente virtual

  Windows:

    venv\Scripts\activate

  Linux/macOS:

    source venv/bin/activate

6.5. Instalar as dependências

Caso o repositório possua o arquivo "requirements.txt", execute:

    pip install -r requirements.txt

Caso esse arquivo ainda não esteja disponível, instale a versão do Django utilizada no desenvolvimento:

    pip install Django==6.1

6.6. Aplicar as migrações do banco de dados

    python manage.py migrate

6.7. Verificar a configuração do projeto

    python manage.py check

6.8. Iniciar o servidor de desenvolvimento

    python manage.py runserver

Para encerrar o servidor, utilize "CTRL + C" no terminal.

7. Estrutura do projeto

A aplicação está organizada em aplicativos Django, responsáveis por separar as funcionalidades do sistema.

PROJECTO-AGENDA/
│
├── agenda/
│   ├── migrations/
│   ├── templates/
│   │   └── agenda/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── contas/
│   ├── migrations/
│   ├── templates/
│   │   └── contas/
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── setup/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md

Descrição dos principais diretórios e arquivos:

- "agenda/": contém as funcionalidades relacionadas às turmas, compromissos e avaliações.
- "contas/": responsável pelas funcionalidades de cadastro, login e gerenciamento de acesso dos usuários.
- "setup/": contém as configurações gerais do projeto Django.
- "templates/": armazena os arquivos HTML utilizados nas interfaces.
- "models.py": define os modelos de dados utilizados pela aplicação.
- "views.py": contém a lógica responsável pelo processamento das requisições.
- "urls.py": define os endereços e caminhos de acesso às páginas.
- "manage.py": permite executar comandos administrativos do Django.
- "requirements.txt": registra as dependências necessárias para executar o projeto.

8. Equipe

Projeto desenvolvido por:

- Ketlen Taiany Pereira de Meneses
- Luiz Fernando Farias Rodrigues
- Giovanni Brandão Tavares da Silva

Instituição: Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte (IFRN).

9. Status do projeto

O Agenda Online IFRN encontra-se em desenvolvimento, com a estrutura inicial da aplicação, autenticação de usuários, painel principal e gerenciamento inicial de turmas implementados.

As funcionalidades de cadastro e gerenciamento de compromissos e avaliações fazem parte das próximas etapas de desenvolvimento.
