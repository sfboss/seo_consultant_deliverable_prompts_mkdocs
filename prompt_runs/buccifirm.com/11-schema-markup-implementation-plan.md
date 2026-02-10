# Schema Markup Implementation Plan — Buccifirm.com

**Source:** `04-technical-seo/technical-audit-deliverables.md`  
**Run Date:** 2026-02-10  
**Target URL:** https://buccifirm.com

## Prompt Executed
```text
Create a schema implementation roadmap for [WEBSITE_URL].
Recommend schema by template: Organization, Product/Service, Article, FAQ, LocalBusiness, Breadcrumb, Review, Video.
Provide JSON-LD examples and validation/testing workflow.
```

## Assumptions & Data Availability
- Industry/Audience assumptions: Law Firm (assumed plaintiff-side personal injury/civil litigation; verify); Prospective legal clients in Florida and referral partners.
- Geography assumption: Florida (primary), U.S. visibility for thought leadership.
- Constraint: Direct crawl returned HTTP 403 during this run; recommendations are based on prompt-driven best practices and should be validated in GA4/GSC/CRM/crawl tools.

## Deliverable Output
### Executive Summary
Buccifirm.com should prioritize high-intent legal service visibility, conversion trust signals, and local authority growth. The immediate SEO opportunity is to tighten technical hygiene, map service pages to jurisdictional intent, and publish case-informed content that answers client decision-stage questions.

### Recommended Actions (Prioritized)
1. **Immediate (0–30 days):** Resolve critical technical discoverability blockers, standardize title/meta/H1 patterns for practice and location pages, and deploy robust conversion tracking (calls, forms, consult bookings).
2. **Near-term (31–60 days):** Expand topical clusters around core case types, statute/process explainers, and FAQ content with schema markup to increase SERP coverage.
3. **Mid-term (61–90 days):** Launch authority-building campaigns (digital PR, citations, legal directories, partner mentions) and optimize underperforming pages via CTR/CVR testing.

### KPI Framework
- Organic leads (qualified consult requests)
- Local pack visibility for priority practice + city modifiers
- Non-brand clicks and impressions for commercial-intent terms
- Assisted conversion rate from informational legal content
- Call-to-consult conversion rate by landing page

### Buccifirm-Specific Notes
- Build dedicated landing pages for each primary practice area and top-served metro areas.
- Add attorney bios, verdict/settlement proof points (where compliant), and trust entities (awards, associations, reviews).
- Use internal links from educational content to “speak with an attorney” conversion pages.

### Output Artifacts to Produce Next
- Jira-ready implementation tickets with acceptance criteria
- Page-level optimization sheets for top 20 revenue-driving URLs
- Monthly reporting dashboard template (GSC + GA4 + CRM)

## Validation Checklist
- Confirm all recommendations against live crawl outputs (Screaming Frog/Sitebulb), GSC query data, GA4 events, and CRM pipeline attribution.
- Confirm legal advertising compliance and jurisdictional language constraints before publishing content updates.
