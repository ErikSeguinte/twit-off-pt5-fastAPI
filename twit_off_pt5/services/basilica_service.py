import basilica, os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('basilica_key')

import basilica

with basilica.Connection(key) as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])
    print(list(embeddings))  # [[0.8556405305862427, ...], ...]
