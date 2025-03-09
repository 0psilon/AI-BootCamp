from transformers import pipeline


model_path = 'tabularisai/multilingual-sentiment-analysis'
device = 'cpu'

sentiment_pipeline = pipeline(
        'sentiment-analysis',
        model=model_path,
        tokenizer=model_path,
        device=device
    )
