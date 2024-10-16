import os
from markdown import markdown
import pdfkit
import sys


def convert_md_to_pdf(md_file, output_dir):
    # 读取Markdown文件内容
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    # 将Markdown转换为HTML
    html_content = markdown(md_content)

    # 设置PDF输出文件名
    pdf_file = os.path.join(
        output_dir, os.path.basename(md_file).replace(".md", ".pdf")
    )

    # 使用pdfkit将HTML转换为PDF
    pdfkit.from_string(html_content, pdf_file)


def process_directory(directory):
    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(root, file)
                print(f"Converting {md_file_path} to PDF...")
                convert_md_to_pdf(md_file_path, root)


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_md_to_pdf.py <directory>")
        sys.exit(1)

    # 获取要处理的目录
    target_directory = sys.argv[1]

    # 处理指定目录
    process_directory(target_directory)


if __name__ == "__main__":
    main()
