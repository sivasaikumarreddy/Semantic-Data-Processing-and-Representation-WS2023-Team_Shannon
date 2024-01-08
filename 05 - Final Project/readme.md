**# Student Essay Sentence Classification


## Files : 
- ``Sentence-classification.ipynb`` - Code to preprocess and train
- ``app.py`` - streamlit code for app deployment using trained model on local
- ``images`` - deployed app example screenshots

### instructions to run the app :
1) Download our trained [Bert model](https://drive.google.com/drive/folders/1swRG0hiOsfbwLzCH_B7-x4XYWNL6KvdU?usp=sharing)
2) Download the code and change the path for the model to the downloaded location 
```sh
model = AutoModelForSequenceClassification.from_pretrained(r"C:\Semester 2\NLP\Final Project\Bert_trained_model")
```
3) Go to the app.py location and run ``streamlit run app.py``

## Screenshots from our predictions in streamlit app : 
