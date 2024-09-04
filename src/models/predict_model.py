from transformers import AutoTokenizer, AutoModelForSeq2SeqLM



INPUT_LENGTH = 512
OUTPUT_LENGTH = 256



def t5_summary(text="", 
               model_name="ntkhoi/mt5-vi-news-summarization", 
               lang="vi"): 
    
    # if language selected is vietnamese
    if "vi" in lang.lower():
        model_name = "ntkhoi/mt5-vi-news-summarization" 
        prompt = f""" Đọc hiểu và tạo 1 tóm tắt tóm lược đoạn văn bản sau với 3, 4 câu theo lời văn tự nhiên:
        ###
        {text} 
        """

    # if language selected is english
    else :
        model_name = "siddheshtv/abstractive_summarization"
        prompt = f"""Understand and generate abstractive summarize below text with max 3 natural senteneces:
        ###
        {text} 
        """


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



def bart_summary(text="", 
               model_name="ntkhoi/bart-vi-news-summarization", 
               lang="vi"): 
    
    # if language selected is vietnamese
    if "vi" in lang.lower():
        model_name = "ntkhoi/bart-vi-news-summarization" 
        prompt = f""" Đọc hiểu và tạo 1 tóm tắt tóm lược đoạn văn bản sau với 3, 4 câu theo lời văn tự nhiên:
        ###
        {text} 
        """

    # if language selected is english
    else :
        model_name = "facebook/bart-large-cnn"
        prompt = f"""Understand and generate abstractive summarize below text with max 3 natural senteneces:
        ###
        {text} 
        """


    tokenizer = AutoTokenizer.from_pretrained(model_name)  
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    encoding = tokenizer(prompt, return_tensors="pt", max_length=INPUT_LENGTH,truncation=True)
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
