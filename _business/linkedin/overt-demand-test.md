# Overt demand test - one post, $0

The question this answers: do strangers want their own AI-conversation psych report badly
enough to chase it? If yes, finishing Overt's worker pipeline is justified. If no, Overt
stays parked and you lost nothing.

## Step 1 - generate your own report

You don't need Overt finished for this. llm-archive already parses your exports locally.
Run your archive through it, then feed the output to Claude with the Psych Review prompt
from `apps/web/src/lib/reports/` in the overt repo. What you need out the other end is
2 or 3 specific, uncomfortable, quotable lines about how you think.

Screenshot the best section. Real screenshot, slightly rough. Not a designed card - the
authenticity is the hook.

## Step 2 - the post

> I ran three years of my own AI conversations through a tool I built. Every ChatGPT,
> Claude, Gemini and Grok export, all of it.
>
> The report it wrote about me was specific and a bit uncomfortable.
>
> [one real line from your report, e.g. the completion-rate pattern or a cognitive tell]
>
> It also worked out my actual project completion rate. I'm not sharing that one.
>
> Built it because I wanted to know what all those conversations say about how I think,
> and no single provider can see across them. Turns out the answer is: plenty.
>
> Screenshot's from my own report.

Attach the screenshot. No link, no product name, no waitlist URL. This post is a question
disguised as a story - the product doesn't exist publicly yet and saying so kills the test.

## Step 3 - the reply playbook

- "Can I get mine?" → "Maybe. It's not public yet - if I open it up I'll DM you. What
  providers do you use?" Log every one of these. This is the demand signal.
- "How does it work?" → answer honestly, point at the llm-archive repo (it's open source,
  costs you nothing, builds credibility).
- "Privacy??" → "Everything ran locally on my machine for this one. That's the standard the
  hosted version would have to meet." Don't over-promise architecture you haven't built.

## Step 4 - the threshold, decided in advance

Count over 7 days: genuine "I want mine" comments + DMs.

- **10 or more** → finish the Overt pipeline (worker + db, roughly the spec's sub-projects
  1, 2 and 4), DM everyone who asked, charge the $20 from day one. No free tier, per your
  own spec.
- **3 to 9** → run the post once more a month later with a different report excerpt before
  deciding. Two data points beat one.
- **Under 3** → park Overt without guilt and put the hours into audits and DoughBoy. The
  test cost one post.

## When to run it

Not before the Week 1-2 teasers have gone out - the post lands harder once your feed has
established the "chef who builds software" frame. Slot it as a bonus post in Week 3 or 4,
any day that isn't Tuesday/Thursday/Saturday.
