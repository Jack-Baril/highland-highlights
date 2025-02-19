from docx import Document

from theme.styles import Styles


class DocxHtmlConverter:
    @staticmethod
    def parse_docx(docx_path):
        docx = Document(docx_path)
        paragraphs = [
            DocxHtmlConverter.format_paragraph(paragraph)
            for paragraph in docx.paragraphs
            if paragraph.text.strip()
        ]
        return f"<html><body>{''.join(paragraphs)}</body></html>"

    @staticmethod
    def format_paragraph(paragraph):
        return f"<p>{' '.join([DocxHtmlConverter.format_run(run) for run in paragraph.runs if run.text.strip()])}</p>"

    @staticmethod
    def format_run(run):
        tags = []
        if run.italic:
            tags.append("<i>")
        if run.underline:
            tags.append("<u>")
        color = DocxHtmlConverter.get_text_color(run)
        formatted_text = f"<span{color}>{run.text}</span>"
        return f"{''.join(tags)}{formatted_text}{''.join(reversed(tags))}"

    @staticmethod
    def get_text_color(run):
        if run.font.color and run.font.color.rgb:
            color = f"#{run.font.color.rgb}"
            if color == Styles.DOCX_HEADER_COLOR:
                return f" style='color: {Styles.TEXT_HEADER_COLOR}'"
        return ""
