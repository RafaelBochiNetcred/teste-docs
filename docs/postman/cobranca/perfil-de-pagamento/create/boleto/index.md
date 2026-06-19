# Boleto

_Origem: `Cobrança > Perfil de Pagamento > Create > Boleto` na collection Postman._

A chaves que diferenciam um PaymentProfile de boleto são:

- customer
- billingAddress
- shippingAddress.
    

Caso tente-se criar um um novo PaymentProfile com as chaves de um já existente, o PaymentProfile existente será retornado, ao invés de criar um novo.
