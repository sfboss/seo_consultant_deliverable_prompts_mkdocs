# Competitive Analysis Prompts

## Competitor Identification and Ranking Comparison

### Purpose
Identify true SEO competitors and compare visibility by topic cluster.

### Client Value
Refocuses strategy around competitors actually winning SERPs, not just business competitors.

### Prompt
```text
Identify the top SEO competitors for [WEBSITE_URL] in [INDUSTRY] for [GEOGRAPHIC_LOCATION].
Compare visibility, ranking footprint, and keyword overlap.

Deliver:
- Competitor shortlist (primary, secondary, emerging)
- Share-of-voice estimate by topic cluster
- Top pages driving competitor traffic
- Terms where [WEBSITE_URL] is within striking distance (positions 4-20)
```

### Expected Output Format
Competitor matrix + opportunity list with priorities.

**Tags:** `beginner` `advanced`

---

## Competitor Content + Backlink + SERP Feature Analysis

### Purpose
Reverse-engineer competitor content depth, link acquisition, and SERP feature capture.

### Client Value
Improves win rate by adapting proven tactics to your brand context.

### Prompt
```text
Perform a deep competitor SEO analysis for [COMPETITOR_URLS] against [WEBSITE_URL].

Include:
1) Content strategy analysis
- Pillars, clusters, update cadence, format mix
2) Backlink strategy analysis
- Link source patterns, anchor text themes, referring domain quality
3) SERP feature analysis
- Featured snippets, PAA, local pack, image/video, FAQ rich results

Output actionable recommendations prioritized by impact/effort.
```

### Example Usage
`[WEBSITE_URL]=https://example-saas.com` and 3-5 direct search competitors.

### Follow-up Prompts
- "Translate this into a 90-day anti-competitive action plan."

**Tags:** `advanced` `technical`
