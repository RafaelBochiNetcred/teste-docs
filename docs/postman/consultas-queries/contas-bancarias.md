# Contas Bancárias

_Origem: `Consultas (queries) > Contas Bancárias` na collection Postman._

### Contas bancárias

A query `bankAccounts` retorna as contas bancárias cadastradas que o usuário tem permissão de ver, caso seja um usuário de MERCHANT, verá apenas as contas bancárias do próprio estabelecimento, caso seja um usuário de MARKETPLACE, verá as contas de todos os estabelecimentos abaixo do marketplace. Ela é especialmente útil quando você precisa identificar os IDs das contas bancárias para utilizá-los na criação ou atualização de uma PayoutRule — cada item da regra (`ruleItem`) referencia uma conta bancária pelo seu `id`.

---

#### Query básica

``` graphql
query {
  bankAccounts(companyId: "COMPANY_ID", isActive: true) {
    edges {
      node {
        id
        isActive
        holderName
        holderDocument
        agency
        number
        accountType
        pixKeyType
        pixKey
        isLiableAccount
        bank {
          compe
          name
        }
      }
    }
  }
}

 ```

---

#### Filtros disponíveis

Os filtros mais relevantes para o dia a dia são:

| Filtro | Tipo | Descrição |
| --- | --- | --- |
| `companyId` | ID | Filtra pelo ID da empresa. Na prática, sempre informado. |
| `companyId__in` | \[ID\] | Lista de IDs de empresas para busca em múltiplas empresas. |
| `isActive` | Boolean | Filtra pelo status de ativação da conta. Ver nota abaixo. |
| `holderDocument` | String | Documento (CPF ou CNPJ) do titular da conta. Busca parcial. |
| `holderName` | String | Nome do titular da conta. Busca parcial. |
| `bankCompe` | String | Código COMPE do banco. Busca parcial. |
| `agency` | String | Número da agência. Permite busca por valor parcial, ex: filtrar "123" encontra a conta "12345". |
| `number` | String | Número da conta. Permite busca por valor parcial, ex: filtrar "123" encontra o número "12345". |

---

#### Exemplo com múltiplos filtros

Buscar contas ativas de uma empresa cujo titular possui um CNPJ específico:

``` graphql
query {
  bankAccounts(
    companyId: "COMPANY_ID"
    isActive: true
    holderDocument: "12345678000199"
  ) {
    edges {
      node {
        id
        holderName
        holderDocument
        agency
        number
        bank {
          compe
          name
        }
        accountType
      }
    }
  }
}

 ```

---

#### Usando o `id` retornado em uma PayoutRule

O campo `id` retornado por `bankAccounts` é o valor a ser informado como `bankAccountId` em cada item ao criar ou atualizar uma PayoutRule:

``` graphql
mutation {
  payoutRuleCreate(input: {
    companyId: "COMPANY_ID"
    name: "Regra principal"
    ruleItems: [
      {
        bankAccountId: "ID_DA_CONTA_OBTIDO_ACIMA"
        splitType: "PERCENTAGE"
        proportion: "100.00"
      }
    ]
  }) {
    payoutRule {
      id
      name
      cardPayoutAllowed
    }
    errors {
      field
      message
    }
  }
}

 ```

Veja mais detalhes sobre criação de PayoutRules na seção PayoutRule.
