# Initial Site Audit Prompts

## Technical SEO Audit Deliverable

### Purpose
Generate a complete technical SEO audit for `[WEBSITE_URL]`, including crawlability, indexation, performance, and architecture issues.

### Client Value
Creates an implementation-ready issue backlog that reduces ranking risk and unlocks growth.

### Prompt
```text
Act as a senior technical SEO consultant. Build a full technical SEO audit for [WEBSITE_URL] in [INDUSTRY] targeting [TARGET_AUDIENCE] in [GEOGRAPHIC_LOCATION].

Include:
- Crawlability and indexation checks (robots.txt, XML sitemap, canonical, noindex, redirect chains)
- Page speed and Core Web Vitals priorities
- Mobile usability issues
- Site architecture and internal linking risks
- Structured data opportunities
- Duplicate content and URL parameter risks

Provide:
1) Executive summary
2) Findings table with severity (Critical/High/Medium/Low)
3) Prioritized 30/60/90 day remediation plan
4) KPI impact estimate per recommendation
5) Stakeholder summary for non-technical leadership
```

### Expected Output Format
Audit report with severity scoring, implementation roadmap, and KPI impact model.

### Example Usage
Use placeholders: `[WEBSITE_URL]=https://www.acmehvac.com`, `[INDUSTRY]=Home Services`, `[TARGET_AUDIENCE]=Homeowners in suburban markets`.

### Follow-up Prompts
- "Convert the critical items into Jira tickets with acceptance criteria."
- "Create QA test cases for each fix."

### Tips for Best Results
Provide GSC and analytics exports for higher-confidence recommendations.

**Tags:** `technical` `advanced`

---

## Content Inventory and Gap Analysis

### Purpose
Map current content coverage and identify missing high-value topics.

### Client Value
Helps allocate content investment toward topics with measurable traffic/conversion potential.

### Prompt
```text
You are an SEO content strategist. Analyze [WEBSITE_URL] and produce a content inventory + gap analysis for [INDUSTRY].

Inputs:
- Current sitemap/pages
- Top competitors: [COMPETITOR_URLS]
- Audience: [TARGET_AUDIENCE]
- Goals: [PRIMARY_GOALS]

Output:
- Content inventory by page type and intent
- Gap matrix by funnel stage
- Topic opportunities with estimated traffic potential
- Priority scoring: Business Impact x Ranking Difficulty x Content Effort
- 12-week execution plan
```

### Expected Output Format
Inventory table + gap matrix + prioritized content roadmap.

### Example Usage
`[COMPETITOR_URLS]=competitorA.com, competitorB.com, competitorC.com`.

### Tips for Best Results
Provide existing content performance by clicks, impressions, and assisted conversions.

**Tags:** `beginner` `creative`

---

## Current Ranking and Backlink Baseline

### Purpose
Establish a benchmark for rankings, visibility, and authority.

### Client Value
Creates a measurable “before” snapshot for quarterly SEO impact reporting.

### Prompt
```text
Build a baseline SEO benchmark for [WEBSITE_URL].

Include:
- Current ranking distribution by position buckets (1-3, 4-10, 11-20, 21-50)
- Keyword intent mix and non-brand vs brand split
- Backlink profile quality assessment (authority, relevance, toxicity risk)
- Competitor overlap and missed opportunity terms
- 10 key benchmark KPIs with definitions and data sources

Present findings for executive and practitioner audiences.
```

### Expected Output Format
Benchmark dashboard definitions + annotated narrative.

### Follow-up Prompts
- "Create a monthly template to track movement against this baseline."

**Tags:** `advanced` `technical`
