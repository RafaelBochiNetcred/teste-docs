# Link de Pagamento

_Origem: `Cobrança > Link de Pagamento` na collection Postman._

O ChargeLink é um link de pagamento, que pode ser configurado para ser utilizável apenas uma vez, ou admitindo múltiplos pagamentos. O link também pode ser expirado após determinado tempo é permancer ativo indifinitavemente.

Um link admite os seguintes métodos para pagamento:

- Cartão.
    
- Boleto normal ou híbrido (permite pagamento via PIX).
    
- Pix.
    
- Cartão recorrente.
    

**Caso seja utilizado o método "cartão recorrente" todos os outros métodos deverão ser enviados como false, visto que se trata de outro tipo de transação.**

**Considerando esses aspectos, é crucial entender que o propósito principal do ChargeLink não é ser um método de pagamento (como boleto, cartão, PIX, etc.), mas sim emitir solicitações de pagamento. Um link ocasionará, após o seu preenchimento, a criação de uma** [Charge](https://documenter.getpostman.com/view/14324610/2s9YeMznXH#9bd35715-5d74-4d84-80a3-d3ab141ce466).

## Nesta secao

- [Criar Link](criar-link/index.md)
- [Enviar Link](enviar-link/index.md)
