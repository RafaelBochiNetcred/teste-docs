# Introdução

_Origem: `Consultas (queries) > Introdução` na collection Postman._

A API GraphQL oferece dois tipos principais de operações: queries (consultas) e mutations. Nessa seção vamos explicar e exemplicar as queries. Mas primeiro é importante ressaltar a diferença entre uma query e uma mutation.

1. **Queries (Consultas)**: As queries são utilizadas para buscar dados da API. Ao enviar uma query, você especifica os campos que deseja receber como resposta. Em geral, as queries são usadas para recuperar informações de consulta, como dados de leitura de um banco de dados. Para fazer uma query, você pode enviar vários campos para filtrar os dados de acordo com sua necessidade. Por exemplo, você pode buscar por transações específicas usando filtros como datas, tipos de transação ou outros critérios relevantes.
    
2. **Mutations (Mutação)**: As mutations são utilizadas para modificar dados na API. Ao enviar uma mutation, você especifica as operações que deseja realizar, como criar, atualizar ou excluir dados. Cada mutation na nossa API, como o ChargeCreate, recebe um campo de entrada (input) específico para aquela operação. Por exemplo, ao criar uma nova cobrança, você precisa fornecer os detalhes necessários, como o valor da cobrança, o cliente associado e outros dados relevantes.
    

Ao entender a distinção entre queries e mutations, você poderá interagir de forma eficaz com a nossa API GraphQL, buscando dados com queries e modificando-os conforme necessário com mutations.

Quase todos os Objetos da nossa API possuem uma query colocando-se o nome do objeto no plural, e.g. _charges_ é a query para o objeto Charge.
