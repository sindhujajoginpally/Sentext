import streamlit as st 
import os
# NLP Pkgs
from textblob import TextBlob 
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from PIL import Image
image = Image.open('s.png')
image2=Image.open('sentext.png')

# Function to Analyse Tokens and Lemma
@st.cache
def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)
    # tokens = [ token.text for token in docx]
    allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
    return allData

def main():
   

#Create two columns with different width
    col1, col2 = st.columns( [0.3, 0.7])
    with col2:               # To display the header text using css style
        st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
        st.title("Sentimental Analysis from Text Feedback")
    with col1:               # To display brand logo
        st.image(image2,  width=150)
    
    st.markdown("""<br><hr style="height:10px;border:none;color:#fff;background-color:#fff;" /> <br>""", unsafe_allow_html=True)
    st.subheader("Extract sentiments from customer feedbacks, product reviews with a click of a button")
    st.markdown("""""")
    st.image(image)
    st.markdown("""
        #### Description
This is a Sentimental Analysis App.
+ Sentimental analysis is a part of the Natural Language Processing (NLP) techniques that consists in extracting emotions related to some raw texts. 
+ The basic task involved in sentiment analysis is to determine the sentiment polarity expressed in a textual content.


        """)
     


    st.markdown("""<hr style="height:10px;border:none;color:#fff;background-color:#fff;" /> """, unsafe_allow_html=True)
        # Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize Your Text")
        message = st.text_area("Enter Text","Type Here ..")
        if st.button("Analyze"):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)
    
    senti=""
    output=""
    # Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Analyse Your Text")
        if st.checkbox("Single Review"):
            message = st.text_area("Enter Text","Type Here ..")
            if st.button("Analyze"):
                    blob = TextBlob(message)
                    result_sentiment = blob.polarity
                    if result_sentiment>0:
                           senti="Positive"
                    elif result_sentiment<0:
                            senti="Negative"   
                    else: 
                            senti="Neutral"
                    output="Sentiment =  "+senti+",\t Polarity = "+str(result_sentiment)
                    st.write(output)
        if st.checkbox("Multiple Reviews"):
            msg = st.text_area("Enter Text","Type Here ..")
            #entences = sent_tokenize(msg)
            #nlp = spacy.load('en_core_web_sm')
            #doc = nlp(msg)
            list = []
            list = msg.split('.')
            i=0
            result_sentiment=[]
            op=[]
            num=[]
            senti=""
            if st.button("Analyze"):
                    while i<len(list)-1:
                        blob = TextBlob(list[i])
                        result_sentiment.append(list[i])
                        result_sentiment[i]= blob.polarity
                        if result_sentiment[i]>0:
                                senti="Positive"
                        elif result_sentiment[i]<0:
                                senti="Negative"   
                        else: 
                                senti="Neutral"
                        
                        op.append(list[i]+"\t => Sentiment =  "+senti+"\t Polarity = "+str(result_sentiment[i]))
                        i=i+1
            st.write(op)

""" 


    
    
"""
if __name__ == '__main__':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    main()