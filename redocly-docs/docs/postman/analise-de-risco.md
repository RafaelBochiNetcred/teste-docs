# Análise de risco

_Origem: `Análise de risco` na collection Postman._

A análise de risco tem como objetivo principal prevenir chargebacks, que ocorrem quando um golpista usa um cartão clonado para efetuar uma compra online. Posteriormente, o legítimo proprietário do cartão percebe a fraude e solicita ao banco o reembolso do valor gasto. Isso resulta na loja não recebendo o pagamento pela compra realizada, mesmo já tendo enviado o produto ao golpista.

# Como funciona a análise de risco:

A análise de risco é realizada em duas etapas:

1. Um script será disponibilizado para sua aplicação, coletando dados públicos do dispositivo do usuário para armazenamento no campo SessionID. Essas informações serão enviadas à [ClearSale](https://api.clearsale.com.br/docs/behavior-analytics), plataforma de solução antifraude parceira Netcred. O processo, com duração média de 3 segundos, visa correlacionar esses dados com coletas anteriores. Recomenda-se integrar o script em páginas interativas, preservando a experiência do usuário, sem comprometer a segurança.
    
2. Ao finalizar o processo de compra, caso a modalidade de pagamento seja cartão, o SessionID deve ser enviado de forma obrigatória no campo sessionId presente dentro do parametro orderInput explicado abaixo e também na seção ChargeCreateCard. Na finalização da criação da cobrança, a combinação dessas informações será enviada à ClearSale, que retornará a aprovação ou rejeição do processo de compra com base na análise feita.
    

**Para ter acesso à documentação completa de como incluir esta funcionalidade em sua solução, acesse o** [<b>link</b>](https://api.clearsale.com.br/docs/behavior-analytics).

# Tipos de análise de risco:

A ClearSale disponibiliza dois tipos de análise:

1. **Realtime**: Processo instantâneo recomendado para negócios com entrega imediata, como softwares e cursos online. Análise ágil para aprovação ou rejeição de pedidos. Pedidos reprovados podem, ocasionalmente, passar por análise manual de até 3 dias úteis, especialmente pedidos de alto risco.
    
2. **Total Garantido**: Ideal para vendas onde a liberação instantânea não é crucial. Análise minuciosa para garantir alta aprovação de pedidos genuínos. Aprovação automática em até 3 horas. Oferece reembolso de até R$ 10.000,00 por pedido em caso de chargeback.
    

**O método ideal para cada empresa será analisado individualmente durante o processo de cadastramento.**

### OrderInput

Junto com o SessionID, deve ser enviada informações sobre o carrinho de compras, que deve ser preenchido com informações precisas, evitando descrições subjetivas e/ou genéricas. Isso é fundamental para aprimorar a eficácia da análise de risco realizada. Essa informação é obrigatória para a análise da ClearSale.

Caso a sua integração não trate com produtos físicos, busque identificar algum serviço prestado relacionado a esta cobrança.

### Parâmetros

| Nome | Exemplo | Descrição |
| --- | --- | --- |
| `sessionId` |  | **Obrigatório**  <br>Identificador de "sessão do usuário".  <br>  <br>Esse ID permite que o pagador seja identificado por informações como sistema operacional, navegador, IP, etc.  <br>  <br>Para gerar esse valor durante a criação da cobrança, siga o [guia da Clearsale](https://api.clearsale.com.br/docs/behavior-analytics). Para obter o app_id do qual eles falam, entre em contato com o suporte da Netcred |
| `referenceCode` | "CARRINHO001" | Código de identificação externo do carrinho |
| `shippingCost` | "15.00" | Valor do frete  <br>  <br>Valor com duas casas decimais |
| `orderItems` |  | **Obrigatório** pelo menos um item  <br>Lista de items do carrinho |
| `orderItems.count` | 2 | **Default:** 1  <br>Quantidade deste produto no carrinho |
| `orderItems.productId` | 99 | **Obrigatório** na ausência do `productInput`  <br>  <br>ID de um produto existente |
| `orderItems.productInput` |  | **Obrigatório** na ausência do `productId`  <br>  <br>Input de um produto |
| `orderItems.productInput.name` | "Tẽnis Preto" | **Obrigatório**  <br>Nome do produto |
| `orderItems.productInput.amount` | "200.00" | **Obrigatório**  <br>Valor unitário do produto  <br>  <br>Valor com duas casas decimais |
| `orderItems.productInput.description` | "Tênis Preto tamanho 40" | Descrição do produto |
| `orderItems.productInput.referenceCode` | "TENIS0001" | Código de referência externo |
| `orderItems.productInput.category` | "Tênis" | Nome da categoria do produto |
