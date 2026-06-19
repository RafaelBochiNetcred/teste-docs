# Instruções para homologação

_Origem: `Instruções para homologação` na collection Postman._

No ambiente de homologação da API ([https://api.sandbox.netcredbrasil.com.br](https://api.sandbox.netcredbrasil.com.br/)) você pode fazer todas as chamadas da nossa plataforma sem a necessidade de criar registros reais. Isso, entretanto, tem algumas limitações por enquanto, como não ser possível simular um pagamento de Boleto ou PIX.

No ambiente de homologação existem alguns dados padrão para testar determinada resposta.

Números de cartão

- 4970100000000048 para testar a **aprovação**
    
- 4970100000000071 para testar a **rejeição**
    

Análise de risco:

- CPF/CNPJ do Customer com final "1" para **aprovação** em análise de risco
    
- CPF/CNPJ do Customer com final **diferente** de "1" para **rejeição** em análise de risco
    

**IMPORTANTE:** evite utilizar dados reais no ambiente de homologação, sempre utilizando ferramentas para a geração de CPFs por exemplo
