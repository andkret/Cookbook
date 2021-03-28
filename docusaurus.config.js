const path = require("path");

module.exports = {
  title: "THE DATA ENGINEERING COOKBOOK",
  tagline: "by ANDREAS KRETZ",
  url: "https://baky0905.github.io", // url where websited is hosted
  baseUrl: "/copy-between-test/", // path where website is available
  favicon: "images/CookbookCover.jpg",
  organizationName: "baky0905", // GitHub org/user name.
  projectName: "copy-between-test", // project name i.e repo name of project
  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",
  themeConfig: {
    colorMode: {
      defaultMode: "light",
      disableSwitch: true,
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: "Data Engineering Cookbook", // title
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
      copyright: `Copyright © ${new Date().getFullYear()} Kristijan Bakaric, Built with Docusaurus.`,
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
          // Please change this to your repo.
          // editUrl: "",
        },
        blog: {
          showReadingTime: true,
          postsPerPage: 5,
          // Please change this to your repo.
          // editUrl: "",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
  // plugins: [require.resolve("docusaurus-lunr-search")], //goes in packlage.json//"docusaurus-lunr-search": "^2.1.10",
};
