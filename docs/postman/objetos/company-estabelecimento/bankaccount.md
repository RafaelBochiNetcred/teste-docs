# BankAccount

_Origem: `Objetos > Company (Estabelecimento) > BankAccount` na collection Postman._

Um objeto BankAccount guarda os dados de uma conta bancária da Company. Normalmente elas são utilizadas em PayoutRules para formar um split de pagamento.

### Campos BankAccount

| Nome | Tipo |  |
| --- | --- | --- |
| `id` | Inteiro | Identificador único |
| `bank` | Objeto Bank | Banco da conta bancária |
| `bank.ispb` | String | Código ISPB do banco |
| `bank.compe` | String | Código COMPE do banco |
| `documentType` | String | Tipo do documento do titular da conta:  <br>CPF ou CNPJ |
| `holderDocument` | String | Documento do titular da conta |
| `holderName` | String | Nome do titular da conta |
| `agency` | String | Codigo da agência, com dígito verificador |
| `number` | String | Número da conta, com dígito verificador |
| `accountType` | String | Tipo da conta:  <br>\- CC: Conta Corrente  <br>\- CD: Conta de Depósito  <br>\- PG: Conta de Pagamento  <br>\- PP: Conta Poupança |
| `transferFee` | Decimal | Taxa de transferência |
| `pixKeyType` |  | TIpo da chave PIX:  <br>\- EMAIL  <br>\- CPF  <br>\- CNPJ  <br>\- PHONE  <br>\- RANDOM_KEY |
| `pixKey` |  | Chave PIX |
