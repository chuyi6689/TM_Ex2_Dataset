import json

def prepare_for_prodigy(filename):
    output_name = filename.replace(".jsonl", "_ready.jsonl")
    with open(filename, "r", encoding="utf-8") as f_in, \
         open(output_name, "w", encoding="utf-8") as f_out:
        for line in f_in:
            data = json.loads(line)
            
            ingredients_str = ", ".join(data.get("Ingredients", []))
            data["text"] = f"RECIPE: {data.get('Name')}\nDESC: {data.get('Description') or ''}\nINGREDIENTS: {ingredients_str}"
            
            f_out.write(json.dumps(data, ensure_ascii=False) + "\n")
    print(f"✅ finished：{output_name}")

prepare_for_prodigy("my_new_50.jsonl")
prepare_for_prodigy("boris_new_50.jsonl")