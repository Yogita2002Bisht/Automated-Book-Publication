import google.generativeai as genai

# setup Gemini API
genai.configure(api_key="AIzaSyAKEQ5BUtB4ROB8gJw0wDtHC3RBoNibLQU")

# using Gemini's flash model for faster rewrites
model = genai.GenerativeModel("gemini-1.5-flash")

def rewrite_text(text):
    """rewrite chapter in a more natural + modern style"""
    try:
        reply = model.generate_content(
            f"Take this chapter and rewrite it in a smoother, modern tone. Keep it clear and engaging:\n\n{text}"
        )
        return reply.text
    except Exception as e:
        print(" rewrite failed:", e)
        return text  # fallback to original if something goes wrong

# read the original chapter
with open("chapter1.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

#  generate a rewrite
new_version = rewrite_text(original_text)

#  save the rewritten chapter
with open("chapter1_rewritten.txt", "w", encoding="utf-8") as f:
    f.write(new_version)

print(" chapter rewrite saved with Gemini!")

