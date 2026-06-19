# PixCondition

_Origem: `Objetos > Charge (Cobrança) > PixCondition` na collection Postman._

Um PixCondition guarda configurações de um PIX, como a multa ou desconto a serem aplicados. Se a configuração estiver salva em um BilletICondition, seu ID pode ser utilizado para aplicá-la a novos boletos no ChargeCreate.

### Campos do PixCondition

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `name` | String | Nome da condição |
| `description` | String | Descrição da condição |
| `company` | Objeto Company | Estabelecimento (`MERCHANT`) dono dessa condição |
| `interestType` | String | **Sempre preenchido junto dos campos** `interestValueType`e `interestValue`  <br>  <br>Tipo do juros:  <br>\- DAYS  <br>\- DAYS_MONTHLY  <br>\- DAYS_ANNUALLY  <br>\- WORKING_DAYS  <br>\- WORKING_DAYS_MONTHLY  <br>\- WORKING_DAYS_ANNUALLY  <br>  <br>A tabela abaixo explica o funcionamento de cada um |
| `interestValueType` | String | **Sempre preenchido junto dos campos** `interestType`e `interestValue`  <br>  <br>TIpo do valor do juros: PERCENT ou VALUE |
| `interestValue` | Decimal | **Sempre preenchido junto dos campos** `interestType`e `interestValueType`  <br>  <br>Valor do juros, com duas casas decimais |
| `fineValueType` | String | **Sempre preenchido junto do campo** `fineValue`  <br>  <br>Tipo do valor da multa: PERCENT ou VALUE |
| `fineValue` | Decimal | **Sempre preenchido junto do campo** `fineValueType`  <br>  <br>Valor da multa |
| `discountType` | String | **Sempre preenchido junto de outros campos** `discount`  <br>  <br>Tipo do desconto:  <br>\- FIXED_DATES  <br>\- DAYS  <br>\- WORKING_DAYS  <br>  <br>A tabela abaixo explica o funcionamento de cada um |
| `discountValueType` | String | Tipo do valor do desconto: PERCENT ou VALUE |
| `discountValue` | Decimal | **Sempre preenchido se**`discountType` for DAYS ou WORKING_DAYS  <br>  <br>Valor do desconto cobrado ao dia |
| `discountValue1` | Decimal | **Sempre preenchido junto dos campos** `discountDateDelta1` e `discountType`\=FIXED_DATES  <br>  <br>Valor do desconto até `discountDateDelta1` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta1` | Inteiro | **Sempre preenchido junto dos campos** `discountDateDelta1` e `discountType`\=FIXED_DATES  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue1` será aplicado |
| `discountValue2` | Decimal | **Sempre preenchido junto do campo** `discountDateDelta2`  <br>  <br>Valor do desconto até `discountDateDelta2` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta2` | Inteiro | **Sempre preenchido junto do campo** `discountValue2`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue2` será aplicado |
| `discountValue3` | Decimal | **Sempre preenchido junto do campo**`discountDateDelta3`  <br>  <br>Valor do desconto até `discountDateDelta3` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta3` | Inteiro | **Sempre preenchido junto do campo** `discountValue2`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue3` será aplicado |

### Valores para o campo `interestType`

| Valor | Descrição |
| --- | --- |
| DAYS | Juros aplicado proporcional ao número de dias corridos |
| DAYS_MONTHLY | **Admite apenas** **`interestValueType`** **PERCENT**  <br>  <br>Juros mensal aplicado proporcional ao número de dias corridos após vencimento |
| DAYS_ANNUALLY | **Admite apenas** **`interestValueType`** **PERCENT**  <br>  <br>Juros anual aplicado proporcional ao número de dias corridos após o venciomento |
| WORKING_DAYS | Juros aplicado proporcional ao número de dias úteis após o vencimento |
| WORKING_DAYS_MONTHLY | **Admite apenas** **`interestValueType`** **PERCENT**  <br>  <br>Juros mensal aplicado proporcional ao número de dias úteis após vencimento |
| WORKING_DAYS_ANNUALLY | **Admite apenas** **`interestValueType`** **PERCENT**  <br>  <br>Juros anual aplicado proporcional ao número de dias úteis após o venciomento |

### Valores para o campo `discountType`

| Valor | Descrição |
| --- | --- |
| DAYS | **Campo** **`discountValue`** **deve ser preenchido**  <br>  <br>Desconto aplicado proporcional ao número de dias corridos antes do vencimento |
| WORKING_DAYS | **Campo** **`discountValue`** **deve ser preenchido**  <br>  <br>Desconto aplicado proporcional ao número de dias úteis antes do vencimento |
| FIXED_DATES | **Campos** **`discountValue[1..3]`** **e** **`discountDateDelta[1..3]`** **devem ser preenchidos**  <br>  <br>Permite que até 3 deltas em relação ao vencimento sejam informados, cada intervalo aplicando um valor de desconto distindo. Pelo menos `discountDateDelta1` e `discountValue1` devem estar preenchidos  <br>  <br>Obs.: `discountDateDelta1` sempre deve ser o maior valor (mais distante antes do vencimento) e `discountDateDelta3` sempre deve ser o menor valor (mais próximo antes do vencimento) |
