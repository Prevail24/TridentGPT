

# TridentGPT Roadmap

**Project Codename:** TridentGPT  
**Parent World:** The Watchers  
**Purpose:** A battle-tested OSINT CTF co-pilot for authorized investigations, Hack The Box challenges, training labs, and Watchers-style field reports.

TridentGPT is not just a prompt pack. It is intended to become a practical investigation system: part methodology, part skill library, part OSINT notebook, part field-report engine.

---

## Core Identity

TridentGPT exists to help an investigator move from scattered clues to defensible conclusions.

The system should always support the Trident Loop:

1. **Collect** — gather visible clues, metadata, usernames, domains, images, dates, locations, and artifacts.
2. **Correlate** — connect clues across sources, timelines, identities, domains, files, and platforms.
3. **Conclude** — produce evidence-backed hypotheses, confidence levels, rejected leads, next pivots, and final reports.

The Watchers layer adds tone, identity, and report style, but the tool must remain useful in real CTF work.

---

## Version Milestones

## v0.1 — Foundation

Goal: Preserve the original Claude-OSINT material and add the first TridentGPT layer.

- [ ] Keep `osint-methodology` as an original/reference skill.
- [ ] Keep `offensive-osint` as an original/reference skill.
- [ ] Add `trident-methodology` skill.
- [ ] Add `trident-osint-ctf` skill.
- [ ] Create the first TridentGPT README.
- [ ] Define the Trident Loop.
- [ ] Define authorized-use boundaries.
- [ ] Add basic CTF response format.

---

## v0.2 — CTF Workflow Kit

Goal: Make TridentGPT useful during real Hack The Box OSINT challenges.

- [ ] Add challenge intake template.
- [ ] Add evidence log template.
- [ ] Add pivot log template.
- [ ] Add timeline template.
- [ ] Add final flag report template.
- [ ] Add confidence scoring format.
- [ ] Add rejected-leads section.
- [ ] Add next-pivot recommendation format.

---

## v0.3 — OSINT Playbooks

Goal: Build reusable playbooks for common OSINT challenge types.

- [ ] Username investigation playbook.
- [ ] Domain and subdomain investigation playbook.
- [ ] Image geolocation playbook.
- [ ] Metadata and file artifact playbook.
- [ ] Social media pivoting playbook.
- [ ] Archive and Wayback investigation playbook.
- [ ] Email and handle correlation playbook.
- [ ] Map/location clue playbook.

---

## v0.4 — Watchers Reporting Layer

Goal: Add optional Watchers-style reporting without weakening the practical OSINT workflow.

- [ ] Add Watchers Observation Report template.
- [ ] Add Observer Notes format.
- [ ] Add archive-style classification levels.
- [ ] Add evidence table with confidence ratings.
- [ ] Add field report mode.
- [ ] Add case-file naming convention.
- [ ] Add final report style for The Watchers project.

---

## v0.5 — Helper Scripts

Goal: Begin turning repeated manual steps into tools.

- [ ] Add regex extractor for emails, domains, handles, URLs, hashes, and coordinates.
- [ ] Add evidence log generator.
- [ ] Add pivot log generator.
- [ ] Add markdown report generator.
- [ ] Add filename and metadata checklist helper.
- [ ] Add basic local artifact organizer.

---

## v0.6 — Battle Testing

Goal: Use TridentGPT in real CTF practice and improve it from actual failures.

- [ ] Test against beginner HTB OSINT challenges.
- [ ] Record what helped.
- [ ] Record what slowed the investigation down.
- [ ] Add missing pivots.
- [ ] Remove unnecessary fluff.
- [ ] Improve templates from real usage.
- [ ] Create example solved case reports.

---

## v1.0 — Field-Ready Release

Goal: Make TridentGPT usable as a complete OSINT CTF assistant.

- [ ] Stable README.
- [ ] Stable Trident methodology.
- [ ] Stable CTF skill.
- [ ] Complete template pack.
- [ ] Complete playbook pack.
- [ ] Watchers report mode.
- [ ] At least three tested example cases.
- [ ] Clear safety and authorized-use policy.
- [ ] Clean repo structure.

---

## Long-Term Vision

TridentGPT should eventually become the OSINT engine of The Watchers.

It should support:

- CTF challenge solving.
- Public-source investigation practice.
- Training and education.
- Watchers case-file generation.
- Evidence-backed reports.
- Repeatable investigative methodology.
- A growing library of field-tested playbooks.

The end goal is not just to answer questions. The end goal is to build an investigator's operating system.

---

## Development Rule

Every feature should answer one question:

> Does this help an Observer move from clue to evidence to conclusion?

If yes, build it.  
If no, archive it.