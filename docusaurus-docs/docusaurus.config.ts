import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";
import type * as Redocusaurus from "redocusaurus";

const config: Config = {
  title: "Netcred API",
  tagline: "Documentacao para clientes e integradores",

  url: "https://docs.example.com",
  baseUrl: "/",

  organizationName: "netcred",
  projectName: "api-docs",

  onBrokenLinks: "throw",
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: "warn",
    },
  },

  i18n: {
    defaultLocale: "pt-BR",
    locales: ["pt-BR"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          routeBasePath: "/",
          sidebarPath: "./sidebars.ts",
        },
        blog: false,
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
    [
      "redocusaurus",
      {
        specs: [
          {
            spec: "openapi/openapi.yaml",
            route: "/schema-standalone",
          },
        ],
        theme: {
          primaryColor: "#1663d9",
        },
      } satisfies Redocusaurus.PresetEntry[1],
    ],
  ],

  themeConfig: {
    docs: {
      sidebar: {
        hideable: true,
      },
    },
    navbar: {
      title: "Netcred API",
      items: [
        { to: "/", label: "Inicio", position: "left" },
        { to: "/docs", label: "Visao geral", position: "left" },
        { to: "/por-onde-comecar", label: "Guias", position: "left" },
        { to: "/schemas", label: "Schemas", position: "left" },
      ],
    },
    footer: {
      style: "dark",
      copyright: "Netcred API",
    },
    prism: {
      additionalLanguages: ["bash", "json", "yaml"],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
