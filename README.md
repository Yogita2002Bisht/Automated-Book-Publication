📚 Automated Book Publication

This project provides an end-to-end pipeline for automating book chapter processing — from scraping chapters online to rewriting with AI, reviewing, and allowing human edits before finalizing the content.

🚀 What It Does

✅ Scrapes chapters from sources (e.g., Wikisource) using Playwright
✅ Rewrites text in a fresh, modern tone using Gemini AI
✅ Reviews rewritten drafts and provides AI feedback
✅ Lets editors manually edit & save final versions
✅ Provides a Gradio web interface for an interactive workflow

🛠 Tech Stack

Python 3.10+

Playwright → for scraping & screenshots

Gradio → for the user interface

Gemini AI API → for rewriting & review

VS Code → for development

📂 Project Structure

📦 Automated Book Publication
 ┣ 📜 ai_writer.py        # AI rewrite logic
 ┣ 📜 ai_reviewer.py      # AI review logic
 ┣ 📜 scraper.py          # Web scraping with Playwright
 ┣ 📜 editor_ui.py        # Gradio interface for editing
 ┣ 📜 chapter1.txt        # Example chapter
 ┣ 📜 requirements.txt    # Python dependencies
 ┗ 📜 README.md
 
⚙️ Setup

1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/Yogita2002Bisht/automated-book-publication.git
cd automated-book-publication

2️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
playwright install

3️⃣ Set your Gemini API key

Open ai_writer.py & ai_reviewer.py and paste your key:

python
Copy
Edit
genai.configure(api_key="YOUR_API_KEY")

▶️ Usage

Run the UI:

bash
Copy
Edit
python editor_ui.py

A Gradio app will open in your browser. You can:

✅ Enter a chapter URL → Scrape text & screenshot

✅ Click Rewrite with AI → Gemini rewrites the content

✅ Click Review Chapter → AI provides tone & flow suggestions

✅ Make manual edits → Save as final version

🎯 Why I Built This

I wanted to blend automation with creativity — to create a tool that doesn’t just scrape and dump text, but actually helps turn old chapters into fresh, readable versions. Instead of replacing humans, the idea was to assist editors by doing the heavy lifting (scraping, drafting, reviewing) and letting people focus on the final touch.

This project reflects my curiosity about AI-powered writing tools, my interest in human-in-the-loop workflows, and how technology can make publishing smoother without losing the human voice.

📌 Future Enhancements

🔍 RL-based reward system for better rewriting suggestions

🎙 Voice interaction support for editors

📊 Semantic search for chapter navigation

📜 License

MIT License – free to use, modify, and improve.
