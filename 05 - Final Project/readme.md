# Student Essay Sentence Classification


## Files : 
- ``Sentence-classification.ipynb`` - Code to preprocess and train
- ``app.py`` - streamlit code for app deployment using trained model on local
- ``combined_sentence_data.csv`` - preprocessed data used to train in zip format
- ``images`` - deployed app example screenshots

## Other Links :
- [original_data](https://drive.google.com/drive/folders/1gr3Iv71_qnMa4kawt38WNQylsI8_Vex6?usp=sharing)
- [Glove6B.100d](https://nlp.stanford.edu/projects/glove/)
- [Hugging Face Bert Base Cased](https://huggingface.co/bert-base-cased)



### Instructions to run the app :
1) Download our trained [Bert model](https://drive.google.com/drive/folders/1-QPsEg22N4aQ3dpCu0l2BrjFpFVDyFvp?usp=sharing)
2) Download the code and change the path for the model to the downloaded location 
```sh
model = AutoModelForSequenceClassification.from_pretrained(r"C:\Semester 2\NLP\Final Project\Bert_trained_model")
```
3) Go to the app.py location and run ``streamlit run app.py``

## Screenshots from our predictions in streamlit app : 
Sample Prediction - 1

![Streamlit Prediction-1](https://github.com/sivasaikumarreddy/Semantic-Data-Processing-and-Representation-WS2023-Team_Shannon/blob/47c8159bd44ac70e09d674bfe0c30b0d78d454f2/05%20-%20Final%20Project/images/1.png)

Sample Prediction - 2

![Streamlit Prediction -2](https://github.com/sivasaikumarreddy/Semantic-Data-Processing-and-Representation-WS2023-Team_Shannon/blob/47c8159bd44ac70e09d674bfe0c30b0d78d454f2/05%20-%20Final%20Project/images/2.png)

Sample Prediction - 3

 ![Streamlit Prediction -3](https://github.com/sivasaikumarreddy/Semantic-Data-Processing-and-Representation-WS2023-Team_Shannon/blob/47c8159bd44ac70e09d674bfe0c30b0d78d454f2/05%20-%20Final%20Project/images/3.png)

### Contributions :
- Tharun Kumar Korine Palli - 25%
- Siva Sai Kumar Reddy Kachana - 25%
- Lilly Abraham - 25%
- Vishnu Prasad Vijaya Kumar - 25%
