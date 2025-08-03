import google.generativeai as genai

# setup Gemini key
genai.configure(api_key="AIzaSyAKEQ5BUtB4ROB8gJw0wDtHC3RBoNibLQU")

model = genai.GenerativeModel("gemini-1.5-flash")

def ai_reviewer(text):
    """Quick review on tone + flow, gives bullet-point feedback"""
    try:
        feedback = model.generate_content(
            f"Go through this chapter rewrite and drop feedback on tone, flow, and readability. "
            f"Keep the notes short and in bullet points:\n\n{text}"
        )
        return feedback.text
    except Exception as e:
        print("Review failed:", e)
        return "review not generated – check API or text"

# standalone test (optional)
if __name__ == "__main__":
    with open("chapter1_rewritten.txt", "r", encoding="utf-8") as f:
        draft_text = f.read()

    notes = ai_reviewer(draft_text)

    with open("chapter1_review.txt", "w", encoding="utf-8") as f:
        f.write(notes)

    print("✅ review notes saved to chapter1_review.txt")
