import json
import random

input_path = r'D:\26FS\text mining\ex2\recipes.json'
output_path = r'D:\26FS\text mining\ex2\recipes.jsonl'

random.seed(42) 

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

sample_size = min(50, len(data))
sampled_data = random.sample(data, sample_size)

with open(output_path, 'w', encoding='utf-8') as f:
    for recipe in sampled_data:
        full_text = " ".join(recipe.get('Method', []))
        line = {
            "text": full_text, 
            "meta": {"name": recipe.get("Name"), "url": recipe.get("url")}
        }
        f.write(json.dumps(line, ensure_ascii=False) + '\n')

print(f"{sample_size} saved in {output_path}")