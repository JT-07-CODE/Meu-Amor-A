import streamlit as st
import time

st.title("Mensagem Especial 💖")

mensagens = [
    "Oi minha gostosa 💖",
    "Só pra te lembrar hoje e sempre...",
    "Que desde que te conheci, minha vida mudou completamente",
    "Você me faz sorrir, sonhar, querer viver a vida inteira do seu lado..",
    "Então, eu queria saber de você",
    "Se vc topa dividir as loucuras da vida comigo....pra vida toda....",
    "💍 Você quer se casar comigo? Rs 💍"
]

placeholder = st.empty()
for msg in mensagens:
    placeholder.text(msg)
    time.sleep(6)

st.subheader("Toque a música 🎵")
st.audio("https://www.youtube.com/watch?v=uNuMH2i6wdI&list=RDuNuMH2i6wdI&start_radio=1", format="audio/mp3")
