# PowerPoint to Embedding & Query System

## Overview
This repository provides a pipeline to convert PowerPoint slides (`.pptx`) into structured JSON, generate embeddings, and query relevant slides using vector search.

## Folder Structure
```
.
├── README.md              
├── convert_to_embed.py     # Converts JSON to embeddings
├── convert_to_json.py      # Extracts text & metadata from PPTX
├── public/
│   └── test01.pptx         # Sample PowerPoint file
├── query.py                # Queries the embedded slides
├── requirements.txt        # Python dependencies
└── result/
    └── output.json         # JSON output from PowerPoint conversion
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
### Convert PPTX to JSON
Extracts text & metadata from a PowerPoint file.
```bash
python convert_to_json.py
```
**Output:** `result/output.json`

### Convert JSON to Embeddings
Embeds the extracted content into a vector database.
```bash
python convert_to_embed.py
```

### Query Relevant Slides
Finds the most relevant slide based on an input query.
```bash
python query.py
```

## Notes
- Uses **pgvector** for embedding storage
- Model: intfloat/multilingual-e5-base


