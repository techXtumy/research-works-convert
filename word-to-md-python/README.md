# Word to Markdown Converter (Python)

### Features:
- **Batch conversion** of all `.docx` files in the `public/` directory to Markdown.
- **Uses Mammoth** to extract text from `.docx` and convert it to HTML.
- **Uses html2text** to convert HTML to Markdown.
- **Utilizes markdown-it-py** with plugins for better Markdown formatting.
- **Automatically saves Markdown files** in the `result/` directory.

## Usage

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the script
```bash
python main.py
```

Once executed, all `.docx` files in `public/` will be converted to `.md` files in `result/`.

## Directory Structure
```
.
├── README.md            
├── main.py              # Main script
├── requirements.txt     # Dependencies
├── public/              # Folder containing input .docx files
│   ├── Chuan-Hoa.docx
└── result/              # Folder containing output Markdown files
    ├── Chuan-Hoa.md
```

- **You can modify the `input_folder` and `output_folder` paths in `main.py` as needed**.
