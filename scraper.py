from playwright.sync_api import sync_playwright

def scrape_page(url, save_path="chapter1.txt"):
    """
    Simple scraper that:
    - Opens a page with Playwright
    - Pulls out the main text
    - Saves the text to a .txt file
    - Takes a screenshot for reference
    """

    print(f"[INFO] Loading page: {url}")

    with sync_playwright() as p:
        #  Chromium in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Go to the link
        page.goto(url)

        # Wait until the page stops loading 
        page.wait_for_load_state("networkidle")

        #  Grab the content
        try:
            content = page.inner_text(".mw-parser-output")  # works for Wikisource
        except Exception as e:
            print(f"[WARN] Could not grab content: {e}")
            content = ""

        # Save the text to file
        if content:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[OK] Text written to {save_path}")
        else:
            print("[WARN] No content found to save.")

        #  Save a screenshot next to the text file
        screenshot_path = save_path.replace(".txt", ".png")
        page.screenshot(path=screenshot_path)
        print(f"[OK] Screenshot saved at {screenshot_path}")

        #  Clean exit
        browser.close()

    return content


#  Test run when file is called directly
if __name__ == "__main__":
    test_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    scrape_page(test_url, "chapter1.txt")
