# Conceitos de GraphQL

_Origem: `Por onde começar > Conceitos de GraphQL` na collection Postman._

**1.Consultas (Queries):**  
Quando você precisa acessar informações específicas na nossa API, você utilizará consultas. Por exemplo, você pode querer buscar transações recentes, verificar boletos vencidos ou obter detalhes sobre um pagamento em particular. Cada consulta é cuidadosamente projetada para fornecer os dados necessários para suas operações.

**2. Mutations (Mutações):**  
As mutations são usadas para modificar os dados na nossa API. Elas permitem que você execute ações como criar uma nova cobrança, atualizar o status de um pagamento ou cancelar uma transação. É importante lembrar que mutations afetam diretamente os dados na API e devem ser usadas com cautela.

**3. Schema da API:**  
O Schema da nossa API define a estrutura dos dados disponíveis e as operações que podem ser realizadas. Ele serve como um guia para entender quais dados podem ser acessados e quais ações podem ser executadas. Cada tipo de objeto no Schema possui campos que representam os dados associados a esse objeto.

**4. Argumentos e Variáveis:**  
Ao fazer uma consulta ou uma mutation, você pode precisar fornecer informações específicas, como datas, IDs ou valores. Essas informações são passadas como argumentos na própria consulta ou mutation. Além disso, o uso de variáveis permite tornar suas consultas mais dinâmicas, permitindo que você personalize os valores conforme necessário.

**5. Resolvers e Conexões:**  
Os resolvers são responsáveis por buscar os dados solicitados em uma consulta ou realizar as operações definidas em uma mutation. Eles são como "tradutores" que convertem suas consultas e mutations em ações reais no sistema. Nas consultas que envolvem listas de objetos, como transações ou boletos, usamos o conceito de conexões para navegar entre os objetos relacionados de maneira eficiente.

**6. Tipos de Dados e Relacionamentos:**  
Na nossa API GraphQL, os tipos de dados representam os diferentes recursos disponíveis, como transações, cobranças ou clientes. Esses tipos de dados podem ter relacionamentos entre si, definidos no Schema da API. Por exemplo, uma transação pode estar associada a um cliente ou a uma cobrança. Compreender esses relacionamentos é essencial para criar consultas eficazes e entender como os dados estão conectados na API.
