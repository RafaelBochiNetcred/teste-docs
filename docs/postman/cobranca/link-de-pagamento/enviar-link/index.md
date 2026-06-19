# Enviar Link

_Origem: `Cobrança > Link de Pagamento > Enviar Link` na collection Postman._

Após a criação do ChargeLink deve-se utilizar o método ChargeLinkSend para enviar aos destinatários desejados o link de cobrança que possuirá uma página onde os mesmos poderão preencher os dados e realizar a emissão da cobrança conforme as configurações feitas anteriormente.

### ChargeLinkSend

| Nome | **Exemplo** | **Descrição** |
| --- | --- | --- |
| `chargeLinkId` | "190" | **Obrigatorio**  <br>ID retornado ao enviar o método CreateChargeLink |
| `email` | "teste@empresa.com.br" | e-mail que será enviado a ChargeLink |
| `phoneNumber` | 48954613456 | Número de telefone que será enviado a ChargeLink |
