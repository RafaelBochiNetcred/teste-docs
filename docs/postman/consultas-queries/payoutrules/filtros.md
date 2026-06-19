# Filtros

_Origem: `Consultas (queries) > PayoutRules > Filtros` na collection Postman._

`offset(Int)`: Define o deslocamento (quantidade de registros a serem ignorados) na consulta.

`before(String)`: Filtra registros antes de uma determinada referência, identificada pela string fornecida.

`after(String)`: Filtra registros após uma determinada referência, identificada pela string fornecida.

`first(Int)`: Limita o número de registros retornados, começando do início da lista.

`last(Int)`: Limita o número de registros retornados, começando do final da lista.

`name(String)`: Filtra registros pelo nome do payoutRule.

`companyId(String)`: Filtra registros pelo ID da empresa (Company do tipo `MERCHANT`) que criou a transação.

`isPrimary(String)`: Filtra registros onde a payoutRule é a padrão ou não.

`isActive(String)`: Filtra registros onde a payoutRule está ativa ou não.

`cardPayoutAllowed(Boolean)`: Filtra PayoutRules que podem ser utilizados para vendas de cartão de crédito.
