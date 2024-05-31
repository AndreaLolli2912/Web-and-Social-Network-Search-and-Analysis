import ollama
import pandas as pd

response=ollama.chat(model="llama3", messages=[
    {"role": "system", "content": "Ciao, come sati?"}
    ])
print(response)


