# Requisições enviadas

Aqui definimos os formatos dos Webhooks que são enviados

Existem 3 tipos de formato: Charge, Transaction e PaymentProfile

Uma chamada de exemplo é apresentada para cada, incluindo os headers enviados. Abaixo também estão listados os headers, comuns a todas as chamadas de Webhook

### **Headers**

| Chave | Exemplo | Descrição |
| --- | --- | --- |
| X-NETCRED-Event | "TRANSACTION_UPDATE" | Evento que causou o envio.  <br />Os tipos possíveis são descritos aqui |
| X-NETCRED-Domain | "[https://api.sandbox.netcredbrasil.com.br"](https://api.sandbox.netcredbrasil.com.br) | Domínio do qual foi enviado o Webhook. Sempre será um domínio Netcred |
| X-NETCRED-Signature | "87e99e04539c6588b8ee9b8e716a7a5f68426542b1b017b83d93e31b3a2e54cd" | Hash SHA256 gerado com o corpo da requisição, utilizando a `secretKey` informda na criação do Webhook  <br />  <br />Este hash pode ser refeito do seu lado para garantir a veracidade e integridade dos dados contidos no Webhook |

## Nesta secao

- [Formatos](formatos/index.md)
