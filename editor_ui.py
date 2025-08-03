import os
import gradio as gr
from scraper import scrape_page
from ai_writer import ai_writer        # handles rewriting chapters
from ai_reviewer import ai_reviewer    # handles feedback pass

#  Folder where chapter drafts are kept
WORK_DIR = "."

# Finds chapter files dynamically
def fetch_chapter_list():
    files = []
    for f in os.listdir(WORK_DIR):
        if f.startswith("chapter") and f.endswith(".txt") and "_rewritten" not in f and "_review" not in f and "_final" not in f:
            files.append(f.replace(".txt", ""))
    return sorted(files)

#  Load text versions (original / AI rewrite / feedback)
def pull_versions(chapter):
    try:
        with open(f"{chapter}.txt", "r", encoding="utf-8") as f:
            original = f.read()
    except FileNotFoundError:
        original = "Original not found."

    try:
        with open(f"{chapter}_rewritten.txt", "r", encoding="utf-8") as f:
            rewritten = f.read()
    except FileNotFoundError:
        rewritten = " No AI rewrite yet."

    try:
        with open(f"{chapter}_review.txt", "r", encoding="utf-8") as f:
            notes = f.read()
    except FileNotFoundError:
        notes = "No feedback yet."

    return original, rewritten, notes

#  Store the final humanize version
def save_final(chapter, final_text):
    with open(f"{chapter}_final.txt", "w", encoding="utf-8") as f:
        f.write(final_text)
    return f" Final version locked in for {chapter}"

#  Grab new chapter text from a link
def grab_chapter(url, chapter):
    try:
        data = scrape_page(url, f"{chapter}.txt")
        return (f" Pulled '{chapter}' successfully!",
                data, "", "", gr.update(choices=fetch_chapter_list(), value=chapter))
    except Exception as e:
        return (f" Scraping failed: {str(e)}", "", "", "", gr.update(choices=fetch_chapter_list()))

#  Send original text to AI for rewriting
def rewrite_pass(chapter):
    try:
        with open(f"{chapter}.txt", "r", encoding="utf-8") as f:
            raw = f.read()
        rewrite = ai_writer(raw)
        with open(f"{chapter}_rewritten.txt", "w", encoding="utf-8") as f:
            f.write(rewrite)
        return (f" Rewrite ready for '{chapter}'!",
                raw, rewrite, "", gr.update())
    except Exception as e:
        return (f" Rewrite failed: {str(e)}", "", "", "", gr.update())

#  Run AI reviewer on rewritten draft
def review_pass(chapter):
    try:
        with open(f"{chapter}_rewritten.txt", "r", encoding="utf-8") as f:
            rewrite = f.read()
        feedback = ai_reviewer(rewrite)
        with open(f"{chapter}_review.txt", "w", encoding="utf-8") as f:
            f.write(feedback)
        return (f" Review complete for '{chapter}'",
                "", rewrite, feedback, gr.update())
    except Exception as e:
        return (f" Review step failed: {str(e)}", "", "", "", gr.update())


#Gradio Interface

with gr.Blocks() as demo:
    gr.Markdown("##  Book Draft Assistant – Chapter by Chapter")

    with gr.Row():
        url_box = gr.Textbox(label=" URL", placeholder="Drop a Wikisource link")
        chap_name = gr.Textbox(label=" Chapter Tag", placeholder="e.g. chapter1")

    scrape_btn = gr.Button(" Fetch Chapter")
    rewrite_btn = gr.Button(" Rewrite Draft")
    review_btn = gr.Button(" Run Review")

    status = gr.Label()

    chapter_list = fetch_chapter_list()
    chapter_dropdown = gr.Dropdown(
        choices=chapter_list,
        label=" Chapters",
        value=chapter_list[0] if chapter_list else None
    )

    box_original = gr.Textbox(label="Original Text", lines=15)
    box_rewrite = gr.Textbox(label="AI Draft", lines=15)
    box_review = gr.Textbox(label="Reviewer Feedback", lines=10)

    save_btn = gr.Button(" Save Final")

    #  When dropdown changes, load versions
    chapter_dropdown.change(fn=pull_versions,
                            inputs=chapter_dropdown,
                            outputs=[box_original, box_rewrite, box_review])

    # Scrape chapter
    scrape_btn.click(fn=grab_chapter,
                     inputs=[url_box, chap_name],
                     outputs=[status, box_original, box_rewrite, box_review, chapter_dropdown])

    #  Rewrite chapter
    rewrite_btn.click(fn=rewrite_pass,
                      inputs=[chap_name],
                      outputs=[status, box_original, box_rewrite, box_review, chapter_dropdown])

    #  Review chapter
    review_btn.click(fn=review_pass,
                     inputs=[chap_name],
                     outputs=[status, box_original, box_rewrite, box_review, chapter_dropdown])

    # Save final edits
    save_btn.click(fn=save_final,
                   inputs=[chapter_dropdown, box_rewrite],
                   outputs=status)

#  Launch locally
demo.launch(share=True, inbrowser=True, debug=True)
