import fitz

doc = fitz.open("data/ct200_manual.pdf")

page = doc[0]  # Inspect only the first page

blocks = page.get_text("dict")["blocks"]

for block in blocks:

    if "lines" not in block:
        continue

    for line in block["lines"]:

        for span in line["spans"]:

            text = span["text"].strip()

            if not text:
                continue

            print(
                f"Size={span['size']:.1f} | "
                f"Font={span['font']} | "
                f"Text={text}"
            )