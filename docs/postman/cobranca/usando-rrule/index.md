# Usando RRule

_Origem: `Cobrança > Usando RRule` na collection Postman._

A RRule ("Regra de recorrência" em tradução livre) é um campo opcional presente em nossos métodos CreateChargeBillet, CreateChargeCard  e CreateChargePix, destinado a definir quando e com qual frequência as transações serão geradas — seja para cobranças que se repetem em intervalos específicos (diários, semanais, mensais, entre outros) ou para uma única transação em uma data futura específica.

A data de vencimento (`dueAt`) de cada Transaction é definida **diretamente** pela RRule — ou seja, cada ocorrência gerada pela regra corresponde a uma Transaction com o `dueAt` igual à data calculada pela RRule.

## Nesta secao

- [Diferenças entre rrule e installment_number](diferencas-entre-rrule-e-installment-number.md)
- [RRule](rrule.md)
