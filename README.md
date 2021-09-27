# Carrefour Data Challenge

 O Desafio proporcioou um grande aprendizado, pondo em pratica varias ferramentas aprendidas no bootcamp, e também aprendendo outras para executar o projeto. As etapas feitas no projeto podem ser observadas abaixo.
 
 
# Projeto de uma aplicação da API do twitter.

1. Acessando a API do Twitter usando Tweepy.
2. Introduzindo os dados extraidos do twitter no MondoDB Atlas.
3. Utilizando Heroku para executar os scripts Python totalmente na nuvem.
4. Script para extrair os trending topics a cada 30 minutos.
5. Analise da evolução do volume de um trending Topic.

Trabalhando com a API do twitter foi possivel verificar diversas caracteristicas tanto na maneira que a informação é armazenada no lado do twitter e também o funcionamento do trending topics. A API apresentou informações limitas, apenas o nome do trend e o volume, que muitas da vezes não possuia valores. Já o funciomaneot do trending topics, muitas vezes se a palavra for algo comum ou nome de pessoas famosas ele acaba aumentando o volume de tweets, por exemplo se o nome Michael(jogador de futebol) estiver no trending, qualquer trends referente ao Michael Jackson ou qualquer pessoa chamada Michael que mesmo não tendo a palavra em seu tweet, acaba incluindo no volume de tweets. Foi utilizado o trending de tweets do Brasil, mas quando ele chega a um certo volume e o trending também esta em alta em outros paises, ele retorna o volume total e não apenas da localização.

Foi utilizada o MongoDB para armazenar as informações foi utilizado o modulo M-0(Banco de dados Gratuito na nuvem de 500MB). Na fase de testes essa inserção de dados foi executada em uma maquina local e posteriomente foi exportada para ser executada em um Dyno no Heroku, para que a aplicação executasse na nuvem e colocasse no banco de dados na nuvem.

Observando os dados que foram extraidos durante um dia, foi possivel fazer a evolução dos trendings ao passar do tempo. Também foi possivel observar que 80%~90% dos tweets são relacionados a acontecimentos que foram televisionados. E no futuro conforme o banco de dados tenha mais informações será possivel categorizar os tweets(sports, entretenimento, reality show, etc), e também obter insights referente aos times slots da semana em que esses trendings acontece, por exemplo um jogo de futebol na quarta-feira a noite, os trending começam antes da partida anunciando a expectativa da partida, durante o jogo ele sobe comentando os lances mais marcantes do jogo, e após o jogo aparece alguns trending dos nomes que se destacaram no jogo. Essa mesma analise poderia ser feita para as outras categorias. Essa informação poderia ser utilizada por influenciadores digitais, em que o mais importante é o engajamento com os seus seguidores possibilitando que o influencer possa se preparar e ter conteudo para disponibilizar durante o ponto auto dos trends.

# Lista de funcionalidades a incluir

1. Automatizar a limpeza e analise do banco de dados, removendo entrandas com volume Null e informações redundantes.
2. Criar outro job programado para executar 1 vez ao dia, extraindo as informações do MongoDB estruturando e gravando em outro banco de dados SQL.
3. Fazer analise de sentimento, para detectar o sentimento predominante naquele trending topics e adicionar no banco de dados SQL.
4. Criar um website utilizado Django para disponibilizar a visualização do top 10 trending topics.
5. Disponibilizar a graficos de evolução do volume de tweets.

