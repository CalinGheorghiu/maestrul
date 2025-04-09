
# 🧠 Ce spune Maestrul?

Aplicație realizată cu Streamlit care îți oferă sfaturi scurte, sincere și memorabile – în stilul prietenului tău Ștefan.  
Fiecare întrebare primește un răspuns generat de un model AI antrenat cu un prompt personalizat în limba română.

---

## 🔧 Funcționalități

- 💬 Pune întrebări și primește sfaturi în stil „brothere”
- 🔁 Cere „Alt sfat” pentru aceeași întrebare
- 🌞 Primește „Sfatul zilei” generat automat
- 📋 Copiază rapid răspunsul
- 🔍 Caută în istoricul întrebărilor
- ⭐ Adaugă răspunsuri favorite
- ✏️ Editează ultima întrebare
- 📄 Descarcă istoricul în format `.txt`
- 💰 Estimare cost pe întrebări (cu API OpenAI)

---

## 🗝️ Setup local

1. Instalează dependențele:
   ```bash
   pip install streamlit openai pyperclip
   ```

2. Creează fișierul `.streamlit/secrets.toml` cu:
   ```toml
   OPENAI_API_KEY = "sk-..."
   ```

3. Rulează aplicația:
   ```bash
   streamlit run maestrul_chatgpt_final_v1_5.py
   ```

---

## ℹ️ Costuri

Aplicația folosește OpenAI GPT-3.5.  
Cost estimativ: **~0.002 USD per întrebare**.
