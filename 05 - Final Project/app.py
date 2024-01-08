import streamlit as st
import base64
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch


label_names = ['Lead', 'Position', 'Evidence', 'Claim', 'Concluding Statement', 'Counterclaim', 'Rebuttal', 'No Class']

def get_image_as_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


background_image_path = r"C:\Semester 2\NLP\Final Project\student.jpg"
background_image_base64 = get_image_as_base64(background_image_path)

@st.cache_data 
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(r"C:\Semester 2\NLP\Final Project\Bert_trained_model")
    tokenizer = AutoTokenizer.from_pretrained(r"C:\Semester 2\NLP\Final Project\Bert_trained_model")
    return model, tokenizer

model, tokenizer = load_model()

def classify_text(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding='max_length', max_length=326)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return probs

st.sidebar.title("Students writing Sentence Classification")
st.sidebar.markdown("""
This app takes in the sentence from the student essay and will give the probability of it from these defined classes:
<br>1. Lead
<br>2. Position
<br>3. Evidence
<br>4. Claim
<br>5. Concluding Statement
<br>6. Counterclaim
<br>7. Rebuttal
<br>8. No Class
""", unsafe_allow_html=True)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image_base64}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("data:image/jpg;base64,{background_image_base64}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .stApp {
        /* Adjust the background image and other styles as needed */
    }
    .title {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<h1 class="title">Sentence Classification with BERT</h1>', unsafe_allow_html=True)
user_input = st.text_area('Enter text to classify:', '')

st.markdown("""
    <style>
    table {
        color: white;
        font-weight: bold;
        margin-left: 30%;
        margin-right: auto;
        display: block;
    }
    th {
        color: red;
    }
    td {
        color: white;
        font-weight: bold;
    }
    .highlight {
        color: lime;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

if st.button('Classify'):
    if user_input:
        probabilities = classify_text(user_input)
        probabilities = probabilities.numpy()[0]

        # Rounding  the probabilities 
        probabilities_rounded = [round(prob, 4) for prob in probabilities]
        max_prob = max(probabilities_rounded)
        max_prob_index = probabilities_rounded.index(max_prob)

        html_content = "<table style='border-collapse: collapse;'>"
        html_content += "<tr><th>Label</th><th>Probability</th></tr>"

        for i, (label, prob) in enumerate(zip(label_names, probabilities_rounded)):
            highlight_class = "highlight" if i == max_prob_index else ""
            html_content += f"<tr><td>{label}</td><td class='{highlight_class}'>{prob:.2f}</td></tr>"

        html_content += "</table>"

        st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.write('Please enter some text to classify.')