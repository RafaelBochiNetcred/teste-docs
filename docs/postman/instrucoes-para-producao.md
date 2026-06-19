# Instruções para Produção

_Origem: `Instruções para Produção` na collection Postman._

Ao terminar toda a integração, o próximo passo é mover a integração para o ambiente de produção. Abaixo, segue um quadro com as diferenças entre os dois ambientes.

### Diferenças entre sandbox e produção

| **Sandbox** | **Produção** |
| --- | --- |
| Ambiente de testes | Ambiente de operação |
| Fluxos de chamadas podem ser simulados para validar pontos especificos de cada mutation e query | Fluxos de chamadas são feitos de forma completa, gerando registros e cobranças reais ao final do processo |
| É possível testar todos os métodos de pagamento sem criar cobranças reais | Cada método de pagamento irá gerar cobranças reais ao ser utilizado |

---

E para efetivamente fazer a troca entre os dois ambientes, é necessário passar por 3 etapas, que podem ser feitas de maneira concomitante:

- O primeiro passo é a troca de usuário (login/senha), pois os dois ambientes são isolados um do outro. Normalmente essa informação é encaminhada por e-mail, mas caso não seja, é possível solicitar no suporte um novo usuário para produção;
    
- O segundo passo, é trocar todos os IDs da integração, como `companyID`, `payoutRuleId`, entre outros, pelo mesmo motivo de sandbox e produção serem ambientes isolados;
    
- E o terceiro passo é a troca da URL utilizada na API, onde ela passa de [https://api.sandbox.netcredbrasil.com.br/graphql](https://api.sandbox.netcredbrasil.com.br/graphql) para [https://api.netcredbrasil.com.br/graphql](https://api.netcredbrasil.com.br/graphql) (remove o termo sandbox da URL).
    

Após esses 3 etapas, a sua integração já estará totalmente em produção. Mas, caso precise, o ambiente de sandbox continuará habilitado enquanto existir vínculos ativos com a Netcred, permitindo testes de outros métodos de pagamento, melhorias ou mudanças de fluxos internos.
