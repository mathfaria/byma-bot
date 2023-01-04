<h1 align="center">🎉 ＢＹＭＡ ＢＯＴ 🎉</h1>

Um script escrito em Python para quem quer comprar ingressos de festas 
universitárias no precinho através do site ```https://byma.com.br/```.



## ✨ FUNCIONALIDADES:
Através do arquivo ```configuracoes.txt```, você pode configurar o bot.
A principal das funcionalidades é a possibilidade de configurar qual
ingresso você deseja comprar.  
No campo ```opcao_ingresso```, você pode escolher se o bot irá comprar o
ingresso mais barato, o mais caro, um aleatório ou um de valor mediano. Além
disso, nos campos ```valor_minimo``` e ```valor_maximo``` você pode definir uma
faixa de preço que deseja, caso o preço dos ingressos esteja fora de tal faixa,
a compra será cancelada.  

**DICA: evite deixar o ```valor_minimo``` igual a zero, a razão disso é que
diversas festas vendem itens do evento junto com os ingressos, como abadás, copos,
etc... É importante definir um valor mínimo para não comprar algum destes itens ao
invés do ingresso.**  

  💰 **FORMA DE PAGAMENTO**: Para efetuar o pagamento, o bot utilizará algum cartão já registrado no próprio site 
do byma, para adicionar um novo cartão como método de pagamento, 
vá em:  ```https://byma.com.br/settings``` e clique em ```Adicionar cartão de crédito```.
Preencha as informações e tudo certo!

----

## ⚙️ CONFIGURANDO O BOT:
Após baixar o repositório, abra o arquivo ```configuracoes.txt```. Neste arquivo há um
breve resumo de como configura-lo, mas o que nos importa é esta parte:  

```
url = https://byma.com.br/event/666666666666666666666666
email = abuble@gmail.com
senha = abublebuble
opcao_ingresso = 1
valor_minimo = 10
valor_maximo = 100
```

Aqui você deve inserir as informações do seu evento e de sua conta. Basta substituir
os valores pelos exemplos ficticios, então se seu 
e-mail é  ```usuariolegal@hotmail.com```, a configuração ficará:  
```email = usuariolegal@hotmail.com```
e assim por diante...


**opcao_ingresso:** Essa opção irá definir qual ingresso o bot irá comprar baseado
nos valores:

    opcao_ingresso = 1; Aqui o bot vai escolher o ingresso mais barato  
    opcao_ingresso = 2; Aqui o bot vai escolher o ingresso mais caro  
    opcao_ingresso = 3; Aqui o bot vai escolher um ingresso aleatório 
    opcao_ingresso = 4; Aqui o bot vai escolher um ingresso no valor mediano

    Então, por exemplo, se tiver ingresso de R$10, R$20 e R$30
     com opcao_ingresso = 1, ele comprará o de R$ 10
     com opcao_ingresso = 2, ele comprará o de R$ 30
     com opcao_ingresso = 3, ele comprará qualquer um
     com opcao_ingresso = 4, ele comprará o de R$ 20

----

## 👨‍💻 RODANDO O BOT:
Para que o bot funcione, você precisará instalar quatro bibliotecas, porém existe
uma forma fácil e simples de baixa-las. Abra o CMD (Prompt de comando) 
na pasta do bot e digite:

```py -m pip install -r requirements.txt```

Com as dependências instaladas, basta digitar

```py byma.py```

----

## 🧬 PRÓXIMOS PASSOS:
As próximas funcionalidades que eu pretendo trazer ao bot são:   
  ☐  Integração com o Telegram   
  ☐  Ampliar testes, visando maior eficiência  
  ☐  Ampliar métodos de pagamento  
  ☐  Interface gráfica
