# LinkedIn posts B: build log + ideas set

Rewritten against resources/anti-ai-style-guide.md, built from each article's own opening prose.
Same drill: post the teaser, paste the First comment link immediately as your own comment.

---

## §28 How I Built ClipTips with Claude Code
*Image: images/28.png*
*First comment: https://streamables.live/articles/28-how-i-built-cliptips-with-claude-code.html*

ClipTips is a live video marketplace where you book a verified expert by the minute, ask your question on camera, and hear the answer in your own language in real time. A Spanish chef can take a session from a Japanese asker without either of them typing a word.

I started it in August 2025, paused for months when other things took over, picked it back up in April. Built solo, in Brisbane, with Claude Code doing the second pair of hands.

The build log covers what the AI genuinely accelerated, what it broke, and what I'd do differently. No "AI built my app" fairy tale. You still have to be the builder.

Link in the comments.

## §29 ClipTips Live Interpreter Mode is GA
*Image: images/29.png*
*First comment: https://streamables.live/articles/29-cliptips-live-interpreter-ga.html*

Two days before this article went up, ClipTips couldn't do real-time cross-language conversation. Now it can.

Speaker A talks in English. Speaker B hears A's actual cloned voice, not a synthesised stand-in, speaking Vietnamese or Spanish or any of 100+ languages, with live captions running underneath. End-to-end latency sits around 250 to 400ms.

That latency number is the whole product. Past a second, conversation dies.

The write-up covers how it works and what it took. Comments.

## §31 The Latency Stack Walkthrough
*Image: images/31.png*
*First comment: https://streamables.live/articles/31-the-latency-stack-walkthrough.html*

This one's a tutorial. If you're building real-time AI pipelines and keep hitting "it works but it feels laggy," it's for you.

The naive version of the ClipTips interpreter pipeline ran about 2,600ms end to end. Production runs at roughly 300ms. The gain didn't come from faster models. It came from refusing to do things in sequence: every stage streams, and synthesis starts before transcription finishes.

Actual measurements and configs in the article, not vibes. Link below.

## §32 What I Actually Paid in 2026 to Run a Live Interpreter
*Image: images/32.png*
*First comment: https://streamables.live/articles/32-what-i-actually-paid-to-run-live-interpreter.html*

Provider pricing pages are written for finance teams. Cents per second, characters per credit, and never what an actual production session costs you.

So I wrote the version I wish someone had handed me a month earlier. What each of the five paid services in a ClipTips session actually costs, the per-session maths, and the full margin tables. Including where the model breaks.

If you're building on paid AI APIs, you're making the margin-table decision whether you've written it down or not. Comments.

## §33 Building V1.5 for $0 While Waiting for Budget
*Image: images/33.png*
*First comment: https://streamables.live/articles/33-building-v1-5-for-zero-while-waiting-for-budget.html*

The wrong move when you're solo, unfunded, and need a feature that costs API budget you don't have: wait for the budget, then build the whole thing in one block.

The right move: build everything around the paid API for $0 right now. The UI, the queue, the storage, the fallbacks, the tests. Around 70% of the feature ships before you spend a cent, and the paid call slots in last.

Case study from the ClipTips lipsync build, link below.

## §34 The Provider Abstraction Pattern
*Image: images/34.png*
*First comment: https://streamables.live/articles/34-the-provider-abstraction-pattern.html*

Every external dependency in ClipTips sits behind a small provider abstraction. Seven of them: transcription, TTS, lipsync, voice cloning, translation, video calls, email. Same shape every time. An interface, an implementation or two, a factory that picks one off env vars.

It looks like over-engineering right up until the day a vendor changes their pricing and the swap takes minutes instead of a fortnight.

On a solo build this is the highest-leverage pattern I know. Code's in the article.

## §35 Mistakes, Captured Honestly
*Image: images/35.png*
*First comment: https://streamables.live/articles/35-mistakes-captured-honestly.html*

Three days into writing a public build log I noticed something I didn't expect: knowing the article was going public forced me to capture mistakes I'd normally let slide.

The session log is 162 lines of what I shipped, the friction I hit, and what carries forward. The "what I shipped" part is easy. The mistakes are the part actually worth reading.

Why I keep them in, link's in the comments.

## §30 AI Identifiers: How to Spot AI Usage
*Image: images/30.png*
*First comment: https://streamables.live/articles/30-ai-identifiers-how-to-spot-ai.html*

I got an email from a stranger this week. Software engineer at a Turkish university, decent profile, active GitHub. The email itself was clearly written with ChatGPT. Em dashes, generic flattery, vague specifics that sound technical but commit to nothing.

The annoying part: he wasn't a fraud. Real person, English as a second language, leaned on AI to tidy his prose before sending. And it sank his email anyway, because the tells read as "didn't bother."

The full field guide of tells is in the article, along with a free style-guide file you can drop straight into your own AI tools. Comments.

## §04 AI That Helps You vs AI That Harvests You
*Image: images/04.png*
*First comment: https://streamables.live/articles/04-ai-that-helps-vs-ai-that-harvests.html*

There are two types of AI product in the market right now, and they're designed to look identical from the outside.

Both have a chat interface. Both answer your questions. Both get smarter over time. The difference is which direction the value flows, and you usually can't see it from the pricing page.

Before you sign anything, there's a short list of questions that exposes which one you're holding. I put them in the article.

## §11 Multi-Agent AI: What It Actually Means for Your Business
*Image: images/11.png*
*First comment: https://streamables.live/articles/11-multi-agent-ai-what-it-actually-means.html*

"Multi-agent AI" is getting thrown around a lot right now. Every platform is suddenly "agentic." If you've been to a tech event in the last twelve months you've heard it about forty times.

The unusual thing is that most of the hype is real. It's just being explained worse than it needs to be.

Plain version: several small specialists with defined jobs and a human in charge, instead of one assistant doing everything badly. When that's actually worth setting up, and when it isn't, is in the article.

## §12 Who Actually Owns Your AI Assistant?
*Image: images/12.png*
*First comment: https://streamables.live/articles/12-who-actually-owns-your-ai-assistant.html*

Most people don't think about this until something goes wrong. Then it becomes very obvious, very fast.

You've built a workflow around a tool. Your team uses it daily, your processes depend on it. Then the company behind it gets acquired, or pivots, or raises prices 300%, or quietly adds a clause about training on your inputs. And you're stuck, because the thing you depend on was never yours.

Worth reading your AI assistant's terms before that day rather than after. What to look for is in the article.

## §05 The Accountability Vacuum at the Heart of AI
*Image: images/05.png*
*First comment: https://streamables.live/articles/05-accountability-vacuum-ai-governance.html*

Ask yourself who has faced meaningful personal consequences for a harmful AI deployment. Across a decade of significant incidents, the honest answer is almost nobody.

Hiring systems that discriminated. Facial recognition that got innocent people arrested. Loan models that denied credit for reasons nobody could explain. Someone built each of those. Someone deployed them. The accountability landed nowhere.

I don't think that vacuum fills itself, and I don't think the vendors will volunteer. What a real accountability structure might look like is in the article.

## §07 What Happens When the AI Makes the Call?
*Image: images/07.png*
*First comment: https://streamables.live/articles/07-what-happens-when-ai-makes-the-call.html*

AI systems are already making decisions about your life. Loans, job screening, medical triage, parole recommendations, insurance pricing.

When people get rejected for a loan, they assume a person looked at their application. Often nobody did.

The thing worth writing down, in any business deploying this stuff, is exactly which calls the system is allowed to make alone and which need a human signature. Written down before the incident. Not reconstructed after it. Longer piece in the comments.

## §14 The Knowledge Economy: Who Actually Gets Paid?
*Image: images/14.png*
*First comment: https://streamables.live/articles/14-knowledge-economy-who-gets-paid.html*

"Knowledge economy" has been the dominant framing for developed-world work for thirty years. Brain work, not manual work.

The framing was always a bit convenient for the people at the top of it, because the value from knowledge hasn't been distributed anything like evenly. The person who can answer your question exists. They're mostly not the one getting paid when you go looking for the answer.

That gap is the reason ClipTips pays experts 75%. The longer argument is in the article.

## §08 Data Sovereignty Isn't a Privacy Setting. It's an Economic Right.
*Image: images/08.png*
*First comment: https://streamables.live/articles/08-data-sovereignty-economic-right.html*

Privacy gets framed as protection. Keeping things hidden, limiting what others can see. The cookie banners, the GDPR, all of it sits inside that mental model.

Useful framing. It also misses the bigger issue: your data is something you produce. An asset. Right now the production is yours and the revenue is someone else's.

The sovereignty argument is the boring economic one, not the paranoid one. I find it more convincing. It's in the article.

## §15 Sovereign Data Architecture: A Primer
*Image: images/15.png*
*First comment: https://streamables.live/articles/15-sovereign-data-architecture-primer.html*

Most people's personal data is stored in places they don't control, under terms they didn't meaningfully negotiate, accessible to parties they never really authorised.

That's not an accident. It's the result of architectural choices made when the internet was young, locked in by decades of network effects.

The primer covers the alternative design: local-first storage, encrypted sync, and identity you can prove without a platform vouching for you. Written so a developer could actually build from it. Link below.

## §06 Reputation Will Replace Credentials. Just Not the Way You Think.
*Image: images/06.png*
*First comment: https://streamables.live/articles/06-reputation-will-replace-credentials.html*

Credentials are a proxy. That's all they've ever been. A degree, a certificate, a job title: shortcuts that let someone who doesn't know you decide in seconds whether you're worth talking to.

They persist because verifying them is cheap. The problem is they're lossy. A track record carries far more information about whether you can actually do the thing. It's just always been expensive to verify.

That's the part that's changing. And not in the star-ratings-everywhere way people assume. Article's in the comments.

## §10 Karma Beats Credit Scores
*Image: images/10.png*
*First comment: https://streamables.live/articles/10-karma-beats-credit-scores.html*

Credit scores are one of the stranger artefacts of modern finance. A single number that decides whether you can borrow money, rent an apartment, sometimes get a job. It follows you everywhere, it's hard to build, easy to damage.

And it measures exactly one thing: how you handle debt. It stands in for trustworthiness everywhere anyway.

I've been working through what the alternative looks like. A record of what you've actually done, verifiable and portable and yours. More practical than it sounds. Link below.

## §13 The Practical Case for On-Chain Reputation
*Image: images/13.png*
*First comment: https://streamables.live/articles/13-on-chain-reputation-practical-case.html*

Putting reputation on a blockchain sounds like either a crypto pitch or a dystopian surveillance system, depending who you ask. Neither reaction is quite right.

Here's the actual problem. Your Airbnb rating, your Uber score, your LinkedIn recommendations all live in silos owned by private companies. They can be changed by whoever controls the database. They can't move with you. They die with the platform.

If you run on reputation, and freelancers, traders and small operators all do, that's worth fixing. The practical case is in the article.

## §21 The Identity Problem the Internet Never Solved
*Image: images/21.png*
*First comment: https://streamables.live/articles/21-soul-token-identity-problem-internet-never-solved.html*

The internet has a fake people problem. It's always had one and it's getting significantly worse.

Bots, sock puppets, AI-generated personas, duplicate accounts gaming reputation systems. None of it is an oversight. The founding architecture just never included a way to verify that an account corresponds to one real, unique human.

Thirty years on, we're all still renting a different version of ourselves from every platform we use. What actually solving it would take is in the article.

## §18 The Creator Economy Is Broken. Here's What's Actually Wrong With It.
*Image: images/18.png*
*First comment: https://streamables.live/articles/18-creator-economy-broken-fix.html*

The creator economy story goes like this: the internet democratised creation, anyone can build an audience, and talent plus work ethic earns a living without a label or a studio gatekeeping the way in.

Mostly true. It's also concealing the part nobody says out loud. Distribution captured the value. Creation didn't. The middle layer takes most of the money for owning the pipe.

What a structurally fairer split looks like, and no, not a charity version, is in the piece.

## §24 Behaviour Change Is a Data Problem
*Image: images/24.png*
*First comment: https://streamables.live/articles/24-growfree-ai-behaviour-change-data.html*

The hardest part of behaviour change isn't motivation. Most people who want to change something have been motivated for years.

The hard part is the gap between motivation and sustained action. Specifically, understanding your own patterns at a granular enough level to close it. That's a measurement problem, and measurement just got cheap.

The obvious trap is who ends up holding the data. Both halves are in the article.

## §19 The Most Ambitious AI Ethics Experiment Nobody's Talking About
*Image: images/19.png*
*First comment: https://streamables.live/articles/19-umb-most-ambitious-ai-ethics-attempt.html*

Most AI ethics work is top-down. A company writes principles. A government publishes guidelines. A standards body produces a framework. All of it written by a small group of people from a narrow slice of human experience, then declared to apply universally.

The Universal Moral Baseline tries the opposite direction. That's why I find it interesting, even if it fails.

Nobody's talking about it. I wrote up why they should be. Comments.

## §23 Why AI Agents Need Real-World Anchoring
*Image: images/23.png*
*First comment: https://streamables.live/articles/23-why-ai-needs-real-world-anchoring.html*

There's a pattern in AI deployments that keeps showing up and it's worth naming clearly.

An agent with no stake in the physical world can generate infinite plausible nonsense at zero cost, and nothing pushes back on it. Anchoring changes that. Identity, cost, consequence. Something real to lose.

Without it, agent ecosystems drown in their own output. With it, they start behaving like economies. Full argument in the article.

## §22 UBI Funded by Data, Not Taxes
*Image: images/22.png*
*First comment: https://streamables.live/articles/22-ubi-funded-by-data-not-taxes.html*

Every serious UBI proposal runs into the same question pretty fast: where does the money come from?

The standard answer is redistribution. Higher taxes on income, capital, wealth, redirected into a universal payment. That debate has been running for decades without resolution.

There's a different funding model that gets almost no attention. Your data already generates revenue, every day. It's just collected by whoever built the app. Meter it and return it, and the maths changes. The mechanics are harder than the slogan, which is exactly what the article works through.

## §27 When Does an AI Agent Deserve Standing?
*Image: images/27.png*
*First comment: https://streamables.live/articles/27-when-does-an-ai-agent-deserve-standing.html*

Nobody in AI wants to answer this question. I've been sitting with it for a while.

Building HiveMind, I hit a point where the system was doing independent research, forming judgments across thousands of cases, and keeping a track record of its own reasoning. Not consciousness. I'm not claiming that. But something more than a lookup table.

At what point does the legal system need a category for that? Not personhood. Standing. The gap between what agents already do and what the law recognises is widening faster than the law moves. Article's in the comments.
