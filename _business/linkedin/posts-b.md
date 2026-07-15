# LinkedIn posts B: build log + ideas set

Same rules as posts-a.md: no em dashes, link goes in the first comment, image attached from `images/`.

---

## §28 How I Built ClipTips with Claude Code
*Image: images/28.png*
*First comment: https://streamables.live/articles/28-how-i-built-cliptips-with-claude-code.html*

Six weeks. Solo. A knowledge marketplace with live video sessions, a token economy on Stripe, identity verification, and an AI translation pipeline.

Five years ago that's a funded team's roadmap for a year. I built it alone in Brisbane with Claude Code as the second pair of hands.

The build log covers the stack, what AI genuinely accelerated, what it broke, and what I'd do differently. No "AI built my app" fairy tale. It's a tool. You still have to be the builder. [link in first comment]

## §29 ClipTips Live Interpreter Mode is GA
*Image: images/29.png*
*First comment: https://streamables.live/articles/29-cliptips-live-interpreter-ga.html*

Two people who don't share a language can now hold a live video conversation on ClipTips, each hearing the other in their own language, in the speaker's own cloned voice, at roughly 250 to 400ms end to end.

That last number is the whole product. Above a second, conversation dies.

Shipped, in production, solo build. The log covers the latency stack, the cost lock-down and the V1.5 lipsync queue. [link in first comment]

## §31 The Latency Stack Walkthrough
*Image: images/31.png*
*First comment: https://streamables.live/articles/31-the-latency-stack-walkthrough.html*

The naive version of the ClipTips translation pipeline took about 2,600ms. Conversation is dead at that speed.

Production runs at roughly 300ms. The gain didn't come from faster models. It came from refusing to do things in sequence: streaming every stage, starting synthesis before transcription finishes, and treating the pipeline as five overlapping streams instead of five steps.

Real measurements, real configs, in the article. Parallelism beats per-stage speed. [link in first comment]

## §32 What I Actually Paid in 2026 to Run a Live Interpreter
*Image: images/32.png*
*First comment: https://streamables.live/articles/32-what-i-actually-paid-to-run-live-interpreter.html*

Everyone publishes architecture posts. Almost nobody publishes the bill.

So I did: verified provider pricing, per-session maths, and full margin tables for running live AI translation. Where the model works, where it breaks, and what the 1.5x session premium actually covers.

If you're building on paid AI APIs, the margin table is the product decision. [link in first comment]

## §33 Building V1.5 for $0 While Waiting for Budget
*Image: images/33.png*
*First comment: https://streamables.live/articles/33-building-v1-5-for-zero-while-waiting-for-budget.html*

Waiting on budget for the expensive API is not a reason to stop shipping.

About 70% of any paid-API feature can be built before you spend a cent: the UI, the queue, the storage, the fallbacks, the tests, the provider interface. The paid call slots in last, like an appliance into a finished kitchen.

Case study from the ClipTips V1.5 lipsync build in the article. [link in first comment]

## §34 The Provider Abstraction Pattern
*Image: images/34.png*
*First comment: https://streamables.live/articles/34-the-provider-abstraction-pattern.html*

ClipTips depends on seven external services. Video, transcription, translation, voice, email, payments, identity.

Every one of them sits behind a small interface I own. Three files per provider, selection by environment variable, vendor swaps in minutes instead of rewrites.

Solo builders need this more than teams do: you can't afford a fortnight of migration every time a vendor changes pricing. The pattern, with code, in the article. [link in first comment]

## §35 Mistakes, Captured Honestly
*Image: images/35.png*
*First comment: https://streamables.live/articles/35-mistakes-captured-honestly.html*

My build log includes the failures. On purpose.

Documentation that hides mistakes doesn't teach. And a public log where errors are visible creates an accountability loop that private notes never do: you fix things properly when you know they'll be read.

Six weeks of honest session logs taught me more than any tutorial. The practice, and what it caught, in the article. [link in first comment]

## §30 AI Identifiers: How to Spot AI Usage
*Image: images/30.png*
*First comment: https://streamables.live/articles/30-ai-identifiers-how-to-spot-ai.html*

You can usually tell when text was written by AI and pasted unedited. The tells are consistent: the same sentence rhythms, the same filler phrases, the em dashes everywhere.

I keep a working list of those patterns, partly as a filter for inbound, partly as a style guide for my own writing. If a machine helped, fine. If nobody edited it, it shows, and it tells your reader you didn't care enough to.

The full field guide is in the article. [link in first comment]

## §04 AI That Helps You vs AI That Harvests You
*Image: images/04.png*
*First comment: https://streamables.live/articles/04-ai-that-helps-vs-ai-that-harvests.html*

Two AI tools can look identical in the demo and be opposites underneath.

One works for you: your data stays yours, the value lands in your business.
One works on you: the product is your data, and you're paying to hand it over.

The tell is rarely on the pricing page. I wrote up the questions that expose which one you're looking at, before you sign. [link in first comment]

## §11 Multi-Agent AI: What It Actually Means for Your Business
*Image: images/11.png*
*First comment: https://streamables.live/articles/11-multi-agent-ai-what-it-actually-means.html*

"Multi-agent AI" sounds like conference noise, so here's the plain version: instead of one assistant that does everything badly, several small specialists with defined jobs, coordinating, with a human in charge.

For a business it's the difference between hiring one overwhelmed generalist and running an actual team with roles.

What that structure looks like and when it's worth it. [link in first comment]

## §12 Who Actually Owns Your AI Assistant?
*Image: images/12.png*
*First comment: https://streamables.live/articles/12-who-actually-owns-your-ai-assistant.html*

You've told your AI assistant more about your business than you've told your accountant.

Now read the terms of service and check who owns that conversation history, who can train on it, and what happens to it when you close the account.

Ownership questions feel abstract until the answer matters. Then they're the only questions. [link in first comment]

## §05 The Accountability Vacuum at the Heart of AI
*Image: images/05.png*
*First comment: https://streamables.live/articles/05-accountability-vacuum-ai-governance.html*

Ask yourself who has faced meaningful personal consequences for an AI system's failure. Anywhere. Ever.

Software that makes decisions has arrived; accountability for those decisions hasn't. That vacuum is the most under-priced risk in the whole industry, and it won't be filled by vendors volunteering.

What an accountability structure could actually look like. [link in first comment]

## §07 What Happens When the AI Makes the Call?
*Image: images/07.png*
*First comment: https://streamables.live/articles/07-what-happens-when-ai-makes-the-call.html*

The interesting failure isn't AI giving bad advice. It's AI making the decision, with no human in the loop, and everyone downstream assuming someone approved it.

The safety line isn't "human oversight" as a slogan. It's knowing exactly which decisions the system may make alone, which need sign-off, and writing that boundary down before the incident, not after. [link in first comment]

## §14 The Knowledge Economy: Who Actually Gets Paid?
*Image: images/14.png*
*First comment: https://streamables.live/articles/14-knowledge-economy-who-gets-paid.html*

The person who can answer your question exists. They're just not the one getting paid when you search for the answer.

Platforms monetise expertise; experts mostly don't. That gap is the reason I built a marketplace where the expert gets 75% and the session is translated live so language stops gating who can sell what they know. [link in first comment]

## §08 Data Sovereignty Isn't a Privacy Setting. It's an Economic Right.
*Image: images/08.png*
*First comment: https://streamables.live/articles/08-data-sovereignty-economic-right.html*

Privacy talk frames your data as something to hide. Wrong frame.

Your data is something you produce. An asset. And right now the production is yours while the revenue is someone else's.

Sovereignty means the default flips: you hold it, you licence it, you can leave with it. The economic case, not the paranoid one. [link in first comment]

## §15 Sovereign Data Architecture: A Primer
*Image: images/15.png*
*First comment: https://streamables.live/articles/15-sovereign-data-architecture-primer.html*

If the data isn't owned by the user, nothing built on top of it is either.

The primer covers the three pieces that make ownership real rather than rhetorical: local-first storage, encrypted sync, and identity you can prove without a third party vouching for you.

A reference architecture any developer could implement. [link in first comment]

## §06 Reputation Will Replace Credentials. Just Not the Way You Think.
*Image: images/06.png*
*First comment: https://streamables.live/articles/06-reputation-will-replace-credentials.html*

A degree says someone vouched for you once. A track record says the work keeps vouching for you.

The shift to reputation is real, but the naive version (star ratings everywhere) is a mess of manipulation. The interesting question is what makes a reputation signal trustworthy, portable, and hard to fake. [link in first comment]

## §10 Karma Beats Credit Scores
*Image: images/10.png*
*First comment: https://streamables.live/articles/10-karma-beats-credit-scores.html*

A credit score knows one thing about you: how you handle debt. It stands in for trustworthiness everywhere anyway.

What if the record covered what you've actually done: delivered, repaid, contributed, resolved? Verifiable, portable, yours?

That's the karmic ledger idea, and it's more practical than it sounds. [link in first comment]

## §13 The Practical Case for On-Chain Reputation
*Image: images/13.png*
*First comment: https://streamables.live/articles/13-on-chain-reputation-practical-case.html*

Your reputation currently lives on platforms. It can't move with you, it can be deleted, and it dies with the platform.

The practical case for putting reputation on-chain isn't crypto ideology. It's portability and tamper-resistance for the one asset freelancers, traders and small operators actually run on. [link in first comment]

## §21 The Identity Problem the Internet Never Solved
*Image: images/21.png*
*First comment: https://streamables.live/articles/21-soul-token-identity-problem-internet-never-solved.html*

Thirty years in and the internet still can't answer "is this the same person as last time?" without a corporation in the middle.

Every platform re-solves identity badly, and you rent a different self from each. What self-owned identity would take, and why it keeps not happening. [link in first comment]

## §18 The Creator Economy Is Broken. Here's What's Actually Wrong With It.
*Image: images/18.png*
*First comment: https://streamables.live/articles/18-creator-economy-broken-fix.html*

The creator economy's problem isn't too few creators or too little content. It's that the middle layer takes most of the money for owning the pipe.

Distribution captured the value; creation didn't. What a fairer split looks like structurally, not charitably. [link in first comment]

## §24 Behaviour Change Is a Data Problem
*Image: images/24.png*
*First comment: https://streamables.live/articles/24-growfree-ai-behaviour-change-data.html*

Most behaviour change fails for a boring reason: no honest feedback loop. You can't steer what you don't measure.

AI finally makes the measurement cheap enough to be personal. What that unlocks, and the obvious trap in who holds the data. [link in first comment]

## §19 The Most Ambitious AI Ethics Experiment Nobody's Talking About
*Image: images/19.png*
*First comment: https://streamables.live/articles/19-umb-most-ambitious-ai-ethics-attempt.html*

Most AI ethics work is a PDF nobody operationalises.

The experiment I find genuinely interesting tries to make ethics structural: rules encoded into how the system runs, with accountability attached, rather than principles pinned to a wall. Worth knowing about even if it fails. [link in first comment]

## §23 Why AI Agents Need Real-World Anchoring
*Image: images/23.png*
*First comment: https://streamables.live/articles/23-why-ai-needs-real-world-anchoring.html*

An AI agent with no stake in the physical world can generate infinite plausible nonsense at zero cost.

Anchoring changes that: identity, cost, consequence, something real to lose. Without it, agent ecosystems drown in their own output. With it, they start resembling economies. [link in first comment]

## §22 UBI Funded by Data, Not Taxes
*Image: images/22.png*
*First comment: https://streamables.live/articles/22-ubi-funded-by-data-not-taxes.html*

Everyone's data generates revenue today. It's just collected by whoever built the app.

Run the thought experiment: if that value were metered and returned to the people producing it, you get a dividend that isn't funded by taxation. The mechanics are harder than the slogan, which is exactly why they're worth working through. [link in first comment]

## §27 When Does an AI Agent Deserve Standing?
*Image: images/27.png*
*First comment: https://streamables.live/articles/27-when-does-an-ai-agent-deserve-standing.html*

An AI agent can hold money, sign transactions and build a track record. At what point does the legal system need a category for that?

Not personhood. Standing: the ability to be a party to something. The gap between what agents already do and what the law recognises is widening fast. [link in first comment]
