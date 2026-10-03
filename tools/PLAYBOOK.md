# GMP weekly post playbook

For the automatic weekly run that builds and schedules Global Math Prep (GMP) social posts.

## Accounts
- Metricool brand (blogId) **7096377**, timezone **America/Halifax**. It is linked to Instagram @globalmathprep and to the Facebook page.
- Posting time: **9:00 AM Halifax** (20:00 Ulaanbaatar).
- Media must be public URLs. Push the files to this repo (`jargalmaaamgalan-art/desktop-tutorial`). Then use `https://raw.githubusercontent.com/jargalmaaamgalan-art/desktop-tutorial/<commit-sha>/<path>`. Always use the commit SHA, never the branch name, so the links can't be cached.

## How every post is published
- **Instagram:** a carousel. Slide 1 is the **PNG** (a still cover, so the grid never shows a black tile). Slides 2 to N are the **MP4** videos. Set `instagramData.type = "POST"`.
- **Facebook:** a separate post, all slides as **PNG**. Facebook rejects carousels made of several videos (error 500).
- Both go out at the same date and time, with the same caption.
- First comment, Facebook post: NO website links. Meta limits this page's monthly external links ("out of monthly active links"); only Meta links (wa.me, m.me) are allowed. Use:
  `📩 Үнэгүй SAT тест болон бүртгэлийн линкийг авах бол доор "SAT" гэж бичээрэй, Messenger-ээр илгээнэ.` / `💬 WhatsApp: https://wa.me/14288801826` (two lines). The "SAT" comment automation sends the website links by private message.
- First comment, Instagram post (Instagram never makes links in comments clickable):
  `✅ Үнэгүй SAT тест, 📝 бүртгэл: profile дээрх линкээр орно уу 👆` / `💬 WhatsApp: +1 428 880 1826` (two lines)

## Building slides
- The generators are in `tools/v2`. `gen30.py` is the model for a short lesson post: cover, idea, Bluebook question, answer, end page. Copy it to a new `genNN.py`, change the content, then run `python3 genNN.py --video`. Run it once without `--video` first to check for OVERFLOW.
- Emoji: use **only one** animated emoji, on the cover.
- Size 1080×1350. The header uses the real GMP logo strip, never a redrawn logo.
- Each post gets **its own colour**. Never repeat the colour of a recent post.
- Every post is built like a book: a cover with a hook, then content, then an end page with the QR code and class times.

## Reels
- GMP brand label (logo, thin divider, "GLOBAL MATH PREP" in spaced capitals, gold "КАНАДААС" + SVG maple leaf, dark translucent pill) sits in the **top-left corner** (left 36px, top 150px), below Instagram's top bar, above the white title boxes.

- Reel music: Instagram does NOT allow adding music after a Reel is posted (owner tested Oct 2, 2026). Always schedule Reels with autoPublish FALSE and no audioConfiguration; the owner publishes from the Metricool app notification and adds trending music before sharing. Set a reminder 5 minutes before each Reel.

- Reel covers: always a dedicated topic cover (orange label + big topic title, e.g. "SAT-д бүртгүүлэх 7 алхам"), readable in the 4:5 grid crop; never a mid-video hook frame.
- Reel style approved Oct 2, 2026 (credits Reel): full-screen real footage with hard cuts every 3–4 s; big bold Montserrat captions popping in 1–2 lines at a time, key word in orange (#ffb43a); short orange label pill per scene; every term explained in a few words (e.g. "SL (энгийн түвшин)"); hook in the first 2 s; under 30 s; teen tone with "чи"; no emojis on screen. Builder: scratchpad reel/cap.py.

## Content rules (from the owner)
- Take questions and examples **verbatim** from her own lesson modules in the private repo `jargalmaaamgalan-art/GMP-REPO`, for example `desktop-masters/2-KEEP-ON-DESKTOP/sat-writing-*.html`. Each module has a `const M = [...]` with stems, options, answers and explanations. Never invent SAT questions.
- Never call a question a "real SAT", "жинхэнэ" or "College Board" question unless the source says so. Use "дасгал" instead.
- Split topics so each post has one idea and 5 or 6 slides.
- Write natural, teen-friendly Mongolian. Watch vowel harmony on Latin words: `Zoom-ээр`, `D-тэй`, `Meanwhile-ын`. Use no em-dashes.
- Class times: SAT English **Мя · Пү · Бя**, Math **Да · Лх · Ба**, both **20:00–21:20** UB time. Groups are **2–6**.
- Captions: 2 or 3 short lines, 1 or 2 emojis, then the line `Бүртгэл, хуваарь авах бол "SAT" гэж коммент бичээрэй 👇` (this triggers the owner's Meta comment→message automation; use "IGCSE" for IGCSE posts), then `#SAT #DigitalSAT #SATEnglish #GlobalMathPrep` (use `#SATMath` for Math).
- Don't advertise student scores.

## Audit before scheduling (required)
Ask a separate agent to look at every PNG and check:
- logic and answers;
- natural Mongolian;
- visibility (nothing cut off or hidden);
- times and numbers;
- claims that could mislead.

Fix everything it finds before scheduling.

## Report
Send the owner a short report:
- a table of what was scheduled (date, title, slide count);
- what the audit changed;
- anything that needs her decision.

- Reels: schedule for INSTAGRAM ONLY in Metricool (no Facebook provider). Facebook Reels ignore autoPublish false and post automatically with no music (owner saw this Oct 3, 2026). When posting from the Instagram app, the owner adds music and turns on "Share to Facebook" so both get the same music.
