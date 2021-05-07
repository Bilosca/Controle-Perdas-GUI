# Controle-Percas-GUI
## Sobre o Projeto
A primeira versão do projeto em command line foi commitada dia 09/12/20.<br>
Como trabalho com reposição de mercadorias, geralmente a vencimentos de produtos, isso me inspirou a criar o projeto Controle-Percas<br>
com o objetivo de facilitar, organizar, e melhorar o gerenciamento do meu trabalho, além de desenvolver minhas habilidades como desenvolvedor, e atrabalhar com tecnologias novas para mim.

Este é o primeiro de vários commits, para a evolução do projeto para uma interface gráfica.

## Tecnologias usadas
este programa utiliza da Linguagem python, e dos seus seguintes módulos:
- sqlite3 -> Sistema de gerenciamento de bancos de Dados Relacionais
- tkinter -> Módulo para criação de Interfaces gráficas

## Atualizações:

### 29/03/21
- Implementação do método de Inserção de Remessa no Banco de Dados
- Junto com o cálculo de diferença de dias para o vencimento de um produto

### 30/03/21
- Criação da Janela  Buscar Produto, para procurar o produto desejado
- Implementação do método de Busca de Remessa no Banco de Dados
- Melhor maneira para preenchimento do Formulário "Setor" na janela Insere Remessa
- Modificações na escrita do código para facilitação de leitura
- Criação da Função que controla e executa as queries

### 01/04/21
- Criação da Janela que possibilita a visualização dos dados usando a classe Treeview do módulo ttk

### 02/04/21
- Aperfeiçoamento da janela de visualização dos dados do produto
- Adicionamento de uma scrollbar dentro da tabela para melhor funcionabilidade e visuabilidade dos dados

### 05/04/21
- Adicionamento do botão para atualização da tabela, que antes era necessário reiniciar o programa para atualizar
- Melhorias para indentificação de produtos perto de vencimento na tabela

### 06/04/21
- Adicionamento da funcionabilidade de atualizar os dias restantes para o vencimento do produto;<br>
a função é chamada assim que o aplicativo é executado, atualizando os dias na tabela.

### 15/04/21
- Após 9 dias trabalhando no código porem sem fazer nenhum commit, decidi fazer mudanças na estrutura do código e adicionamento de novas funções;
- Mudanças nos campos de Inserimento de Dados, cujo agora ficam na janela principal
- Mudanças na função de Inserir Remessa aonde já não abre mais uma nova janela
- Adicionamento da Função de Selecionar um item da tabela com um double-click no mouse, no qual distribuirá seus dados para os campos
- Exclusão da Função de Busca de Remessa para uma melhor análise de como implementar ao código

### 16/04/21
- Inserimento das funções "Editar Remessa" e "Deletar Remessa"
- compactação das funções passadas para resetar os campos aos estados originais, para apenas uma função

### 03/05/21
- Após algumas semanas sem fazer nenhum novo commit, fui realizando mudanças no código, cujo umas não foi ficando do meu agrado, até chegar neste momento;
- Mudanças nas funções e código,
- remoção de botões no menu principal
- inserimento de novos botões e novas funções,
- possibilidade de caminhar por arquivos, abrir um banco de dados ja existente

### 06/05/21
- Modificação da função "adicionarItem" para ordenar a ordem dos items na tabela para uma melhor visualização e leitura dos dados
