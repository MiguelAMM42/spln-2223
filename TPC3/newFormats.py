from jinja2 import Template
import json

def generate_html(data):
    html = ""
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                html += f"<h2>{key}</h2>"
                html += generate_html(value)
            elif isinstance(value, list):
                html += f"<h3>{key}</h3>"
                for item in value:
                    html += generate_html(item)
            else:
                html += f"<p><b>{key}:</b> {value}</p>"
    else:
        html += f"<p>{data}</p>"
    return html

def generate_markdown(data):
    markdown = ""
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                markdown += f"\n## {key}\n"
                markdown += generate_markdown(value)
            elif isinstance(value, list):
                markdown += f"\n### {key}\n"
                for item in value:
                    markdown += generate_markdown(item)
            else:
                markdown += f"\n**{key}:** {value}\n"
    else:
        markdown += f"\n{data}\n"
    return markdown

def generate_latex(data):
    latex = ""
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                latex += f"\\section{{{key}}}\n"
                latex += generate_latex(value)
            elif isinstance(value, list):
                latex += f"\\subsection{{{key}}}\n"
                for item in value:
                    latex += generate_latex(item)
            else:
                latex += f"\\textbf{{{key}:}} {value}\n"
    else:
        latex += f"\n{data}\n"
    return latex



with open('data/medicina_treated.json', 'r') as f:
    data = json.load(f)

html = generate_html(data)
with open('out/medicina_treated.html', 'w', encoding='utf-8') as f:
    f.write(html)

md = generate_markdown(data)
with open('out/medicina_treated.md', 'w', encoding='utf-8') as f:
    f.write(md)
latex = generate_latex(data)

with open('out/medicina_treated.tex', 'w', encoding='utf-8') as f:
    f.write(latex)