from sentence_transformers import SentenceTransformer
import psycopg2
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Connect DB
MODEL = SentenceTransformer("intfloat/multilingual-e5-base")
DB_NAME=os.getenv('DB_NAME')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')

try:
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Database connected successfully")
except psycopg2.OperationalError as e:
    print(f"Error connecting details:: {e}")
except Exception as e:
    print(f"Error details:: {e}")
cur = conn.cursor()


with open("./result/output.json", "r", encoding="utf-8") as f:
    ppt_data = json.load(f)
for slide in ppt_data["slides"]:
    json_content = json.dumps(slide)
    embedding = MODEL.encode(json_content).tolist()

    cur.execute(
        """INSERT INTO pptx_json_embeddings (slide_number, json_content, embedding) 
        VALUES (%s, %s, %s)""",
        (slide["slide_number"], json_content, embedding)
    )

conn.commit()
cur.close()
conn.close()
