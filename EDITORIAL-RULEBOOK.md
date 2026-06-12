# Cookbook Editorial Rulebook

The rules for what goes into the Data Engineering Cookbook, what stays out, and
how everything cross-links. Read this before adding or restructuring content.
If an edit breaks a rule here, the rule wins — or we change the rule on purpose.

---

## 1. What the Cookbook IS

The Cookbook is the **wide map of the field** and the **on-ramp**. Its job is to
help a reader understand the 2026 data-engineering landscape, locate themselves
in it, and learn *how to think* — then route them to the right deeper resource.

It is the **discovery layer**: the broad, browsable, GitHub/SEO surface that
pulls strangers in and turns them into email subscribers.

The Cookbook owns:
- **The 2026 worldview** — how the field splits (data / analytics / ML / AI
  engineering), what changed, where a reader fits.
- **Roadmaps / "Start Here"** — the on-ramp paths by role and level.
- **Judgment & decisions** — "lake vs warehouse vs lakehouse," "stream vs
  batch," "do you even need big data." The *why* and *how to choose*.
- **Patterns & concepts** — mental models, architecture thinking, trade-offs.
- **The breadth net** — case studies, interview questions, data sources. The
  surface that attracts traffic.

## 2. What the Cookbook is NOT

- **NOT a tool catalog.** It never lists "all the tools for the Process phase."
  That is the Tools Guide's job (see §3). When a reader asks "but which tool?",
  the Cookbook *links to the Tools Guide* — it does not answer inline.
- **NOT a build manual.** Step-by-step pipeline builds live in courses /
  hands-on content, not here.
- **NOT a dumping ground for links.** Resources are woven in at the point of
  curiosity (see §5), not collected in an end chapter.

> **The one-sentence test:** if a paragraph could be replaced by a row in the
> Tools Guide matrix, it does not belong in the Cookbook.

---

## 3. Division of labor (Cookbook vs Tools Guide vs the rest)

| Layer | Document | Owns | Funnel role |
|---|---|---|---|
| **Map** | **Cookbook** | Worldview, roadmaps, decisions, concepts, breadth net | Discovery → email capture |
| **Mechanics** | **Tools Guide** | Blueprint phases, tool matrix, pipeline patterns, project→course links | Focused magnet → Academy |
| **Depth** | **Free content** (YT / LinkedIn / Udemy / free courses) | How-to, demos, tutorials | Woven inline everywhere |
| **Paid apex** | **Academy → Masterclass** | Full courses, certification | Apex CTA |

**Rule:** each fact has exactly one home. The blueprint *mechanics and tool
catalog* live in the Tools Guide. The Cookbook references them; it never
re-creates them.

When the Cookbook touches the blueprint (Connect → Buffer → Process → Store →
Visualize), it stays at the **decision/concept** altitude and hands off:

> *"…for the full tool catalog and cloud-native vs open-source alternatives for
> this phase, grab the Tools Guide → {{TOOLS_GUIDE_CTA}}"*

That hand-off is also a funnel step (email capture / Academy jump). One move,
both goals.

---

## 4. The funnel ladder (where every CTA points)

Every piece of content should make the next step obvious. The ladder:

1. **Cookbook** (free, broad) → capture the **email via download**.
2. **Tools Guide** (focused magnet) → another capture / Academy jump.
3. **Free content** (YT / LinkedIn / courses) → woven inline at each decision.
4. **Academy → Masterclass** (paid apex) → the deep "go further" CTA.

Goals, in order: build trust → capture email → drive views to (sponsored) free
content → upsell to the paid tier.

---

## 5. The inline-link pattern (how resources are woven in)

Resources appear **at the point of curiosity**, never in a separate chapter.
Model: the Tools Guide's example-projects move — concept → diagram → "here's the
course."

After a concept or decision, attach the relevant exits:

```markdown
## Storing your data: lake, warehouse, or lakehouse?

[2–3 paragraphs of opinionated judgment — when each makes sense, the trade-off
that trips people up, what I'd pick and why.]

> 🎥 Watch: [video]
> 📝 Read: [article / LinkedIn post]
> 🧰 Full tool catalog for this phase: {{TOOLS_GUIDE_CTA}}
> 🎓 Build it hands-on: [free course]
> 🚀 Go deeper: {{MASTERCLASS_CTA}}
```

Rules for inline links:
- Only attach links that genuinely fit the topic. No padding.
- A topic with no link yet = a visible gap = your content backlog. Leave the
  block; it tells you what to record next.
- Prose carries the value. Links are exits, not the substance.

---

## 6. CTA tokens (define once, reuse everywhere)

Never hard-code campaign links inline. Use tokens so a single edit re-points the
whole book — critical for the planned Academy→free / Masterclass→paid switch.

| Token | Means | Today points to |
|---|---|---|
| `{{DOWNLOAD_CTA}}` | Get the PDF / join the mailing list | email-capture page |
| `{{TOOLS_GUIDE_CTA}}` | Get the Tools Guide | Tools Guide download |
| `{{MASTERCLASS_CTA}}` | The paid apex | Academy (later: Masterclass) |
| `{{ACADEMY_CTA}}` | The course platform | LearnDataEngineering.com |

When the business model changes, update the token definitions in one place — not
the content.

---

## 7. Modernization rules (keeping it "2026")

- **Lead with current.** Modern Data Stack, lakehouse + table formats
  (Iceberg / Delta / Hudi), the AI-data layer (vector DBs, embeddings, RAG,
  feature stores), DataOps / observability / contracts / catalogs.
- **Don't delete history — relabel it.** Legacy tech (MapReduce, Sqoop, Flume,
  Storm, Samza, Drill, Solr) becomes a short *"Legacy / know-it-exists"* note,
  not a deep section.
- **Reframe "Data Science" → the four destination roles** (data / analytics /
  ML / AI engineering) wherever the old framing appears. See §9 for how these
  relate to the origin-based roadmaps — don't conflate the two.
- **Surface, don't bury** (see §10). Hot, in-demand topics — AI engineering
  above all — get direct entry points near the top, not a subsection three
  levels deep.
- **Opinion over completeness.** A clear recommendation beats an exhaustive
  survey. Surveys are the Tools Guide's job.

---

## 8. Quick decision guide ("where does this go?")

- Explaining *why* or *how to choose* → **Cookbook**.
- Listing *which tools exist* for a phase → **Tools Guide** (link to it).
- Step-by-step *how to build* it → **course / free content** (link to it).
- A real resource (video / article / course) → **inline, at the topic**.
- "All the resources in one place" → **no.** See §5.

---

## 9. Paths & roadmaps: two axes (don't conflate them)

Two different questions, two different structures. Mixing them is the most
likely structural mistake — keep them separate.

| Axis | Answers | Keyed on | Owner |
|---|---|---|---|
| **Destination** | "What are the DE-adjacent roles in 2026, which do I want?" | where you're **going** | Cookbook-owned field map |
| **Origin** | "I'm an analyst / dev / grad — how do I get in from here?" | where you're **coming from** | mirrors the LDE roadmaps 1:1 |

**Destination → the field map.** A Cookbook-owned worldview section: data /
analytics / ML / AI engineering as distinct roles. Pure orientation, no funnel
pressure — it serves the reader who doesn't yet know what they want. No LDE
dependency.

**Origin → the "Start Here" roadmaps.** These mirror the LDE roadmap selector
1:1 (Beginner / Data Analyst / Data Scientist / Software Developer). The Cookbook
gives the *free orientation* for each ("the path from where you are"); each one's
apex CTA deep-links to the matching **paid** LDE roadmap. The Cookbook never
reproduces the week-by-week curriculum (§2).

- Roadmap selector: https://learndataengineering.com/p/roadmap-selector
- Canonical origin roadmaps = Beginner · Data Analyst · Data Scientist ·
  Software Developer. Name them to match LDE so the funnel is 1:1.

**AI Engineering straddles both.** On LDE it's a *destination* ("become an AI
engineer"), not an origin like the other four. So it appears in the field map as
a first-class role **and** as a surfaced roadmap on-ramp — flagged as "where
you're going," not "where you came from."

---

## 10. Surface, don't bury

On a five-year-old wide map, the topics people actually search for get buried
under accumulated structure unless we deliberately surface them. Don't let that
happen — give in-demand topics direct entry points near the top, the same way
the LDE site routes people straight to AI engineering instead of hiding it.

**Worked example — AI engineering appears in three surfaced places, not one:**
- In the **field map** as a first-class destination role (§9).
- As a **direct on-ramp / CTA** to the AI Engineering roadmap.
- As the **AI-data layer** woven through the blueprint — vector DBs, embeddings,
  RAG, feature stores — connecting to the existing Ollama/RAG tutorials in
  `sections/04-HandsOnCourse.md`.

**Why it matters for the funnel:** the surfaced AI on-ramp *is* a top-of-funnel
magnet, because it matches what strangers are searching for in 2026. Burying it
wastes the exact traffic we most want to capture.

**Rule of thumb:** if a topic is in high demand and a reader would expect to find
it fast, it gets a surfaced entry point — not a deep subsection.
