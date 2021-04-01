const path = require("path");

module.exports = {
  title: "THE DATA ENGINEERING COOKBOOK",
  tagline: "by ANDREAS KRETZ",
  url: "http://cookbook.learndataengineering.com",
  baseUrl: "/", // path where website is available
  favicon: "images/CookbookCover.jpg",
  organizationName: "andkret", // GitHub org/user name.
  projectName: "Cookbook", // project name i.e repo name of project
  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",
  themeConfig: {
    colorMode: {
      defaultMode: "light",
      disableSwitch: true,
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: "Data Engineering Cookbook",
      logo: {
        alt: "Site Logo",
        src: "images/CookbookCover.jpg", // path with respect to static dir
      },
      items: [
        {
          to: "docs/01-Introduction",
          label: "Cookbook",
          position: "left",
        },
        {
          href: "https://learndataengineering.com/",
          label: "Data Engineering Academy",
          position: "right",
        },
        {
          href: "https://medium.com/plumbersofdatascience",
          label: "Plumbers Of Data Science",
          position: "right",
        },
        {
          href: "https://github.com/andkret/Cookbook",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "light",
      links: [],
      copyright: `Copyright © ${new Date().getFullYear()} Andreas Kretz. Built by Kristijan Bakaric with Docusaurus.`,
    },
    // prism: {
    //   additionalLanguages: ["powerquery", "dax"],
    // },
  },
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
  // plugins: [require.resolve("docusaurus-lunr-search")], //goes in packlage.json//"docusaurus-lunr-search": "^2.1.10",
};
