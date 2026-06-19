# BilletCondition

_Origem: `Objetos > Charge (Cobrança) > BilletCondition` na collection Postman._

Um BilletCondition guarda configurações de um boleto, como a multa ou desconto a serem aplicados. Se as configuração estiver salva em um BilletICondition, seu ID pode ser utilizado para aplicá-la a novos boletos no ChargeCreate.

### Campos do BilletCondition

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `name` | String | Nome da condição |
| `description` | String | Descrição da condição |
| `company` | Objeto Company | Estabelecimento (`MERCHANT`) dono dessa condição |
| `interestType` | String | Tipo do juros:  <br>\- PERCENT  <br>\- VALUE |
| `interestValue` | Decimal | Valor do juros, em relação ao `interestType` |
| `fineType` | String | Tipo da multa:  <br>\- PERCENT  <br>\- VALUE |
| `fine` | Decimal | Valor da multa, em relação ao `fineType` |
| `discountType` | String | Tipo do desconto:  <br>\- PERCENT  <br>\- VALUE |
| `advanceDiscountValue` | String | **Não preenchido junto de outros campos** **`discount`**, além de **`discountType`**  <br>  <br>Desconto aplicado por dias corridos antes do vencimento, em relação a `discountType` |
| `discountValue1` | Decimal | **Sempre preenchido junto de** `discountDateDelta1`  <br>  <br>Valor do desconto até `discountDateDelta1` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta1` | Integer | **Sempre preenchido junto de** `discountValue1`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue1` será aplicado |
| `discountValue2` | Decimal | **Sempre preenchido junto de** `discountDateDelta2`  <br>  <br>Valor do desconto até `discountDateDelta2` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta2` | Integer | **Sempre preenchido** **junto de** `discountValue2`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue2` será aplicado |
| `discountValue3` | Decimal | **Sempre preenchido junto de** `discountDateDelta3`  <br>  <br>Valor do desconto até `discountDateDelta3` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta3` | Integer | **Sempre preenchido junto de** `discountValue2`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue3` será aplicado |
