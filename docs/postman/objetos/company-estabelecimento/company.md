# Company

_Origem: `Objetos > Company (Estabelecimento) > Company` na collection Postman._

A Company é um empresa. As empresas são dividas nos seguintes tipos, indicados também pelo campo `companyType`:

- FACILITATOR: Sub-adquirente, responsável pelo gerenciamento e liquidação dos recebíveis (é o caso da Netcred)
    
- MARKETPLACE: Marketplaces possuem várias empresas abaixo de si, para as quais usuários deste Marketplace podem criar cobranças. Um Marketplace pode ter sub-marketplaces e vice-versa.
    
- FINANCIER: Financiador, responsável por financiar operações de crédito através de Contracts, que trocam a titularidades de recebíveis a seu favor
    
- MERCHANT: Estabelecimento que possuem cobranças e os únicos para os quais cobranças podem ser criadas
    
- REFERRER: Empresa que indica outras e ganha uma comissão das vendas geradas por elas
    

### Campos de Company

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `id` | Inteiro | Identificador único |
| `companyType` | String | Tipo da empresa:  <br>\- FACILITATOR  <br>\- MARKETPLACE  <br>\- FINANCIER  <br>\- MERCHANT  <br>\- REFERRER |
| `companyState` | String | Estado da empresa:  <br>\- ACTIVE  <br>\- INACTIVE  <br>\- SUSPENDED  <br>\- ONGOING  <br>\- AWAITING_APPROVAL  <br>\- DENIED |
| `name` | String | Nome fantasia |
| `legalName` | String | Razão social |
| `cnae` | String | Código de Atividade Econômica (CNAE) |
| `documentType` | String | Tipo do documento: CPF ou CNPJ |
| `document` | String | Número do documento |
| `email` | String | Email principal da empresa |
| `phone` | String | Telefone principal da empresa |
