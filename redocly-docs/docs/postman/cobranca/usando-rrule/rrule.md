# RRule

_Origem: `Cobrança > Usando RRule > RRule` na collection Postman._

Parâmetros que podem ser utilizados:

- DTSTART: data e hora em que a aplicação da regra dará início.
    
- UNTIL: data e hora em que a regra será finalizada.
    
- FREQ: frequência com o qual a geração de charge irá ocorrer.
    
- INTERVAL: intervalo entre as ocorrências, de acordo com a `FREQ` definida.
    
- COUNT: quantidade de charges a serem geradas.
    
- BYDAY: dia da semana em que será gerado a charge (SU,MO,TU,WE,TH,FR,SA).
    
- BYMONTHDAY: dia do mês que será gerado a charge.
    
- BYSETPOS: valor numérico que corresponde ao sentido de leitura do BYMONTHDAY ( "1" lê dá esquerda para a direita e "-1" lê os valores da direita para a esquerda).
    

Os parametros não são obrigatórios e deverão ser utilizados de acordo com a necessidade para atender determinado objetivo de geração de transações. No caso do BYSETPOS ele é essencial para criar transações no último dia de cada mês, como mostra o primeiro exemplo na tabela a seguir.

Abaixo estão alguns exemplos de uso da rrule:

| **rrule:** | **Regra:** | Resultado: |
| --- | --- | --- |
| "DTSTART:20260430T000000Z RRULE:FREQ=MONTHLY;COUNT=12;BYMONTHDAY=28,29,30,31;BYSETPOS=-1" | 12 transactions mensais no último dia de cada mês | 30 de abril  <br>31 de maio  <br>30 de junho  <br>31 de julho  <br>{...} |
| "DTSTART:20261201T000000Z RRULE:FREQ=DAILY;COUNT=12" | 12 transactions diárias a partir de 01 de dezembro | 01-12 de dezembro de 2026 |
| "DTSTART:20261215T000000Z RRULE:FREQ=DAILY;UNTIL=20261225T000000Z" | Transactions diárias entre 15 e 25 de dezembro | 15-25 de dezembro de 2026 |
| "DTSTART:20260101T000000Z RRULE:FREQ=DAILY;INTERVAL=2;UNTIL=20260130T000000Z" | Transactions entre 01 e 30 de janeiro com intervalo de 01 dia. | 01,03,05,07,09,11,13,15,17,19,21,23,25,27 e 29 de Janeiro de 2026 |
| "DTSTART:20260101T000000Z RRULE:FREQ=MONTHLY;COUNT=12;BYDAY=1FR" | Transactions mensais com geração marcada para a primeira sexta-feira de cada mês | 05 de janeiro  <br>02 de fevereiro  <br>01 de março  <br>05 de abril  <br>{...} |
| "DTSTART:20260101T000000Z RRULE:FREQ=WEEKLY;COUNT=12;BYDAY=MO" | Transactions semanais às segundas-feiras | 05 de janeiro  <br>12 de janeiro  <br>19 de janeiro  <br>26 de janeiro  <br>{...} |
| "DTSTART:20261010T000000Z RRULE:FREQ=DAILY;COUNT=1" | 1 transaction em uma data futura específica, sem repetição | 10 de outubro de 2026 |
