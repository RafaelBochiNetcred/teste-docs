# Paginação

_Origem: `Consultas (queries) > Paginação` na collection Postman._

Nossas queries suportam paginação para controlar o volume de resultados retornados em uma única requisição. A paginação permite que você **recupere subconjuntos de resultados**, facilitando a navegação em grandes conjuntos de dados.

### Parâmetros de Paginação

- **first** (opcional) – _número inteiro_  
    Quantidade máxima de itens que devem ser retornados na resposta, este filtro tem o limite de 200.  
    Exemplo: `first=10` retorna até 10 itens por página.
    

- **offset** (opcional) – _número inteiro_  
    Índice de início da página, indicando quantos resultados devem ser “pulados” antes de retornar os itens.  
    Exemplo: `offset=20` faz a API pular os primeiros 20 itens e retornar os resultados a partir daí.
    

- **orderBy** (opcional) – _string_  
    Campo pelo qual os resultados devem ser ordenados. Por padrão, a ordenação é feita por um campo padrão da API (por exemplo, `createdAt` ou outro definido pela rota).  
    Exemplo: `orderBy=-createdAt` ordena pela data de criação dos itens.
    

### Como Funciona

## Primeira Página

Consulta da primeira página (primeiros 50 registros):

``` graphql
query {
  transactions(first: 50, offset: 0, orderBy: "-due_at") {
    edges {
      node {
        id
        dueAt
        paidAt
        voidAt
        billingAt
        processedAt
        isDisputed
        method
        amount
        paidAmount
        authorizationCode
        installmentNumber
        transactionState
        rejectedReason
        captureMedium
        voidReason
      }
    }
  }
}

 ```

Nesse exemplo:

- A API retorna até 5**0 itens** (por conta do `first=50`).
    
- A partir do primeiro registro (pois `offset=0`).
    
- Ordenados pelo campo `due_at` de forma decrescente.
    
- Retorna os elementos 1 até 50
    

## Segunda Página

Para obter a segunda página, basta incrementar o `offset` pelo valor utilizado em `first`.

``` graphql
query {
  transactions(first: 50, offset: 50, orderBy: "-due_at") {
    edges {
      node {
        id
        dueAt
        paidAt
        voidAt
        billingAt
        processedAt
        isDisputed
        method
        amount
        paidAmount
        authorizationCode
        installmentNumber
        transactionState
        rejectedReason
        captureMedium
        voidReason
      }
    }
  }
}

 ```

O que muda:

- Retorna 50 elementos ignorando os primeiros 50 elementos
    
- Retorna os elementos 51 até 100
    

Para a próxima página basta acrescentar +50 ao offset e assim por diante até encerrar os objetos.

### Exemplo de Resposta

``` graphql
{
  "data": {
    "transactions": {
      "edges": [
        {
          "node": {
            "id": "1",
            "dueAt": "2025-02-10T00:00:00Z",
            "paidAt": "2025-02-09T14:32:10Z",
            "voidAt": null,
            "billingAt": "2025-02-01T08:00:00Z",
            "processedAt": "2025-02-09T14:31:58Z",
            "isDisputed": false,
            "method": "PIX",
            "amount": 150.00,
            "paidAmount": 150.00,
            "authorizationCode": "12345",
            "installmentNumber": 1,
            "transactionState": "PAID",
            "rejectedReason": null,
            "captureMedium": "ONLINE",
            "voidReason": null
          }
        },
        {
          "node": {
            "id": "2",
            "dueAt": "2025-02-08T00:00:00Z",
            "paidAt": null,
            "voidAt": null,
            "billingAt": "2025-02-01T09:15:00Z",
            "processedAt": null,
            "isDisputed": false,
            "method": "BILLET",
            "amount": 320.50,
            "paidAmount": 0.00,
            "authorizationCode": null,
            "installmentNumber": 1,
            "transactionState": "PENDING",
            "rejectedReason": null,
            "captureMedium": "TERMINAL",
            "voidReason": null
          }
        },
        {
          "node": {
            "id": "3",
            "dueAt": "2025-02-05T00:00:00Z",
            "paidAt": null,
            "voidAt": "2025-02-04T11:20:45Z",
            "billingAt": "2025-02-01T10:45:00Z",
            "processedAt": null,
            "isDisputed": false,
            "method": "CARD",
            "amount": 89.90,
            "paidAmount": 0.00,
            "authorizationCode": null,
            "installmentNumber": 1,
            "transactionState": "VOIDED",
            "rejectedReason": null,
            "captureMedium": "ONLINE",
            "voidReason": "REQUESTED_BY_CUSTOMER"
          }
        }
      ]
    }
  }
}

 ```

### Notas

- Se **nenhum parâmetro de paginação** for informado, a API irá retornar um número padrão de itens (200 items).
    
- O parâmetro `orderBy` ajuda a garantir que a páginação seja **determinística** (a ordem dos itens não muda entre as páginas).
    
- Ajustar corretamente o `offset` e o `first` permite que você navegue entre as páginas de resultados de forma previsível.
