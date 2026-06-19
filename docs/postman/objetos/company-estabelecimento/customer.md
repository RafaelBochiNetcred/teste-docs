# Customer

_Origem: `Objetos > Company (Estabelecimento) > Customer` na collection Postman._

O Customer é o pagador das cobranças, podendo ser tanto uma pessoa física quanto jurídica.

### Campos Customer

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `id` | Inteiro | Identificador único |
| `company` | Objeto Company | Empresa do tipo `MERCHANT` ou `MARKETPLACE` para a qual este Customer foi cadastrado  <br>  <br>Obs.: o Customer pode estar "repetido" em várias empresas |
| `name` | String | Nome do pagador |
| `email` | String | Email |
| `documentType` | String | Tipo do documento:  <br>CPF ou CNPJ |
| `document` | String | Número do CPF/CNPJ |
| `phone` | String | Telefone ou celular |
| `birthDate` | Date | Data de nascimento |
| `gender` | String | Gênero do pagador:  <br>\- MALE  <br>\- FEMALE  <br>\- OTHER |
