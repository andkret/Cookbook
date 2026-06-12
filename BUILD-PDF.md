# Building the Cookbook PDF

How to turn the multi-file cookbook into a single PDF **without** merging files
or hand-fixing links. We use a book compiler (mdBook) that resolves cross-file
links automatically. You keep editing section files and pushing to GitHub as
normal — the PDF is just a build output.

## The idea

- **Content** lives in `sections/*.md` — edit normally, push to GitHub normally.
- **Order** is declared once in `sections/SUMMARY.md`.
- **Styling** lives in CSS/theme, never in the content.
- **PDF** is a disposable output — regenerate with one command, never hand-edit.

---

## One-time setup

### 1. Install mdBook + PDF backend
```bash
brew install mdbook
cargo install mdbook-pdf      # needs Rust (https://rustup.rs)
```

### 2. Create `book.toml` in the repo root
```toml
[book]
title = "The Data Engineering Cookbook"
authors = ["Andreas Kretz"]
src = "sections"

[output.html]
[output.pdf]
```

### 3. Create `sections/SUMMARY.md` (declares chapter order)
```markdown
# Summary

[Introduction](01-Introduction.md)
- [Basic Engineering Skills](02-BasicSkills.md)
- [Advanced Engineering Skills](03-AdvancedSkills.md)
- [Free Hands-On Courses](04-HandsOnCourse.md)
- [Case Studies](05-CaseStudies.md)
- [Best Practices Cloud Platforms](06-BestPracticesCloud.md)
- [130+ Data Sources](07-DataSources.md)
- [1001 Interview Questions](08-InterviewQuestions.md)
- [Recommended Books & Courses](09-BooksAndCourses.md)
- [Updates](10-Updates.md)
```

### 4. Two one-time fix-ups
- **Links:** make in-file links use `XX-File.md#anchor` (drop the `sections/`
  prefix — mdBook's `src` is already `sections`).
- **Images:** make sure the `images/` folder is reachable from `sections/`
  (copy or symlink it so paths like `images/foo.jpg` resolve).

---

## Every time you want a fresh PDF

```bash
mdbook build
# website  -> ./book
# PDF      -> ./book/pdf/output.pdf
```

Add a video/article to a section, push to GitHub, rerun `mdbook build`. Done.
Cross-file links resolve automatically — no merging, no sed, nothing to break.

---

## Workflow reminder

1. **Update content first** (videos, articles, courses into the right sections).
2. Push to GitHub as usual.
3. Run `mdbook build` to regenerate the PDF.

---

## Alternatives (if mdBook ever doesn't fit)

- **Honkit** — maintained GitBook fork, same `SUMMARY.md` model:
  `npm i -g honkit && honkit pdf ./ cookbook.pdf`
- **Quarto** — more powerful, multi-format, but its PDF path uses LaTeX which
  fights the raw HTML (`<div align>`, `<img>`) in these files. Only worth it if
  you rewrite the HTML bits as plain Markdown.
