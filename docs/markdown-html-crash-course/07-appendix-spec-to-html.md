# 07 — Appendix: One Spec, the HTML It Became

Top ka two-minute proof ek casual paragraph se page banaya tha. Yeh appendix uski grown-up version
hai — Concept 1 wali real spec, aur usne jo page banaya. Spec parho. **HTML line-by-line mat parho.**
Lambi HTML browser ke liye hai, aankh ke liye nahi. Neeche ke do blocks ka contrast hi lesson hai.

## Input: ek Markdown spec

```markdown
# Al-Noor Tuition Academy Landing Page Spec

## Goal

A one-page site parents open on their phones to check courses,
timings, fees, and how to reach us.

## Requirements

- Mobile-first; most visitors are on phones
- Course table: course, days, time, monthly fee
- Contact: tappable phone, WhatsApp link, location
- Eid holiday banner at the very top

## Hard constraints

- Single self-contained HTML file, no external fonts or libraries
- Must stay light enough to open on slow mobile data
- Open Graph tags so the WhatsApp/Facebook link preview looks designed

## Out of scope

- Online payments
- Student login
```

## Output: HTML jo yeh bana

Yeh file ~6 KB ki hai, koi extra network request nahi karti, phone par clean parhti hai, aur Open
Graph tags carry karti hai jo uska link preview shape karti hain. Upar ki spec ki har line yahan
present hai. **Ek honest gap:** preview image ke liye `og:image` chahiye jo kisi hosted picture ki
taraf point kare — self-contained file ke paas yeh nahi hai jab tak page kahin publish na ho. Page
ka ghar milne ke baad tag add karo.

Neeche ka block jaan-boojh kar lamba hai — tumhe **scroll past** karna hai. Yehi scroll lesson hai —
reading browser mein hoti hai, yahan nahi.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Al-Noor Tuition Academy</title>

    <!-- Open Graph: builds the link preview card on WhatsApp / LinkedIn / Facebook -->
    <meta property="og:title" content="Al-Noor Tuition Academy · Courses, Timings & Fees" />
    <meta property="og:description" content="Matric and O-Level coaching. See current courses, class timings, monthly fees, and how to reach us." />
    <meta property="og:type" content="website" />

    <style>
      :root { --ink:#27313b; --muted:#5c6b78; --paper:#fbf7f1; --card:#ffffff; --line:#e7ded2; --accent:#c1633a; --accent-soft:#f4e4d8; }
      * { box-sizing: border-box; }
      body { margin:0; background:var(--paper); color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; line-height:1.5; -webkit-text-size-adjust:100%; }
      .wrap { max-width:680px; margin:0 auto; padding:0 18px 48px; }
      .banner { background:var(--accent); color:#fff; text-align:center; font-weight:600; font-size:.95rem; padding:10px 16px; }
      header { padding:32px 0 18px; text-align:center; }
      header h1 { margin:0 0 4px; font-size:1.7rem; letter-spacing:-.01em; }
      header p { margin:0; color:var(--muted); font-size:1rem; }
      h2 { font-size:1.05rem; text-transform:uppercase; letter-spacing:.06em; color:var(--accent); margin:34px 0 12px; }
      table { width:100%; border-collapse:collapse; background:var(--card); border:1px solid var(--line); border-radius:12px; overflow:hidden; }
      th, td { text-align:left; padding:12px 14px; font-size:.95rem; }
      thead th { background:var(--accent-soft); color:var(--ink); font-size:.8rem; text-transform:uppercase; letter-spacing:.05em; }
      tbody tr+tr td { border-top:1px solid var(--line); }
      td.fee { font-weight:600; white-space:nowrap; }
      .contact { display:grid; gap:10px; margin-top:6px; }
      .contact a { display:flex; align-items:center; gap:12px; text-decoration:none; background:var(--card); border:1px solid var(--line); border-radius:12px; padding:14px 16px; color:var(--ink); font-weight:500; }
      footer { margin-top:36px; text-align:center; color:var(--muted); font-size:.85rem; }
    </style>
  </head>
  <body>
    <div class="banner">Eid holidays: the academy is closed 6–9 June. Classes resume 10 June.</div>
    <div class="wrap">
      <header>
        <h1>Al-Noor Tuition Academy</h1>
        <p>Matric &amp; O-Level coaching · Gulberg, Lahore</p>
      </header>
      <h2>Courses &amp; Timings</h2>
      <table>
        <thead><tr><th>Course</th><th>Days</th><th>Time</th><th>Fee / month</th></tr></thead>
        <tbody>
          <tr><td>Matric Mathematics</td><td>Mon–Wed</td><td>4:00–5:30 pm</td><td class="fee">PKR 3,500</td></tr>
          <tr><td>Matric Physics</td><td>Tue–Thu</td><td>5:30–7:00 pm</td><td class="fee">PKR 3,500</td></tr>
          <tr><td>O-Level Chemistry</td><td>Mon–Wed</td><td>6:00–7:30 pm</td><td class="fee">PKR 4,000</td></tr>
          <tr><td>O-Level English</td><td>Fri–Sat</td><td>10:00–11:30 am</td><td class="fee">PKR 4,000</td></tr>
        </tbody>
      </table>
      <h2>Reach Us</h2>
      <div class="contact">
        <a href="tel:+923001234567">Call: 0300 123 4567</a>
        <a href="https://wa.me/923001234567">WhatsApp: 0300 123 4567</a>
        <a href="https://maps.google.com/?q=Gulberg+Lahore">Main Boulevard, Gulberg (view on map)</a>
      </div>
      <footer>Open for admissions · New batches every month</footer>
    </div>
  </body>
</html>
```

*(SVG icons original source se hata diye gaye hain readability ke liye — pattern wahi hai jo book
mein hai; exact icons ke liye live page: [markdown-html-crash-course](https://agentfactory.panaversity.org/docs/markdown-html-crash-course).)*

## Ab course ki teen cheezein khud karo

1. **Phone par kholo.** Poora HTML block Claude.ai mein paste karo, kaho *"turn this exact HTML into
   an artifact, change nothing,"* publish karo, phone par link kholo. Dekho tum ne **parha**, skim
   nahi kiya. (Concept 8)
2. **Prompt se badlo, type karke nahi.** Agent ko kaho: *"Add a fifth course row for FSc Biology,
   Sat-Sun 2 to 3:30 pm, PKR 4,500, and make the holiday banner dismissible."* Ek tag bhi touch nahi
   kiya. (Concept 9)
3. **Real link par publish karo.** Concept 12 ke kisi rung se push karo, WhatsApp mein link share
   karo, preview card render hote dekho. (Concept 11)

Yehi poora crash course hai ek artifact mein. Precise Markdown spec gayi, readable HTML aayi, tumne
prompt se edit kiya, tumne ship kar diya.

---
[⬅ Practice Projects + FAQ](06-practice-projects.md) · [Agla: Test Your Understanding ➡](08-test-your-understanding.md)
