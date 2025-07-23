import os
import fitz  # PyMuPDF
import json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.splitext(os.path.basename(pdf_path))[0]
    headings = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                text = " ".join([span["text"] for span in line["spans"] if span["text"].strip()])
                if not text:
                    continue

                font_size = line["spans"][0]["size"]
                if font_size > 16:
                    level = "H1"
                elif 13 < font_size <= 16:
                    level = "H2"
                elif 11 < font_size <= 13:
                    level = "H3"
                else:
                    continue

                headings.append({
                    "level": level,
                    "text": text,
                    "page": page_num + 1
                })

    return {
        "title": title,
        "outline": headings
    }

def process_all_pdfs(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            result = extract_outline(pdf_path)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.json")
            with open(output_path, "w", encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    process_all_pdfs("/app/input", "/app/output")
