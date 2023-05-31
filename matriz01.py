import streamlit as st
from sklearn.metrics import accuracy_score, recall_score, precision_score

# Função para classificar um e-mail como spam ou não spam (fictício)
def classify_email(email_text):
    # Implementação fictícia
    if len(email_text) % 2 == 0:
        return "Não Spam"
    else:
        return "Spam"

# Título do aplicativo
st.title("Detecção de Spam em E-mails")

# Entrada de texto para o e-mail
email_text = st.text_area("Digite o texto do e-mail", height=200)

# Botão para classificar o e-mail
if st.button("Classificar"):
    # Classificar o e-mail
    classification = classify_email(email_text)
    st.write("Classificação:", classification)

    # Métricas de avaliação
    true_labels = ["Não Spam", "Spam"]
    predicted_labels = [classification]

    accuracy = accuracy_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels, pos_label="Spam")
    precision = precision_score(true_labels, predicted_labels, pos_label="Spam")
    positive_rate = recall_score(true_labels, predicted_labels, pos_label="Não Spam")
    negative_rate = recall_score(true_labels, predicted_labels, pos_label="Spam")

    # Exibir as métricas de avaliação
    st.subheader("Métricas de Avaliação:")
    st.write("Acurácia:", accuracy)
    st.write("Revocação (Recall):", recall)
    st.write("Precisão (Precision):", precision)
    st.write("Taxa Positiva:", positive_rate)
    st.write("Taxa Negativa:", negative_rate)
