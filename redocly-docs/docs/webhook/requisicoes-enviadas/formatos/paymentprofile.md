# PaymentProfile

### Formato PaymentProfilePayload

| Nome | Exemplo | Descrição |
| --- | --- | --- |
| `id` | 16182 | Identificador único do PaymentProfile |
| `method` | "BILLET" | Método: CARD, BILLET ou PIX |
| `is_active` | true | Se o PaymentProfile está ativo |
| `card_number` | "497010XXXXXX0048" | Número do cartão de crédito |
| `expiry_month` | 6 | Mês de expiração do cartão de crédito |
| `expiry_year` | 2028 | Ano de expiração do cartão de crédito |
| `brand` | "VCC" | Bandeira do cartão de crédito, em formato arranjo de pagamento |
| `card_holder_name` | "Dono Cartão" | Nome do titular do cartão de crédito |
| `void_at` | "2023-05-30T03:47:20.628345Z" | Date e hora do cancelamento do PaymentProfile |
| `last_operation_at` | "2023-05-30T03:47:20.628345Z" | Date e hora da última Operation do PaymentProfile |
| `rejected_reason` | "Erro na validação dos dados" | Motivo da recusa do PaymentProfile |
| `company` | 99 | ID da Company  dona do PaymentProfile |
