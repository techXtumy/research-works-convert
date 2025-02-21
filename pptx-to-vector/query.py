import psycopg2
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()

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


query_text = "Comparing with Current Workflow?"

query_vector = MODEL.encode(query_text).tolist()
query_sql = """
SELECT json_content, 1 - (embedding <=> %s::vector) AS similarity
FROM pptx_json_embeddings
ORDER BY similarity DESC
LIMIT 5;
"""

cur.execute(query_sql, (query_vector,))
results = cur.fetchall()

for i, (slide_text, similarity) in enumerate(results):
    print(f"{i+1}. Score: {similarity:.4f}")
    print(f"Slide no::   {slide_text}\n")

cur.close()
conn.close()
