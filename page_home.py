import streamlit as st
from entry import Entry

class Page_Home:

    def __init__(self):
        self.entry = Entry()
    
    def save_inputs(self, file, relation_scheme_name):
        self.entry.set_content(file.read())
        self.entry.set_relation_scheme_name(relation_scheme_name)
        self.entry.saves()

    def run(self):
        
        # Title section
        st.title("Projet GPT-SQL")
        st.subheader("Spécifiez votre :orange[document texte] et votre :blue[schéma de relation]")

        # Separator
        st.markdown("---")
        
        # Text section
        st.header(":orange[Texte]")
        file = st.file_uploader("Text", type=None, accept_multiple_files=False, label_visibility="hidden")

        # Separator
        st.markdown("---")
        
        # Relation scheme section
        st.header(":blue[Schéma de relation]")
        relation_scheme_name = st.text_input("Nom", max_chars=25)
        
        # Separator
        st.markdown("---")
        
        # Next page button
        next_button = st.button("Suivant", type='primary')
        
        # If "Suivant" button clicked
        if next_button :
            self.save_inputs(file, relation_scheme_name)
            #st.switch_page("pages/2_page_attributes.py")

page = Page_Home()
page.run()
