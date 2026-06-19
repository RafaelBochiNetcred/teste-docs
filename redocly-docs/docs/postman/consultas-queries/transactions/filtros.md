# Filtros

_Origem: `Consultas (queries) > Transactions > Filtros` na collection Postman._

`offset(Int)`: Define o deslocamento (quantidade de registros a serem ignorados) na consulta.

`before(String)`: Filtra registros antes de uma determinada referência, identificada pela string fornecida.

`after(String)`: Filtra registros após uma determinada referência, identificada pela string fornecida.

`first(Int)`: Limita o número de registros retornados, começando do início da lista.

`last(Int)`: Limita o número de registros retornados, começando do final da lista.

`created_Gte(DateTime)`: Filtra registros com data de criação maior ou igual a data e hora especificadas.

`created_Lte(DateTime)`: Filtra registros com data de criação menor ou igual da data e hora especificadas.

`billingAt_Gte(Date)`: Filtra registros com data de cobrança maior ou igual a data especificada.

`billingAt_Lte(Date)`: Filtra registros com data de cobrança menor ou igual da data especificada.

`billedAt_Gte(DateTime)`: Filtra registros com data de faturamento maior ou igual a data e hora especificadas.

`billedAt_Lte(DateTime)`: Filtra registros com data de faturamento menor ou igual da data e hora especificadas.

`paidAt_Gte(DateTime)`: Filtra registros com data de pagamento maior ou igual a data e hora especificadas.

`paidAt_Lte(DateTime)`: Filtra registros com data de pagamento menor ou igual da data e hora especificadas.

`dueAt_Gte(Date)`: Filtra registros com data de vencimento maior ou igual a data especificada.

`dueAt_Lte(Date)`: Filtra registros com data de vencimento menor ou igual da data especificada.

`voidAt_Gte(DateTime)`: Filtra registros com data de anulação maior ou igual a data e hora especificadas.

`voidAt_Lte(DateTime)`: Filtra registros com data de anulação menor ou igual da data e hora especificadas.

`installmentNumber(Int)`: Filtra registros com o número de parcela especificado.

`transactionState(String)`: Filtra registros pelo estado da transação.

`authorizationCode(String)`: Filtra registros pelo código de autorização.

`isDisputed(Boolean)`: Filtra registros com base em se há uma disputa associada ou não.

`captureMedium(String)`: Filtra registros pelo meio de captura.

`id(String)`: Filtra registros pelo ID específico.

`id_In([String])`: Filtra registros cujos IDs estão presentes na lista fornecida.

`orderBy(String)`: Especifica a ordem de classificação dos resultados (Lista no próximo tópico).

`method(String)`: Filtra registros pelo método de pagamento.

`customerId(String)`: Filtra registros pelo ID do cliente.

`customerName(String)`: Filtra registros pelo nome do cliente.

`customerDocument(String)`: Filtra registros pelo documento do cliente.

`companyId(String)`: Filtra registros pelo ID da empresa (Company do tipo `MERCHANT`) que criou a transação.

`companyId_In([String])`: Filtra registros cujos IDs de empresa (Company do tipo `MERCHANT`) estão presentes na lista fornecida.

`companyMarketplaceId(String)`: Filtra registros pelo ID do marketplace da empresa (caso disponível).

`companyMarketplaceId_In([String])`: Filtra registros cujos IDs de marketplace da empresa estão presentes na lista fornecida (caso disponível).

`brand(String)`: Filtra registros pela bandeira do cartão.

`cardNumber(String)`: Filtra registros pelo número do cartão.

`cardMode(String)`: Filtra registros pelo modo do cartão.

`chargeType(String)`: Filtra registros pelo tipo de cobrança.

`chargeId(String)`: Filtra registros pelo ID da cobrança.

`contractId(String)`: Filtra registros pelo ID do contrato.

`contractId_IsNull(Boolean)`: Filtra registros com ou sem ID de contrato especificado.

`contractId_In([String])`: Filtra registros cujos IDs de contrato estão presentes na lista fornecida.

`contractIdentifier(String)`: Filtra registros pelo identificador de contrato.

`printUrl(String)`: Filtra registros pela URL de impressão.

`transactionState_In([String])`: Filtra registros cujos estados de transação estão presentes na lista fornecida.

`installmentNumber_Gte(String)`: Filtra registros com número de parcela maior ou igual que o valor especificado.

`installmentNumber_Lte(String)`: Filtra registros com número de parcela menor ou igual que o valor especificado.

`billingCycle_Gte(String)`: Filtra registros com ciclo de cobrança maior ou igual que o valor especificado.

`billingCycle_Lte(String)`: Filtra registros com ciclo de cobrança menor ou igual que o valor especificado.

`amount_Gte(String)`: Filtra registros com valor maior ou igualque o valor especificado.

`amount_Lte(String)`: Filtra registros com valor menor ou igualque o valor especificado.

`chargeLinkId(String)`: Filtra registros pelo ID de link de cobrança.

`terminalSerialNumber(String)`: Filtra registros pelo número de série do terminal.

`terminalId(String)`: Filtra registros pelo ID do terminal.

`extraInfo(String)`: Filtra registros por informações extras.

`chargeServiceCode_In([String])`: Filtra registros cujos códigos de serviço de cobrança estão presentes na lista fornecida.

`protestedStatus(String)`: Filtra registros pelo status de protesto.

`protestedStatus_In([String])`: Filtra registros cujos status de protesto estão presentes na lista fornecida.

`negativeListedStatus(String)`: Filtra registros pelo status de lista negativa.

`negativeListedStatus_In([String])`: Filtra registros cujos status de lista negativa estão presentes na lista fornecida.
