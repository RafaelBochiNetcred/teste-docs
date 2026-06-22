# Autenticação

A autenticação ocorre por meio do token JWT, mais detalhes sobre este formato em [JWT Docs](https://jwt.io/).

Para autenticar, basta executar uma requisição **tokenAuth** com seu nome de usuário e senha que foram enviados por email. Sendo a solicitação bem-sucedida, você recebe um token utilizado nas requisições subsequentes. A validade do token é de 24h a partir da sua criação.

As demais requisições da API precisam do header HTTP **"Authorization": "JWT** _**token**_**"**, onde _token_ é o token obtido pelo **tokenAuth**.
