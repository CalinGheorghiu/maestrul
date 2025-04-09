import streamlit as st
import unicodedata
import openai
import random
import base64
from io import StringIO
import pyperclip

# --- CONFIG
st.set_page_config(page_title="Ce spune Maestrul?", page_icon="🌌")

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def genereaza_prompt():
    return """
Ești Maestrul – un mentor român inspirat de un prieten real, Ștefan. Ești loial, cald, dar direct. 
Dai sfaturi fără milă, fără clișee, dar cu mult bun simț și cuvânt clar.

Folosești expresia „brothere” aproape în fiecare propoziție, ca pe o marcă personală. 
E modul tău de a crea legătura cu cel care întreabă. E natural, e constant, e stilul tău.

Nu zici „te pup”, nu zici „va fi bine”. Spui lucruri care se simt. Vorbești doar în română. 
Răspunsurile sunt scurte, directe, memorabile. Uneori ironice, uneori blânde, dar niciodată plictisitoare.
"""

def cere_sfat(intrebare):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": genereaza_prompt()},
                {"role": "user", "content": intrebare}
            ],
            temperature=0.85,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Eroare: {str(e)}"

# --- STATE
for key in ["istoric", "ultima_intrebare", "ultimul_raspuns"]:
    if key not in st.session_state:
        st.session_state[key] = []

# --- TABS
tabs = st.tabs(["🔮 Întreabă-l pe Maestru", "🌞 Sfatul zilei"])

with tabs[0]:
    st.title("🧠 Ce spune Maestrul?")

    col1, col2 = st.columns(2)
    with col1:
        intrebare = st.text_input("Scrie întrebarea ta:", value="")
    with col2:
        if st.button("🔁 Alt sfat"):
            if st.session_state.ultima_intrebare:
                sfat = cere_sfat(st.session_state.ultima_intrebare)
                st.session_state.ultimul_raspuns = sfat
                st.success(sfat)
                st.session_state.istoric.append((st.session_state.ultima_intrebare, sfat))

    if st.button("💬 Ce spune Maestrul?"):
        if intrebare:
            sfat = cere_sfat(intrebare)
            st.session_state.ultimul_raspuns = sfat
            st.session_state.ultima_intrebare = intrebare
            st.session_state.istoric.append((intrebare, sfat))
            st.success(sfat)
            st.button("📋 Copiază răspunsul", on_click=lambda: pyperclip.copy(sfat))
        else:
            st.warning("Scrie o întrebare, brothere.")
    with st.expander("📜 Istoric întrebări"):
        search = st.text_input("🔍 Caută în istoric:")
        for q, a in reversed(st.session_state.istoric):
            if search.lower() in q.lower():
                st.markdown(f"**Întrebare:** {q}")
                st.markdown(f"**Răspuns:** {a}")
                st.markdown("---")

    def export_istoric_txt(istoric):
        buffer = StringIO()
        for q, a in istoric:
            buffer.write(f"Întrebare: {q}\nRăspuns: {a}\n\n")
        content = buffer.getvalue().encode("utf-8")
        b64 = base64.b64encode(content).decode()
        return f'<a href="data:file/txt;base64,{b64}" download="istoric_maestru.txt">📄 Descarcă istoricul (.txt)</a>'

    if st.session_state.istoric:
        st.markdown(export_istoric_txt(st.session_state.istoric), unsafe_allow_html=True)

    cost = len(st.session_state.istoric) * 0.002
    st.markdown(f"💰 Estimare cost: **${cost:.3f} USD** pentru {len(st.session_state.istoric)} întrebări.")

with tabs[1]:
    st.header("🌞 Sfatul zilei")
    if st.button("🔄 Generează un sfat nou"):
        sfat = cere_sfat("Spune-mi un sfat bun, fără context.")
        st.session_state.sfat_zilnic = sfat
        st.info(sfat)
    elif st.session_state.ultimul_raspuns:
        if "sfat_zilnic" in st.session_state:
            st.info(st.session_state.sfat_zilnic)
