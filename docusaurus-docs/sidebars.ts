import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docs: [
    'intro',
    'index',
    'por-onde-comecar/index',
    'por-onde-comecar/conceitos-de-graphql',
    'autenticacao/index',
    {
      type: 'category',
      label: 'Webhook',
      link: {
        type: 'doc',
        id: 'webhook/index',
      },
      collapsed: false,
      items: [
        {
          type: 'doc',
          label: 'Schema da API',
          id: 'schema-da-api',
        },
        {
          type: 'category',
          label: 'Requisicoes enviadas',
          link: {
            type: 'doc',
            id: 'webhook/requisicoes-enviadas/index',
          },
          collapsed: false,
          items: [
            {
              type: 'category',
              label: 'Formatos',
              link: {
                type: 'doc',
                id: 'webhook/requisicoes-enviadas/formatos/index',
              },
              collapsed: false,
              items: [
                'webhook/requisicoes-enviadas/formatos/charge',
                'webhook/requisicoes-enviadas/formatos/paymentprofile',
                'webhook/requisicoes-enviadas/formatos/payout',
                'webhook/requisicoes-enviadas/formatos/registrationprocess',
                'webhook/requisicoes-enviadas/formatos/transaction',
              ],
            },
          ],
        },
      ],
    },
  ],
};

export default sidebars;
