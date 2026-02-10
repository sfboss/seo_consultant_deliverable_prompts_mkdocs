# Technical Audit Deliverables

## Site Speed Optimization Recommendations

### Purpose
Create a prioritized performance roadmap for improving speed and UX signals.

### Client Value
Faster sites improve conversion rates and reduce ranking friction.

### Prompt
```text
Audit [WEBSITE_URL] and produce a site speed optimization plan.
Analyze server response, caching, render-blocking resources, JS/CSS payload, image delivery, and CDN usage.
Map recommendations to Core Web Vitals impact (LCP, INP, CLS) with effort estimates.
```

### Expected Output Format
Issue table + implementation order + KPI targets.

### Example Usage
`[WEBSITE_URL]=https://www.example.com`

### Tips for Best Results
Provide page-template level test data from mobile and desktop.

## Mobile Usability Audit

### Purpose
Evaluate mobile UX issues affecting rankings and conversions.

### Client Value
Improves engagement and form completion on mobile traffic.

### Prompt
```text
Perform a mobile usability audit for [WEBSITE_URL].
Review viewport setup, tap targets, font legibility, intrusive popups, navigation friction, and mobile conversion blockers.
Prioritize fixes by user impact and implementation effort.
```

### Expected Output Format
Usability findings with severity and remediation plan.

## Schema Markup Implementation Plan

### Purpose
Define structured data opportunities across templates.

### Client Value
Supports rich results and improved SERP visibility.

### Prompt
```text
Create a schema implementation roadmap for [WEBSITE_URL].
Recommend schema by template: Organization, Product/Service, Article, FAQ, LocalBusiness, Breadcrumb, Review, Video.
Provide JSON-LD examples and validation/testing workflow.
```

### Expected Output Format
Template-by-template schema matrix + JSON-LD examples.

## Site Architecture and Internal Linking Strategy

### Purpose
Optimize crawl paths and authority flow across core pages.

### Client Value
Improves indexation and ranking potential for money pages.

### Prompt
```text
Analyze the site architecture of [WEBSITE_URL] and design an internal linking strategy.
Include crawl depth, orphan-page recovery, hub-and-spoke models, anchor text guidance, and link equity flow improvements.
```

### Expected Output Format
Architecture map recommendations + internal linking backlog.

## Crawlability and Indexation Analysis

### Purpose
Identify indexing blockers and crawl inefficiencies.

### Client Value
Ensures strategic pages are discoverable, indexable, and consolidated.

### Prompt
```text
Run a crawlability/indexation analysis for [WEBSITE_URL].
Check robots directives, XML sitemaps, canonicals, noindex usage, redirect chains, duplicate URLs, and parameter handling.
Return critical issues first with implementation sequencing.
```

### Expected Output Format
Crawl/indexation issue log with severity and owner.

## Core Web Vitals Improvement Plan

### Purpose
Deliver a focused CWV recovery plan.

### Client Value
Supports long-term technical stability and search performance.

### Prompt
```text
Build a Core Web Vitals improvement plan for [WEBSITE_URL] by template and device class.
Set target thresholds, identify root causes, and provide phased fixes with QA criteria.
```

### Expected Output Format
CWV scorecard + 30/60/90 day engineering plan.

**Tags:** `technical` `advanced`
