# Diferenças entre rrule e installment_number

_Origem: `Cobrança > Usando RRule > Diferenças entre rrule e installment_number` na collection Postman._

Esta seção explica as diferenças entre os campos **`rrule`** e **`installment_number`**, ambos opcionais e disponíveis nos métodos de criação de cobranças da API Netcred. Eles servem a propósitos distintos e são **mutuamente exclusivos** — apenas um deve ser utilizado por cobrança.

---

## `installment_number`

O campo **`installment_number`** é utilizado para dividir uma única cobrança em um número fixo de parcelas de valor igual. O valor total é dividido automaticamente entre as parcelas, e as datas de vencimento são calculadas em intervalos mensais fixos a partir da primeira data de vencimento informada.

- Gera uma <b>Charge</b> contendo apenas uma <b>Transaction</b> com o número de parcelas informado em **`installment_number`**
    
- É o método utilizado para parcelamento padrão no cartão de crédito, travando o valor total da cobrança no limite do cartão.
    
- Ideal para parcelamentos convencionais com valores e intervalos uniformes.
    

**Exemplo:** Uma cobrança de R$ 1.200,00 com `installment_number: 12` gerará 12 parcelas de R$ 100,00, com vencimentos mensais.

---

## `rrule`

O campo **`rrule`** (Recurrence Rule) permite definir regras de recorrência para cobranças de **cartão**, **boleto** e **pix**, com controle total sobre frequência, intervalo, dias específicos e condições de término. Cada ocorrência gera uma <b>Transaction</b> independente, com seu próprio `dueAt` definido diretamente pela regra.

- Flexível: suporta recorrências diárias, semanais, mensais, anuais e personalizadas.
    
- Permite definir dias específicos da semana (`BYDAY`) ou do mês (`BYMONTHDAY`).
    
- Pode ser usado inclusive para agendar uma **única cobrança em uma data futura**.
    
- É o método utilizado para recorrência no cartão de crédito, travando apenas o valor da parcela do mês no limite do cartão. Também utilizado para as cobranças de Boleto e Pix.
    
- Ideal para cronogramas complexos ou irregulares.
    

**Exemplo:** `FREQ=MONTHLY;BYDAY=MO;COUNT=6` gerará 6 cobranças às segundas-feiras de cada mês.

---

## Comparativo

| Característica | `installment_number` | `rrule` |
| --- | --- | --- |
| Finalidade | Parcelamento simples em parcelas iguais | Recorrência customizada |
| Controle de datas | Automático (intervalos mensais fixos) | Total (definido pela regra) |
| Flexibilidade | Baixa | Alta |
| Transações geradas | Vinculadas à cobrança principal | Transactions independentes, cada uma com seu `dueAt` |
| Caso de uso típico | Parcelamento de compra | Assinaturas, planos, agendamentos |

> **Atenção:** Os campos `rrule` e `installment_number` são **mutuamente exclusivos**. Não utilize ambos na mesma requisição.
