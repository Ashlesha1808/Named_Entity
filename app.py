import streamlit as st
import spacy
from spacy import displacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Set Streamlit page settings
st.set_page_config(page_title="NER App", layout="centered")

# App Title
st.markdown("<h1 style='color:#2c3e50;'>🧠 Named Entity Recognition (NER)</h1>", unsafe_allow_html=True)
st.markdown("Enter a paragraph of text. This app will detect **names**, **locations**, and **organizations**, including Indian names written in English!")

# Text input
text_input = st.text_area("✏️ Enter your text below:", 
                          "Narendra Modi visited Bengaluru and met ISRO scientists at Infosys HQ.")

# If the text area has text and button is clicked
if st.button("🚀 Extract Entities") and text_input.strip() != "":
    doc = nlp(text_input)

    # Dictionary to collect entities
    entity_dict = {"PERSON": [], "GPE": [], "ORG": []}

    # Extract and group entities
    for ent in doc.ents:
        if ent.label_ in entity_dict:
            entity_dict[ent.label_].append(ent.text)

    # Show results
    st.markdown("## 🧾 Extracted Entities")

    if entity_dict["PERSON"]:
        st.markdown("### 🧑 People:")
        for person in set(entity_dict["PERSON"]):
            st.markdown(f"- {person}")

    if entity_dict["GPE"]:
        st.markdown("### 🌍 Locations:")
        for place in set(entity_dict["GPE"]):
            st.markdown(f"- {place}")

    if entity_dict["ORG"]:
        st.markdown("### 🏢 Organizations:")
        for org in set(entity_dict["ORG"]):
            st.markdown(f"- {org}")

    if not any([entity_dict["PERSON"], entity_dict["GPE"], entity_dict["ORG"]]):
        st.warning("No entities found in the text.")

    # Bonus: Visual display
    with st.expander("🔍 Visual Highlight (Entities)"):
        html = displacy.render(doc, style="ent", jupyter=False)
        st.write(f"<div style='background-color:#f9f9f9;padding:10px;border-radius:10px'>{html}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: grey; font-size: 14px;">
        <p>Created by <strong>Ashlesha Chikhale</strong></p>
        <p>PRN: 1032220257</p>
        <p>Email: <a href="mailto:1032220257@mitwpu.edu.in">1032220257@mitwpu.edu.in</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
