# Company (Estabelecimento)

_Origem: `Objetos > Company (Estabelecimento)` na collection Postman._

Objetos no grupo Company estão mais ligados aos estabelecimentos.

Uma **Company** representa uma empresa cadastrada na plataforma Netcred. Cada company possui um tipo (`companyType`) que define seu papel e as operações que ela pode realizar na API.

Os tipos de company disponíveis para as chamadas API são:

- **FACILITATOR**: Sub-adquirente, responsável pelo gerenciamento e liquidação dos recebíveis (é o caso da Netcred)
    
- **MARKETPLACE**: Marketplaces possuem várias empresas abaixo de si, para as quais usuários deste Marketplace podem criar cobranças. Um Marketplace pode ter sub-marketplaces e vice-versa.
    
- **FINANCIER**: Financiador, responsável por financiar operações de crédito através de Contratos, que trocam a titularidades de recebíveis a seu favor
    
- **MERCHANT**: Estabelecimento que possuem cobranças e os únicos para os quais cobranças podem ser criadas
    
- **REFERRER**: Empresa que indica outras e ganha uma comissão das vendas geradas por elas
    

Algumas companies possuem permissões específicas e podem ser utilizadas em chamadas diferentes. Por exemplo, apenas a company do tipo **Merchant** pode ser utilizada na chamada de criação de cobranças (`charges`). As permissões específicas de cada tipo de company serão indicadas nas respectivas chamadas da API.

## Nesta secao

- [Customer](customer.md)
- [Company](company.md)
- [BankAccount](bankaccount.md)
