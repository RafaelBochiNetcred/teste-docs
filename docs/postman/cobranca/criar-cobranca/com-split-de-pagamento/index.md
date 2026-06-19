# Com Split de Pagamento

_Origem: `Cobrança > Criar cobrança > Com Split de Pagamento` na collection Postman._

Aqui demonstramos como utilizar o input de PayoutRule na criação da cobrança para configurar o split para uma cobrança específica.

O envio da PayoutRule é independente do método utilizado. Neste exemplo o foco é no envio do PayoutRule e esta parte do input pode ser facilmente acrescentada às demais chamadas.

No caso de boleto e PIX, a liquidação é sempre em D+1, portanto a configuração de atencipação "não terá efeito", mas funcionará normalmente para cartão de crédito.

**IMPORTANTE:** O estabelecimento precisa ter a funcionalidade de seleção de split habilitada, impactando tanto o envio do `payoutRuleId` quanto `payoutRuleInput.`
