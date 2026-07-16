import fitz

from app.models.parser_node import Node
from app.services.tree_builder import TreeBuilder


class PDFParser:

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def parse(self):

        doc = fitz.open(self.pdf_path)

        nodes = []
        current_node = None

        for page in doc:

            blocks = page.get_text("dict")["blocks"]

            for block in blocks:

                if "lines" not in block:
                    continue

                for line in block["lines"]:

                    for span in line["spans"]:

                        text = span["text"].strip()

                        if not text:
                            continue

                        size = span["size"]

                        # Ignore document title
                        if size >= 20:
                            continue

                        # Main Heading
                        elif 16 <= size <= 17:

                            current_node = Node(text, 1)
                            nodes.append(current_node)

                        # Sub Heading
                        elif 12 <= size <= 13.5:

                            current_node = Node(text, 2)
                            nodes.append(current_node)

                        # Body Text
                        elif 10.5 <= size <= 11.5:

                            if current_node:
                                current_node.body += text + " "

        return nodes


if __name__ == "__main__":

    parser = PDFParser("data/ct200_manual.pdf")

    nodes = parser.parse()

    builder = TreeBuilder()

    builder.build(nodes)

    print(f"\nTotal Nodes: {len(nodes)}\n")

    for node in nodes:

        print("=" * 60)
        print(node.heading)

        if node.parent:
            print(f"Parent   : {node.parent.heading}")
        else:
            print("Parent   : None")

        print(f"Children : {len(node.children)}")
        print(f"Body     : {node.body[:150]}")