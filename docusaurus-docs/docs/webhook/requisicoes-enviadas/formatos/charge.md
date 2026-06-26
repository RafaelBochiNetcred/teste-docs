# Charge

### Formato ChargePayload

| Nome | Exemplo | Descrição |
| --- | --- | --- |
| `id` | 99916 | Identificador único da Charge |
| `reference_code` | "CHARGE0001" | Código de idempotência |
| `charge_type` | "SINGLE" | Tipo da Charge:  <br />\- RECURRING  <br />\- SINGLE |
| `charge_status` | "ONGOING" | Estado da Charge:  <br />\- ONGOING  <br />\- ENDED  <br />\- VOIDED |
| `company` | 99 | ID da Company  dona da Charge |
| `payment_profile` | 223 | **Pode ser nulo**  <br />ID do PaymentProfile utilizado |
| `installment_number` | 12 | Número de parcelas do crédito |
| `bill_days_in_advance` | 0 | Quantos dias antes do vencimentos as Transactions serão emitidas/autorizadas |
| `charge_link_id` | 27 | ID do ChargeLink, caso a Charge tenha sido criada a partir de um |
| `extra_info` | "Contrato X" | Informações extras da Charge |
| `rrule` | "DTSTART:20230529T000000 FREQ=DAILY;INTERVAL=1;COUNT=1" | RRule usada na criação da Charge |
| `transactions` | Lista de objetos TransactionPayload | Lista de Transactions associadas à Charge |
