# PaymentProfile

_Origem: `Objetos > Charge (Cobrança) > PaymentProfile` na collection Postman._

O PaymentProfile associa o Customer (pagador) com informações de cobrança, como endereço de cobrança e dados do cartão.

Um PaymentProfile único é definido pelas chaves (por método):

- Cartão: Número do cartão (truncado), data de expiração e CPF/CNPJ do Customer
    
- PIX: CPF/CNPJ do Customer, endereço de cobrança e endereço do entrega
    
- Boleto: CPF/CNPJ do Customer, endereço de cobrança e endereço do entrega
    

### Campos PaymentProfile

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `id` | Integer | Identificador único |
| `method` | String | Método:  <br>\- CARD  <br>\- BILLET  <br>\- PIX |
| `isActive` | Boolean | Se o PaymentProfile está ativo |
| `company` | Objeto Company | Estabelecimento do tipo `MERCHANT` ou `MARKETPLACE` dono do PaymentProfile |
| `customer` | Objeto Customer | Pagador associado a este PaymentProfile |
| `billingAddress` | Objeto Address | Endereço de cobrança |
| `shippingAddress` | Objeto Address | Endereço de entrega |
| `cardNumber` | String | **Apenas para o método CARD**  <br>  <br>Número truncado do cartão de crédito |
| `expiryMonth` | Inteiro | **Apenas para o método CARD**  <br>  <br>Mês de expiração do cartão de crédito |
| `expiryYear` | Inteiro | **Apenas para o método CARD**  <br>  <br>Ano de expiração do cartão de crédito |
| `brand` | String | **Apenas para o método CARD**  <br>  <br>Bandeira do cartão  <br>  <br>É usado o formato de arranjo de pagamento, e.g. Visa Crédito = "VCC" |
| `cardHolderName` | String | **Apenas para o método CARD**  <br>  <br>Nome do titular do cartão de crédito |
| `token` | String | **Apenas para o método CARD**  <br>  <br>Token utilizado para reutilizar este cartão em cobranças futuras  <br>  <br>Permite utilizar o cartão sem ter os dados salvos diretamente |
| `voidAt` | Datetime | Data e hora do cancelamento deste PaymentPRofile |
| `rejectedReason` | String | **Apenas para o método CARD**  <br>  <br>Motivo de rejeição da Tokenização |
