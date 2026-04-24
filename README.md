# Bridewell AI — Teacher Dashboard (KESW)

Mockup demo of the **Teacher Layer (S3)** for the Bridewell AI chat system at **King Edward's Witley**.
Pair-Up-inspired grid layout, 10 Year-5 pupils, click any card to see their passport.

## Files

| File | Purpose |
|---|---|
| `index.html` | Login page with KESW crest |
| `dashboard.html` | Main teacher UI — grid, passport, charts, prompt editor |

## What the dashboard shows

**Top bar** — school crest, class selector (Year 5 · Alpha), teacher chip.

**Page header** — personalised greeting + live metrics (Active / Msgs today / Needs help / Focus / On-task).

**Student grid (10 pupils, 5×2)** — compact cards like the Pair-Up paper. Each card shows name, coloured human icon (red/amber/green/grey), subject, last message snippet, and progress bar. Red and amber icons pulse. The four actively-chatting pupils (Tom, Priya, Samira, Oliver) sit at the top of the grid with contextual flags.

**Suggested Pair-Ups strip** — complementary-knowledge matches straight out of the Pair-Up research (Solver × Tutor colour coding preserved).

**Right panel — Individual / Pair tabs.**
- *Individual tab:* full Student Passport (reading age, avatar, preferred mode, SEND adaptations, strengths/growth areas), AI briefing, live 4-cell analysis (cognitive load, engagement, help-seeking, misconception), recent transcript, and 4–5 actionable buttons for human-in-the-loop.
- *Pair tab:* active pair suggestion with Solver/Tutor slots, shared task, "Start Pair-Up" button, other suggestions, and a log of past pair-ups from today.

**Bottom charts (4, real-time analysis of student chat logs):**
1. **Cognitive Load per active pupil** — bar chart with "high load" threshold line
2. **Engagement over 30 min** — multi-line timeline (Samira, Oliver, Priya dipping, Tom low)
3. **Topics pupils are wrestling with** — ranked list with heat colouring
4. **Behaviour Mix** — radial donut: deep questions / scaffolded / off-topic / answer-seeking

**Floating FAB → System Prompt Designer modal** — subject tabs, Expert/Guidance mode toggle, editable prompt, guardrail checkboxes.

## The 10 pupils

| # | Pupil | Status | Subject |
|---|---|---|---|
| 1 | Tom W. | 🔴 Red — urgent | Fractions (looping) |
| 2 | Priya N. | 🟡 Amber — focus | Creative Writing (SEND) |
| 3 | Samira K. | 🟢 Green | Fractions (just mastered) |
| 4 | Oliver B. | 🟢 Green | Creative Writing (deep Qs) |
| 5 | George S. | 🟡 Amber | Phonics |
| 6 | Daisy H. | 🟢 Green | Phonics |
| 7 | Freya M. | 🟢 Green | Fractions |
| 8 | Aarav P. | ⚪ Idle | — |
| 9 | Mia O. | 🟢 Green | Creative Writing |
| 10 | Leo F. | ⚪ Idle | — |

Click any of the top 4 (Tom / Priya / Samira / Oliver) to see their full passport, analysis, and transcript populate in the right panel. Priya is pre-selected.

## Host on GitHub Pages

```bash
git init
git add .
git commit -m "Teacher dashboard mockup"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

Then **Settings → Pages → Source: `main` / root → Save.** Site goes live at `https://<you>.github.io/<repo>/`.

Both buttons on the login page route to `dashboard.html`.

## Design notes

- **Palette:** deep ink navy · warm parchment cream · heritage crimson · gold — drawn from the school's 1553 royal-charter origins
- **Typography:** Fraunces (display serif), Instrument Serif (italics), Inter Tight (UI), JetBrains Mono (data labels)
- **Crest:** hand-drawn SVG placeholder — swap for official KESW branding when you have it
- **No framework:** pure HTML + CSS + vanilla JS. No build step, no dependencies

## Next steps

- Wire grid to `/api/sessions/live` and stream updates via WebSocket
- Pull cognitive-load / engagement scores from the analyser models
- Persist pair-ups and prompt edits to the Bridewell AI backend
- Replace inline crest SVG with the official KESW branding pack
- Auth against the school's Microsoft tenant
