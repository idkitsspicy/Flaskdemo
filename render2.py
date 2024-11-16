from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("./models/bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("./models/bert-base-uncased")
