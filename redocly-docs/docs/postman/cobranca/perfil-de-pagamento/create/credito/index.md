# Crédito

_Origem: `Cobrança > Perfil de Pagamento > Create > Crédito` na collection Postman._

Na cobrança de crédito o paymentProfile exerce um papel fundamental, ajudando na segurança e agilidade em pagamentos recorrentes. As principais vantagens são:

1. **Segurança**: Armazenar os detalhes do cartão de crédito de um cliente de forma segura é fundamental para proteger informações sensíveis. Ao criar um "payment profile", o sistema geralmente não armazena os detalhes do cartão de crédito do cliente diretamente, mas sim um token único que representa esses detalhes. Isso reduz significativamente o risco de exposição a fraudes ou violações de dados, já que os detalhes do cartão não estão armazenados no sistema.
    
2. **Facilidade de uso**: Uma vez que um "payment profile" é criado com sucesso, o token associado a ele pode ser usado para realizar transações futuras sem a necessidade de solicitar novamente os detalhes do cartão de crédito do cliente. Isso proporciona uma experiência conveniente para os clientes, pois não precisam inserir repetidamente as informações do cartão a cada compra.
    
3. **Recorrência e Pagamentos Automáticos**: Em modelos de negócios baseados em assinatura ou pagamentos recorrentes, como serviços de streaming, academias online ou planos de software, os "payment profiles" são essenciais. Uma vez que o cliente tenha fornecido os detalhes do cartão e concordado com os termos do serviço, um "payment profile" é criado e utilizado para cobranças automáticas futuras. Isso simplifica o processo de pagamento para o cliente e garante uma receita recorrente para o fornecedor do serviço.
    
4. **Melhoria da Conveniência do Cliente**: Ao evitar que os clientes tenham que inserir repetidamente os detalhes do cartão, você está melhorando a experiência do cliente, tornando o processo de compra mais rápido e fácil. Isso pode aumentar as taxas de conversão e a satisfação do cliente.
    

  
As chaves que diferenciam um PaymentProfile de cartão são:

- cardNumber
- customer
- expiryYear
- expiryMonth
    

Caso tente-se criar um um novo PaymentProfile com as chaves de um já existente, o PaymentProfile existente será retornado, ao invés de criar um novo.
