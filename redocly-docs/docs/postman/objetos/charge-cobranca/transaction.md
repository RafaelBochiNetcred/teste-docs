# Transaction

_Origem: `Objetos > Charge (Cobrança) > Transaction` na collection Postman._

A Transaction são os 'pagamentos' de fato, ela corresponde a um boleto, PIX ou pagamento de cartão.

Os objetos \[nome\]Info acrescentam à Transaction informações mais específicas de cada método (Cartão, Pix ou Boleto). Esses objetos contém informações "repetidas" de outros, isso acontece porque um PaymentProfile, por exemplo, pode mudar o seu `billingAddress`, enquanto os dados do `billingInfo` permancem estáticos depois que uma transação é emitida/autorizada. Os objetos Info também são apresentados nesta seção.

### Campos da Transaction

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `id` | Inteiro | Identificador único |
| `uuid` | Strign | Identificador único em formato UUID |
| `amount` | Decimal | Valor nominal |
| `paidAmount` | Decimal | Valor pago  <br>  <br>Pode ser diferente do `amount` em boleto e PIX, devido a descontos ou acréscimos |
| `refundedAmount` | Decimal | Valor estornado  <br>  <br>É menor ou igual ao valor pago |
| `transactionState` | String | Estado da Transaction:  <br>\- SCHEDULED  <br>\- REJECTED  <br>\- VOIDED  <br>\- BILLED  <br>\- EXPIRED  <br>\- PAID  <br>\- PARTIALLY_REFUNDED  <br>\- REFUNDED  <br>\- IN_ANALYSIS  <br>\- MANUAL_ANALYSIS  <br>  <br>Para mais informações sobre cada uma consulte a tabela abaixo. |
| `method` | String | Método:  <br>\- BILLET: Boleto  <br>\- PIX  <br>\- CARD: Cartão de crédito |
| `installmentNumber` | Inteiro | **Apenas para o método CARD**  <br>Número de parcelas do crédito |
| `captureMedium` | String | Método de 'captura':  <br>\- ONLINE: transações criadas a partir da API  <br>\- TERMINAL: transações provenientes de terminais POS ou QRCode estático |
| `rejectedReason` | String | Motivo da recusa |
| `billingAt` | Date | Data na qual **ocorrerá** a emissão/autorização |
| `billedAt` | Datetime | Data e hora na qual **ocorreu** a emissão/autorização |
| `dueAt` | Date | Data na qual **ocorrerá** a captura, no método CARD.  <br>  <br>Data de vencimento para BILLET e PIX. |
| `paidAt` | Datetime | Data e hora no qual **ocorreu** o pagamento/captura.  <br>  <br>No caso do boleto, pode ser que a hora não esteja correta, pois apenas temos acesso à data do pagamento. |
| `processedAt` | Datetime | Data e hora do processamento da transação, normalmente é igual/proximo a `paidAt`.  <br>  <br>Essa data é usada como base para a geração das liquidações |
| `voidAt` | Datetime | Data e hora na qual ocorreu o cancelamento desta Transaction |
| `voidReason` | String | Motivo do cancelamento |
| `manualCapture` | Boolean | **Apenas para o método CARD**  <br>Se a captura será manual, i.e. não ocorrerá de forma automática |
| `isDisputed` | Boolean | Se a Transaction está em processo de chargeback |
| `attempts` | Inteiro | **Apenas para o método CARD**  <br>Numero de tentativas de autorização efetuadas |
| `billExpiryDate` | Date | **Apenas para os métodos BILLET e PIX**  <br>  <br>Data na qual uma emissão irá expirar após a data de vencimento (`dueAt`)  <br>  <br>Após esta data a transação passa para o estado EXPIRED |
| `refundMaxDate` | Date | Data máxima na qual a transação poderá ser estornada |
| `billingCycle` | Inteiro | Número sequencial da Transaction dentro da Charge |
| `printUrl` | String | **Apenas para o método BILLET**  <br>Link encurtado para download do boleto |
| `charge` | Objeto Charge | Cobrança a qual esta Transaction pertence |
| `company` | Objeto Company | Estabelecimento (`MERCHANT`) dono desta Transaction |
| `customer` | Objeto Customer | Pagador |
| `paymentProfile` | Objeto PaymentProfile | Informações de cobrança para a Transaction |
| `billetCondition` | Objeto BilletCondition | **Apenas para o método BILLET**  <br>Configurações de boleto |
| `pixCondition` | Objeto PixCondition | **Apenas para o método PIX**  <br>Configurações de PIX |
| `chargeLink` | Objeto ChargeLink | ChargeLink associado, caso a Charge tenha sido criada a partid de um |
| `payoutRule` | Objeto PayoutRule | **Mutuamente exclusivo com** **`contract`**  <br>  <br>Split de pagamento |
| `contract` | Objeto Contract | **Mutuamente exclusivo com** **`payoutRule`**  <br>  <br>Contrato associado a esta cobrança. Ele vai direcionar os recebíveis para um Financiador |
| `cardInfo` | Objeto CardInfo | **Apenas para o método CARD**  <br>Informações específicas sobre o cartão, como a número do cartão truncado e a bandeira |
| `billetInfo` | Objeto BilletInfo | **Apenas para o método BILLET**  <br>Informações específicas sobre o boleto, incluindo configurações de juros e afins |
| `pixInfo` | Objeto PixInfo | **Apenas para o método PIX**  <br>Informações específicas sobre o PIX, incluindo configurações de juros e afins |
| `billingInfo` | Objeto BillingInfo | Informações de cobrança, como endereço e pagador |

### Estados da Transaction

| Estado | Descrição |
| --- | --- |
| SCHEDULED | Agendada, será emitida/autorizada em `billingAt` |
| REJECTED | **Apenas para CARD**  <br>Rejeitada na autorização, e.g. falta de fundos |
| VOIDED | Cancelada |
| BILLED | Emitida/Autorizada |
| EXPIRED | "Vencida", a data de vencimento (`dueAt`) passou de determinada número de dias  <br>  <br>Para todos os efeitos é equivalente a VOIDED |
| PAID | Paga |
| PARTIALLY_REFUNDED | Parcialmente estornada  <br>`0 < refundedAmount < paidAmount` |
| REFUNDED | Totalmente estornada  <br>`refundedAmount = paidAmount` |
| IN_ANALYSIS | Em análise de risco  <br>Irá será aprovada ou rejeitada automaticamento em até 2h |
| MANUAL_ANALYSIS | Em análise manual  <br>Netcred está verificando os dados e irá aprovar ou rejeitar em breve |

### Fluxos de estado da Transction por método

<img src="https://content.pstmn.io/41e54e3e-3224-4d85-ad26-8ba12ba47733/Rmx1eG8gVHJhbnNhw6fDo28gQm9sZXRvLmpwZw==" alt="Boleto">

<img src="https://content.pstmn.io/6447f5b8-b049-4917-926e-ae07de285e29/Rmx1eG8gVHJhbnNhw6fDo28gUGl4LmpwZw==" alt="Pix">

<img src="https://content.pstmn.io/e0f1342a-b991-4d93-b1b6-f069d7e323a3/Rmx1eG8gVHJhbnNhw6fDo28gQ2FydMOjby5qcGc=" alt="Cartão%20de%20Crédito">

### Campos do BillingInfo

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `billingAddressNumber` | String | Número do endereço |
| `billingAddressStreet` | String | Rua do endereço |
| `billingAddressDistrict` | String | Bairro/Distrito do endereço |
| `billingAddressCity` | String | Cidade do endereço |
| `billingAddressState` | String | Sigla do estado do endereço |
| `billingAddressAdditionalDetails` | String | Informações adicionais do endereço, e.g. número do apartamento |
| `billingAddressZipCode` | String | CEP do endereço, apenas números |
| `shippingAddressNumber` | String | Número do endereço |
| `shippingAddressStreet` | String | Rua do endereço |
| `shippingAddressDistrict` | String | Bairro/Distrito do endereço |
| `shippingAddressCity` | String | Cidade do endereço |
| `shippingAddressState` | String | Sigla do estado do endereço |
| `shippingAddressAdditionalDetails` | String | Informações adicionais do endereço, e.g. número do apartamento |
| `shippingAddressZipCode` | String | CEP do endereço, apenas números |
| `customerName` | String | Nome do pagador |
| `customerEmail` | String | Email do pagador |
| `customerDocumentType` | String | Tipo do documento do pagador (CPF ou CNPJ) |
| `customerDocument` | String | Documetno do pagador |
| `customerPhone` | String | Número de telefone do pagador |
| `customerBirthDate` | Date | Data de nascimento do pagador |
| `customerGender` | String | Gênero do pagador |

### Campos do CardInfo (Cartão)

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `cardNumber` | String | Número do cartão truncado, e.g. "497010XXXXXX0048" |
| `cardMode` | String | "Modo" do cartão utlizado:  <br>\- CREDIT: Crédito  <br>\- DEBIT: Débito (apenas de terminal)  <br>\- PRE_PAID: Crédito pré-pago |
| `cardHolderName` | String | Titular do cartão |
| `expiryMonth` | Inteiro | Mês de expiração |
| `expiryYear` | Inteiro | Ano de expiração |
| `brand` | String | Bandeira do cartão  <br>  <br>É usado o formato de arranjo de pagamento, e.g. Visa Crédito = "VCC" |

### Campos do BilletInfo (Boleto)

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `billetType` | String | Tipo do boleto:  <br>\- NORMAL: sem QRCode PIX  <br>\- HYBRID: com QRCode PIX |
| `digitableLine` | String | Linha digitável  <br>  <br>Preenchido após a emissão |
| `barCode` | String | Código de barras  <br>  <br>Preenchido após a emissão |
| `txid` | String | Identificador associado ao PIX do boleto  <br>  <br>Preenchido após a emissão |
| `pixCopyPaste` | String | Código PIX copia e cola  <br>  <br>Preenchido após a emissão  <br>  <br>Obs.: para gerar a imagem do QRCode basta usar este código em uma biblioteca de QRCode |
| `interestType` | String | Tipo do juros:  <br>\- PERCENT  <br>\- VALUE |
| `interestValue` | Decimal | Valor do juros, em relação ao `interestType` |
| `fineType` | String | Tipo da multa:  <br>\- PERCENT  <br>\- VALUE |
| `fine` | Decimal | Valor da multa, em relação ao `fineType` |
| `discountType` | String | Tipo do desconto:  <br>\- PERCENT  <br>\- VALUE |
| `advanceDiscountValue` | String | **Não preenchido junto de outros campos****`discount`****, além de** **`discountType`**  <br>  <br>Desconto aplicado por dias corridos antes do vencimento, em relação a `discountType` |
| `discountValue1` | Decimal | **Sempre preenchido junto de** `discountDateDelta1`  <br>  <br>Valor do desconto até `discountDateDelta1` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta1` | Integer | **Sempre preenchido junto de** `discountValue1`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue1` será aplicado |
| `discountValue2` | Decimal | **Sempre preenchido junto de** `discountDateDelta2`  <br>  <br>Valor do desconto até `discountDateDelta2` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta2` | Integer | **Sempre preenchido** **junto de** `discountValue2`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue2` será aplicado |
| `discountValue3` | Decimal | **Sempre preenchido junto de** `discountDateDelta3`  <br>  <br>Valor do desconto até `discountDateDelta3` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta3` | Integer | **Sempre preenchido junto de** `discountValue2`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue3` será aplicado |

### Campos do PixInfo (PIX)

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `pixType` | String | Tipo do PIX:  <br>\- IMMEDIATE: expira em pouco tempo (gerado no ChargeLink)  <br>\- WITH_DUE_DATE: Semelhante a boleto, com configurações de multa e etc (gerado no ChargeCreate)  <br>\- STATIC: pagamento por QRCode estático do estabelecimento  <br>\- TERMINAL: pagamento por terminal POS |
| `e2eid` | String | Identificador único do pagametno PIX no Bacen  <br>  <br>Preenchido após o pagamento |
| `pixCopyPaste` | String | Código PIX copia e cola  <br>  <br>Preenchido após a emissão  <br>  <br>Obs.: para gerar a imagem do QRCode basta usar este código em uma biblioteca de QRCode |
| `expiresAt` | Datetime | Data e hora de expiração do PIX se o `pixType` for IMMEDIATE |
| `interestType` | String | **Sempre preenchido junto dos campos** `interestValueType`e `interestValue`  <br>  <br>Tipo do juros:  <br>\- DAYS  <br>\- DAYS_MONTHLY  <br>\- DAYS_ANNUALLY  <br>\- WORKING_DAYS  <br>\- WORKING_DAYS_MONTHLY  <br>\- WORKING_DAYS_ANNUALLY  <br>  <br>Para a explicação de cada um, consulte a documentação de PixCondition |
| `interestValueType` | String | **Sempre preenchido junto dos campos** `interestType`e `interestValue`  <br>  <br>TIpo do valor do juros: PERCENT ou VALUE |
| `interestValue` | Decimal | **Sempre preenchido junto dos campos** `interestType`e `interestValueType`  <br>  <br>Valor do juros, com duas casas decimais |
| `fineValueType` | String | **Sempre preenchido junto do campo** `fineValue`  <br>  <br>Tipo do valor da multa: PERCENT ou VALUE |
| `fineValue` | Decimal | **Sempre preenchido junto do campo** `fineValueType`  <br>  <br>Valor da multa |
| `discountType` | String | **Sempre preenchido junto de outros campos** `discount`  <br>  <br>Tipo do desconto:  <br>\- FIXED_DATES  <br>\- DAYS  <br>\- WORKING_DAYS  <br>  <br>Para a explicação de cada um, consulte a documentação de PixCondition |
| `discountValueType` | String | Tipo do valor do desconto: PERCENT ou VALUE |
| `discountValue` | Decimal | **Sempre preenchido se**`discountType` for DAYS ou WORKING_DAYS  <br>  <br>Valor do desconto cobrado ao dia |
| `discountValue1` | Decimal | **Sempre preenchido junto dos campos** `discountDateDelta1` e `discountType`\=FIXED_DATES  <br>  <br>Valor do desconto até `discountDateDelta1` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta1` | Inteiro | **Sempre preenchido junto dos campos** `discountDateDelta1` e `discountType`\=FIXED_DATES  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue1` será aplicado |
| `discountValue2` | Decimal | **Sempre preenchido junto do campo** `discountDateDelta2`  <br>  <br>Valor do desconto até `discountDateDelta2` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta2` | Inteiro | **Sempre preenchido junto do campo** `discountValue2`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue2` será aplicado |
| `discountValue3` | Decimal | **Sempre preenchido junto do campo** `discountDateDelta3`  <br>  <br>Valor do desconto até `discountDateDelta3` dias antes do vencimento, em relação a `discountType` |
| `discountDateDelta3` | Inteiro | **Sempre preenchido junto do campo** `discountValue2`  <br>  <br>Número de dias antes do vencimento até o qual o desconto `discountValue3` será aplicado |
