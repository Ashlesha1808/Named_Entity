import streamlit as st
import spacy
from spacy import displacy

# Download and load spaCy model (works on Streamlit Cloud)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Page config
st.set_page_config(page_title="NER App", layout="centered")

# Title
st.markdown("<h1 style='color:#2c3e50;'>🧠 Named Entity Recognition (NER)</h1>", unsafe_allow_html=True)
st.markdown("Enter English text with Indian names. This app extracts **People**, **Locations**, and **Organizations** using spaCy.")

# Input area
text_input = st.text_area("✍️ Enter your text here:", 
    "Ashlesha Chikhale met Narendra Modi at MITWPU in Pune. Infosys and ISRO were discussed.")

# Entity extraction button
if st.button("🚀 Extract Entities") and text_input.strip() != "":
    doc = nlp(text_input)

    # Dictionary for entity storage
    entity_dict = {"PERSON": [], "GPE": [], "ORG": []}

    for ent in doc.ents:
        if ent.label_ in entity_dict:
            entity_dict[ent.label_].append(ent.text)

    st.markdown("## 🧾 Extracted Entities")

    if entity_dict["PERSON"]:
        st.markdown("### 👤 People")
        for person in set(entity_dict["PERSON"]):
            st.markdown(f"- {person}")

    if entity_dict["GPE"]:
        st.markdown("### 🗺️ Locations")
        for location in set(entity_dict["GPE"]):
            st.markdown(f"- {location}")

    if entity_dict["ORG"]:
        st.markdown("### 🏢 Organizations")
        for org in set(entity_dict["ORG"]):
            st.markdown(f"- {org}")

    if not any(entity_dict.values()):
        st.warning("No named entities found!")

    # Visual displacy output
    with st.expander("🔍 Highlight Entities in Text"):
        html = displacy.render(doc, style="ent", jupyter=False)
        st.write(
            f"<div style='background-color:#f9f9f9;padding:10px;border-radius:10px'>{html}</div>", 
            unsafe_allow_html=True
        )

# Footer with author details
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
