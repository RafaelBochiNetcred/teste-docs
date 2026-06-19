# Charge

_Origem: `Objetos > Charge (Cobrança) > Charge` na collection Postman._

A Charge é a Cobrança é si. Ela é, essencialmente, um agrupamento de Transactions. As suas configurações são repassadas para essas Transactions na criação.

### Campos da Charge

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `id` | Inteiro | ID único |
| `uuid` | UUID | ID único em formato UUID |
| `referenceCode` | String | **Pode ser nulo**  <br>Referência externa idempotente |
| `amount` | Decimal | Valor |
| `method` | String | Método:  <br>\- BILLET: Boleto  <br>\- PIX  <br>\- CARD: Cartão de crédito |
| `submethod` | String | Sub-método, conforme tabela abaixo. |
| `rrule` | String | A [RRule](https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html) define a "frequência" para a geração das datas de vencimento (dueAt) das Transactions dessa Charge. |
| `ipAddress` | String | IP de onde foi gerada a cobrança |
| `customerIpAddress` | String | IP do usuário final que requisitou a cobrança |
| `voidAt` | Datetime | Data e hora do cancelamento |
| `voidReason` | String | Motivo do cancelamento |
| `chargeType` | String | Tipo da Charge:  <br>\- SINGLE: a emissão aconteceu na hora da criação  <br>\- RECURRING: foi criada com pelo menos uma Transaction SCHEDULED (agendada) |
| `chargeStatus` | String | Status atual da cobrança:  <br>\- ONGOING: ainda tem Transactions pendentes  <br>\- ENDED: todas as Transactions atingiram um estado final  <br>\- VOIDED: foi cancelada |
| `installmentNumber` | Inteiro | **Apenas para o método CARD**  <br>Número de parcelas do crédito |
| `extraInfo` | String | Texto com informações adicionais |
| `manualCapture` | Boolean | **Apenas para o método CARD**  <br>Se a captura será manual, i.e. não ocorrerá de forma automática |
| `billingCycleTotal` | Inteiro | Total de Transactions desta Charge |
| `billingCyclePaid` | Inteiro | Total de Transactions desta Charge no estado PAID |
| `billingCyclesProcessed` | Inteiro | Total de Transactions desta Charge em um estado diferente de SCHEDULED |
| `company` | Objeto Company | Estabelecimento (`MERCHANT`) dono desta Charge |
| `customer` | Objeto Customer | Pagador |
| `paymentProfile` | Objeto PaymentProfile | Informações de cobrança para a Charge |
| `billetCondition` | Objeto BilletCondition | **Apenas para o método BILLET**  <br>Configurações de boleto |
| `pixCondition` | Objeto PixCondition | **Apenas para o método PIX**  <br>Configurações de PIX |
| `chargeLink` | Objeto ChargeLink | ChargeLink associado, caso a Charge tenha sido criada a partid de um |
| `payoutRule` | Objeto PayoutRule | **Mutuamente exclusivo com** **`contract`**  <br>Split de pagamento |
| `contract` | Objeto Contract | **Mutuamente exclusivo com** **`payoutRule`**  <br>Contrato associado a esta cobrança. Ele vai direcionar os recebíveis para um Financiador |

### Tabela de `submethod`

| Método | Nome | Descrição |
| --- | --- | --- |
| BILLET | NORMAL | Boleto sem QRCode PIX |
| BILLET | HYBRID | Boleto com QRCode PIX |
| PIX | IMMEDIATE | PIX que expira em um curto período de tempo. Criado a partir do ChargeLink |
| PIX | WITH_DUE_DATE | PIX semelhante a boleto, com data de vencimento e configurações. Criado pelo ChargeCreate |
| PIX | STATIC | PIX pago por QRCode estático |
| PIX | TERMINAL | PIX pago por terminal POS |
| CARD | NOT_APPLICABLE | Apenas para o campo não ficar vazio no método CARD |
