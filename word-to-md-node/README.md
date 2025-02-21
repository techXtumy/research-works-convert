# Word to Markdown Converter (Node.js)

### Features:
- **Batch conversion** of all `.docx` files in the `public/` directory to Markdown
- **Uses Mammoth.js** to convert Word to HTML
- **Uses Turndown.js** to convert HTML to Markdown
- **Automatically saves Markdown files** in the `result/` directory
- **Integrates markdownlint** to check Markdown quality

## Usage

### Install dependencies
```bash
npm install
```

### Run the script
```bash
node app.js
```

Once executed, all `.docx` files in `public/` will be converted to `.md` files in `result/`.

## Directory Structure
```
.
├── README.md            # Documentation
├── app.js               # Main script
├── package.json         # Dependency information
├── public/              # Folder containing input .docx files
│   ├── Chuan-Hoa.docx
└── result/              # Folder containing output Markdown files
    ├── Chuan-Hoa.md
```
