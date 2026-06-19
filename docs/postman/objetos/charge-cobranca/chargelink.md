# ChargeLink

_Origem: `Objetos > Charge (Cobrança) > ChargeLink` na collection Postman._

O ChargeLink é um link de pagamento, que pode ser configurado para ser utilizável apenas uma vez, ou admitindo múltiplos pagamentos. O link também pode ser expirado após determinado tempo é permancer ativo indifinitavemente.

<h3>Parâmetros</h3>

| Nome | **Exemplo** | Descrição |
| --- | --- | --- |
| `id` | Inteiro | ID unico |
| `isActive` | Boolean | Link está ativo |
| `baseAmount` | Decimal | valor base da cobrança  <br>**se estiver vazio deve ser informado no momento do pagamento** |
| `unique` | Boolean | Link unico ou não |
| `timesUsed` | Int | Quantidade de vezes que o Link foi usado |
| `billetAllowed` | Boolean | pagamento por boleto habilitado |
| `cardSingleAllowed` | Boolean | pagamento por cartão habilitado |
| `cardRecurringAllowed` | Boolean | pagamento por cartão de forma recorrente habilitado |
| `pixAllowed` | Boolean | pagamento por PIX habilitado |
| `companyName` | String | Define se o método de pagamento boleto pode ser utilizado |
| `company` | Objeto Company | Estabelecimento (`MERCHANT`) dono desta ChargeLink |
| `expiryDate` | DateTime | Data e hora que expira o link de pagamento |
| `maxInstallments` | Int | Maximo de parcelas |
| `url` | String | url gerado para a ChargeLink |
| `billetCondition` | Objeto BilletCondition | **Apenas para BILLET**  <br>Configurações de boleto |
| `order` | Objeto OrderInput |  |
| `pixExpiringSeconds` | Int | Tempo de expiração do PIX |
| `billetType` | String | "NORMAL" ou "HYBRID" |

### Tipos de boleto

| Método | Nome | Descrição |
| --- | --- | --- |
| `billletType` | NORMAL | Boleto sem QRCode PIX |
| `billletType` | HYBRID | Boleto com QRCode PIX |
