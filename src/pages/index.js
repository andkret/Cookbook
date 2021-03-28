import React from "react";
import classnames from "classnames";
import Layout from "@theme/Layout";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import useBaseUrl from "@docusaurus/useBaseUrl";
import styles from "./styles.module.css";
//
// const features = [
//   {
//     title: <a href="./">1</a>,
//     imageUrl: "./",
//     description: "",
//   },
//   {
//     title: <a href="./">2</a>,
//     imageUrl: "./",
//     description: "",
//   },
// ];

// function Feature({ imageUrl, title, description }) {
//   const imgUrl = useBaseUrl(imageUrl);
//   return (
//     <div className={classnames("col col--4", styles.feature)}>
//       <div className="text--center">
//         {/* <img className={styles.featureImage} src={imgUrl} alt={title} /> */}
//       </div>
//       <h3>{title}</h3>
//       <p>{description}</p>
//     </div>
//   );
// }

function Home() {
  const context = useDocusaurusContext();
  const { siteConfig = {} } = context;
  return (
    <Layout title={`Hello from ${siteConfig.title}`} description="">
      <header className={classnames("hero hero--primary", styles.heroBanner)}>
        <div className="container">
          <img
            className={styles.mainImage}
            width="300"
            height="400"
            src="images/CookbookCover.jpg"
          />
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={classnames(
                "button button--outline button--lg",
                styles.getStarted
              )}
              to={useBaseUrl("docs/01-Introduction")}
            >
              Read the Cookbook!
            </Link>
          </div>
        </div>
      </header>
      {/* <main className={styles.content}>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              {features.map((props, idx) => (
                <Feature key={idx} {...props} />
              ))}
            </div>
          </div>
        </section>
      </main> */}
    </Layout>
  );
}

export default Home;
