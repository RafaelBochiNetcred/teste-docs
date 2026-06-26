# Webhook

Webhook permitem que o seu sistema receba notificações sobre as cobranças em nossa API. Eles são úteis, por exemplo, para atualizar o status de um boleto que foi pago.

## Referência técnica

- [Ver endpoints REST de Webhooks em Schemas](/schemas)
- [Ver schema OpenAPI completo](/schemas)

Eventos para Webhook e o momento de sua chamada:

- **ANY**
  - Qualquer evento. Um header ainda indica o evento que aconteceu
- **CHARGE_CREATE**
  - Criação da Charge
- **CHARGE_UPDATE**
  - Atualização da Charge
- **CHARGE_VOID**
  - Cancelamento da Charge
- **TRANSACTION_CREATE**
  - Criação da Transaction
- **TRANSACTION_CAPTURE**
  - Captura da Transaction
- **TRANSACTION_UPDATE**
  - Atualização da Transaction, incluindo chamada de atualização e obtenção de pagamento PIX/Boleto
- **TRANSACTION_EXPIRE**
  - Expiração da Transaction
- **TRANSACTION_VOID**
  - Cancelamento da Transaction
- **TRANSACTION_REFUND**
  - Estorno da Transaction
- **TRANSACTION_DISPUTE**
  - Transaction entrou em processo de chargeback
- **TRANSACTION_AUTHORIZE**
  - Emissão/Autorização da Transaction
- **PAYMENT_PROFILE_TOKENIZE**
  - Tokenização do PaymentProfile, sendo sucesso ou não
- **PAYMENT_PROFILE_UPDATE**
  - Atualização do PaymentProfile
- **PAYMENT_PROFILE_DELETE**
  - Desativação/Cancelamento do PaymentProfile
- **PAYMENT_PROFILE_EXPIRING**
  - Falta um mês para a o vencimento do PaymentProfile, no caso de Cartão de crédito
- **WEBHOOK_PING**
  - Ao chamar a mutation de WebhookPing para teste
- **PAYOUT_CREATE**
  - Criação do Payout
- **PAYOUT_SETTLE**
  - Liquidação do Payout
- REGISTRATION_PROCESS_CREATE
  - Criação de RegistrationProcess
- REGISTRATION_PROCESS_UPDATE
  - Atualização de RegistrationProcess
- REGISTRATION_PROCESS_CANCEL
  - RegistrationProcess cancelado
- REGISTRATION_PROCESS_COMPLETE
  - RegistrationProcess concluído

## Nesta secao

- [Requisições enviadas](requisicoes-enviadas/index.md)
- [Schemas REST de Webhooks](/schemas)
