import torch
import docx
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

from transformers import pipeline



#model_path = ("../Models/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english"
 #             "/.no_exist/714eb0fa89d2f80546fda750413ed43d93601a13")


#analyzer = pipeline("text-classification", model=model_path)

# print(analyzer(["This production is good", "This product was quite expensive"]))

device = 0 if torch.cuda.is_available() else -1

analyzer = pipeline("text-classification", model="distilbert/distilbert-base-"
                                             "uncased-finetuned-sst-2-english", device=device)


def sentiment_analyzer(review):
    sentiment = analyzer(review)
    return sentiment[0]['label']

def sentiment_bar_chart(df):
    sentiment_counts = df['Sentiment'].value_counts()

    # Create a bar chart
    fig, ax = plt.subplots()
    sentiment_counts.plot(kind='pie', ax=ax, autopct='%1.1f%%', color=['green', 'red'])
    ax.set_title('Review Sentiment Counts')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    # ax.set_xticklabels(['Positive', 'Negative'], rotation=0)

    # Return the figure object
    return fig


def read_reviews_and_analyze_sentiment(file_object):
    # Load the word file into a DataFrame
    doc = docx.Document(file_object)

    # Extract the reviews from the Word file
    reviews = [p.text for p in doc.paragraphs]

    # Create a pandas DataFrame
    df = pd.DataFrame({'Reviews': reviews})

    # Apply the sentiment analyzer to each review
    df['Sentiment'] = df['Reviews'].apply(sentiment_analyzer)

    chart_object = sentiment_bar_chart(df)
    return df, chart_object

# result = read_reviews_and_analyze_sentiment("../Files/Prod-review.xlsx")
# print(result)
# Example usage:
# df = read_reviews_and_analyze_sentiment('path_to_your_excel_file.xlsx')
# print(df)


demo = gr.Interface(fn=read_reviews_and_analyze_sentiment,
                    inputs=[gr.File(file_types=["docs"], label="Upload your review comment file")],
                    outputs=[gr.Dataframe(label="Sentiments"), gr.Plot(label="Analysis")],
                    title="Sentiment Analyzer",
                    description="THIS APPLICATION WILL BE USED TO ANALYZE THE SENTIMENT BASED ON FILE UPLAODED.")
demo.launch()

