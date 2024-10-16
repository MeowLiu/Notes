import os
from markdown import markdown
from markdown import markdown
import pdfkit
import sys


input = "硅基生物学\《线性代数》\第一章：矩阵与方程组.md"
output = "./第一章：矩阵与方程组.pdf"

with open(input, encoding="utf-8") as f:
    md_content = f.read()

html_content = markdown(md_content, output_format="html")
pdfkit.from_string(input=md_content, output_path=output)
print(md_content)
print(html_content)
