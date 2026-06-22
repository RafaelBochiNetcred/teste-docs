# Por onde começar

_Origem: `Por onde começar` na collection Postman._

Esta seção descreve o caminho mínimo para realizar sua primeira integração com a API Netcred. Siga os passos abaixo na ordem apresentada.

<img src="https://content.pstmn.io/828fe784-1e09-47c9-879b-0e6a175ce10d/aW1hZ2UucG5n" width="882" height="660">

---

### 1. Obter credenciais

As credenciais de acesso (usuário e senha) são fornecidas pela equipe Netcred após o cadastro. Sem elas não é possível avançar. Caso não as tenha recebido, entre em contato com o suporte.

---

### 2. Autenticar

Execute a mutation `tokenAuth` com o seu usuário e senha. A resposta contém um token JWT que deve ser enviado em **todas** as requisições subsequentes no header HTTP:

```
Authorization: JWT <token>

 ```

O token tem validade de **24 horas**. Após esse período, repita a autenticação para obter um novo token.

Veja mais detalhes na seção [Autenticação](../autenticacao/index.md).

---

### 3. Obter o ID da empresa (`companyId`)

A grande maioria das chamadas da API exige que você informe um `companyId`. Use a query `getCompanies` para listar todas as empresas disponíveis ao seu usuário e obtenha os IDs necessários.

Veja mais detalhes na [Referência da API](../../../openapi/openapi.yaml).

---

### 4. Criar uma cobrança

Com o `companyId` em mãos, você já pode criar cobranças. A API suporta três modalidades:

- **Boleto bancário**
    
- **Cartão de crédito**
    
- **PIX**
    

→ Veja exemplos e parâmetros na [Referência da API](../../../openapi/openapi.yaml).

---

### 5. Acompanhar o status da transação

Após criar uma cobrança, uma ou mais transações são geradas. Existem duas formas de monitorar o status:

**5a. Consulta ativa (polling)**  
Consulte o estado atual da transação a qualquer momento usando a query de transações.  
→ Consulte a [Referência da API](../../../openapi/openapi.yaml).

**5b. Webhook ✓ Recomendado**  
Configure um Webhook para receber notificações automáticas em tempo real sempre que o status de uma transação mudar. Elimina a necessidade de polling e garante menor latência na atualização do seu sistema.  
→ Seção [Webhook](../webhook/index.md).

---

> **Importante —** acompanhe os estados da transação pela referência da API ou pelos eventos recebidos via Webhook.
  

---

### Leitura complementar

Caso não tenha experiência com GraphQL, recomendamos explorar a seção [Conceitos de GraphQL](conceitos-de-graphql.md) para entender a estrutura das consultas e mutations antes de avançar para chamadas mais complexas.

### Suporte

Caso seu fluxo dependa de algo a mais do que o indicado nesta sessão ou ficar alguma dúvida de como prosseguir você pode entrar em contato com o nosso [Suporte](https://wa.me/+554732270080).

## Nesta secao

- [Conceitos de GraphQL](conceitos-de-graphql.md)
