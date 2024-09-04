from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

INPUT_LENGTH = 512
OUTPUT_LENGTH = 256


def generate_summary(text: str,
                     model_name: str = "ntkhoi/bart-vi-news-summarization",
                     lang: str = "Tiếng Việt"):
    """
    Generate summary of the text using the selected model.
    """

    # First, define the prompt based on the languages selected
    if "vi" in lang.lower():
        prompt = f""" Đọc hiểu và tạo 1 tóm tắt tóm lược đoạn văn bản sau với 3, 4 câu theo lời văn tự nhiên:
            ###
            {text}
            """
    else:
        prompt = f"""Understand and generate abstractive summarize below text with max 3 natural senteneces:
            ###
            {text}
            """

    # Next, based on the model selected, generate the summary

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    encoding = tokenizer(prompt, return_tensors="pt", max_length=INPUT_LENGTH, truncation=True)
    input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]

    outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_masks,
        max_length=OUTPUT_LENGTH
    )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    )

    return summary
