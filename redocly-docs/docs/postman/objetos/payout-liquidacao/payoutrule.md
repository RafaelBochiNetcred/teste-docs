# PayoutRule

_Origem: `Objetos > Payout (Liquidação) > PayoutRule` na collection Postman._

O objeto PayoutRule define um split de pagamento associado a uma Company. Uma empresa pode ter vários splits, mas um deles será o primário (marcado pelo campo `isPrimary`), que será utilizado sempre que um for necessário mas não informado.

Toda PayoutRule deve ter pelo menos um RuleItem com `splitType` PERCENTAGE e a soma dos `proportions` de RuleItems PERCETAGE deve ser igual a "100.0" .

### Campos PayoutRule

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `id` | Inteiro | Identificador único |
| `company` | Objeto Company | Empresa a qual este split pertence. Pode ser um `MERCHANT` ou `MARKETPLACE` |
| `isActive` | Boolean | Se esse split está ativo e pode ser utilizado |
| `isPrimary` | Boolean | Se esse split é o padrão  <br>  <br>Apenas um split pode ser padrão em uma empresa |
| `ruleItems` | Lista de objetos RuleItem | Lista de "destinos" do split.  <br>  <br>Consulte a tabela a baixo para ver os campos de um RuleItem |

### Campos RuleItem

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `splitType` | String | Tipo de split para essa conta:  <br>\- PERCENTAGE: uma porcetagem (`proportion`) será repassada para esta conta  <br>\- FIXED_AMOUNT: este valor (`amount`) será repassado para esta conta, se for possível |
| `proportion` | Decimal | **Sempre preenchido** quando `splitType` for PERCENTAGE  <br>  <br>Proporção repassada à conta |
| `amount` | Decimal | **Sempre preenchido** quando `splitType` for FIXED_AMOUNT  <br>  <br>Valor repassado à conta |
| `isLiable` | Boolean | Se esta conta irá arcar com débitos (como taxas de aluguél e estornos)  <br>  <br>Taxas associadas diretamente á transação (como MDR e antecipação) são descontadas independente deste campo |
| `bankAccount` | Objeto BankAccount | Conta bancária para esta parte do split |
| `schedule` | Objeto Schedule | Configuração das opções de antecipação  <br>  <br>Consulte na tabela abaixo o seu formato |
| `card_payout_allowed` | `Boolean` | Somente leitura  <br>Indica se esta regra de payout está habilitada para liquidar cobranças de **cartão de crédito**.  <br>O campo será `true` somente quando **todos** os itens da regra (`ruleItems`) tiverem uma conta bancária cujo `holderDocument` é igual ao `document` da empresa EC (Estabelecimento Comercial) associada à regra. Caso qualquer conta bancária pertença a um terceiro (documento diferente), o valor será `false`. |

### Campos Schedule

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `scheduleType` | String | **Se** **`automaticAdvance`** **for** **`false`** **esse campo é ignorado, mas ainda estará preenchido**  <br>  <br>Tipo da antecipação aplicada:  <br>\- DAILY  <br>\- WEEKLY  <br>\- MONTHLY |
| `scheduleAnchor` | Inteiro | **Se** **`automaticAdvance`** **for** **`false`** **esse campo é ignorado, mas ainda estará preenchido**  <br>  <br>Indica o "dia" da antecipação em relacão ao `scheduleType`:  <br>\- DAILY: o anchor será um valor entre 1 e 31, indicando quantos dias depois do processamento será liquidado  <br>\- WEEKLY: o anchor será um valor de 0 a 6, onde 0 é segunda-feira e 6, domingo  <br>\- MONTHLY: o anchor será um valor entre 1 e 31, indicando o dia do mês quando ocorrerá as liquidações |
| `automaticAdvance` | Boolean | Se antecipação está habilitada.  <br>  <br>Caso true, a liquidação será feita conforme indicado pelos campos `scheduleType` e `scheduleAnchor`, acarretando em uma taxa de antecipação  <br>  <br>Caso contrário, as datas padrão de liquidação serão utilizada |
