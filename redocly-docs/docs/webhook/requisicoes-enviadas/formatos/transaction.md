# Transaction

### Formato TransactionPayload

| Nome | Exemplo | Descrição |
| --- | --- | --- |
| `id` | 1234 | Identificador único da Transaction |
| `uuid` | "f6412196-35fb-4716-b308-0e2cfea7c970" | Identificador único da Transaction em formato UUID |
| `transaction_state` | "PAID" | Estado da Transaction |
| `amount` | "10.0" | Valor total |
| `refunded_amount` | "0.0" | Valor estornado |
| `paid_amount` | "10.0" | Valor pago |
| `installment_number` | 2 | Número de parcelas de crédito |
| `company` | 99 | ID da Company  dona da Transaction |
| `charge` |  | Dados da Charge associada |
| `charge.id` | 16486 | Identificador único da Charge |
| `charge.reference_code` | "CHARGE0001" | Código de idempotência |
| `charge.charge_link_id` | 16128 | Identificador único do ChargeLink criador da Charge |
| `billet_info` |  | **Somente presente para o método BILLET**  <br>  <br>Dados de Boleto |
| `billet_info.id` | 1684 | Identificador único do BilletInfo |
| `billet_info.bar_code` | "74897937700000099891122224595067890312345109" | Código de barras do Boleto |
| `billet_info.digitable_line` | "74891121150012026789503123451084787040000000015" | Linha digitável do Boleto |
| `pix_info` |  | **Somente presente para o método PIX  <br>  <br>**Dados de PIX |
| `pix_info.id` | 6126 | Identificador único do PixInfo |
| `pix_info.pix_type` | "WITH_DUE_DATE" | Tipo do PIX  <br>  <br>Conforme conforme documentação de Transaction |
| `pix_info.pix_copy_paste` | "00020126930014br.gov.bcb.pix2571pix-qrcode-h.sicredi.com.br/qr/v2/cobv/a938ad9546364b5e9c535056c3c457a45204000053039865802BR5903PIX6006Cidade62070503\*_\\_63043ECD" | Código PIX copia e cola |
| `pix_info.e2eid` | "E0379324270230530145747wFS3U4uG8" | Identificador do pagamento PIX |
| `pix_info.expires_at` | "2023-05-26T03:47:20.628345Z" | Data e hora de expiração do PIX, caso tipo IMMEDIATE |
| `capture_medium` | "ONLINE" | "Meio de captura": ONLINE ou TERMINAL |
| `method` | "CARD" | Método: BILLET, PIX ou CARD |
| `billing_at` | "2023-05-26" | Data quando será feita a emissão/autorização |
| `billed_at` | "2023-05-26T03:47:20.628345Z" | Data e hora quando foi feta a emissão/autorização |
| `due_at` | "2023-05-30" | Data quando será feita a captura para CARD e data de vencimento para BILLET e PIX |
| `paid_at` | "2023-05-30T03:47:20.628345Z" | Data e hora quando foi feito o pagamento  <br>  <br>Obs.: no caso do boleto a hora não é confiável |
| `attempts` | 1 | Número de tentativas de autorização, pode ser maior que 1 para CARD |
| `is_disputed` | false | Se atransação está em processo de chargeback |
| `operations` |  | **Pode estar vazio quando a transação estiver SCHEDULED**  <br>  <br>Lista de operações de gateway, como emissão/autorização, captura e cancelamento |
| `operations.id` | 16984 | Identificador único da Operation |
| `operations.message` | "Erro crítico" | Mensagem de erro resumida |
| `operations.message_detail` | "Erro ao valida dados" | Mensagem de erro mais detalhada |
| `operations.operation_status` | "FAILURE" | Status da Operation:  <br>\- SUCCESS: concluido com sucesso  <br>\- REJECTED: concluido com sucesso mas retornou recusa  <br>\- FAILURE: ocorreu alguma falha no gateway |
| `operations.operation_date` | "2023-05-30T03:47:20.628345Z" | Date e hora quando ocorreu a Operation |
| `operations.operation_type` | "EMISSION" | Tipo da Operation:  <br>\- AUTHORIZE  <br>\- CAPTURE  <br>\- VOID  <br>\- TOKENIZE  <br>\- UPDATE  <br>\- REFUND  <br>\- IMPORT  <br>\- EMISSION  <br>\- RISK_ANALYSIS |
| `payment_profile` | Objeto PaymentProfilePayload | **Pode ser nulo**  <br>Dados do PaymentProfile |
