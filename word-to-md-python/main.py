import mammoth
import html2text  
import os
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin


input_folder = "./public"
output_folder = "./result"
os.makedirs(output_folder, exist_ok=True)

md = (
    MarkdownIt('commonmark' ,{'breaks':True,'html':True})
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .enable('table')
)

for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name.rsplit(".", 1)[0] + ".md") 

    with open(input_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value

    markdown = html2text.html2text(html)
    markdown_final = md.render(markdown)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_final)