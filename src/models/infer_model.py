from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

INPUT_LENGTH = 1024
OUTPUT_LENGTH = 512


def generate_summary(text: str, model_name: str = "BART", lang: str = "Tiếng Việt",output_length: int = OUTPUT_LENGTH):
    """
    Generate summary of the text using the selected model.
    """

    # define the prompt and model_name based on the languages selected
    if "vi" in lang.lower():
        if "bart" in model_name.lower():
            prompt = f""" Đọc hiểu và tạo 1 tóm tắt tóm lược đoạn văn bản sau với 3, 4 câu theo lời văn tự nhiên:
                ###
                {text}
                """
            model_name = "ntkhoi/bart-vi-news-summarization"
        elif "t5" in model_name.lower():
            prompt = f""" {text} """
            model_name = "ntkhoi/mt5-vi-news-summarization"

    else:
        prompt = f"""Understand and generate abstractive summarize below text with max 3 natural sentences:
            ###
            {text}
            """
        if "bart" in model_name.lower():
            model_name = "facebook/bart-large-cnn"
        elif "t5" in model_name.lower():
            model_name = "siddheshtv/abstractive_summarization"

    # Next, based on the model selected, generate the summary

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    encoding = tokenizer(
        prompt, return_tensors="pt", max_length=INPUT_LENGTH, truncation=True
    )
    input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]

    outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks, max_length=int(1.5*output_length)
    )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    )

    return summary
