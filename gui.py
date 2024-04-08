import streamlit as st

class Gui:

    def __init__(self):
        
        self.title = "Projet GPT-SQL"
        self.subheader_info = '''Spécifiez votre :orange[document texte] et votre :blue[schéma de relation]''' 
    


    def page_one(self):

        st.title(self.title)
        st.subheader(self.subheader_info)

        st.markdown("---")
                
        st.header(":orange[Texte]")
        text_file = st.file_uploader("", type=None, accept_multiple_files=False, label_visibility="hidden")

        st.markdown("---")

        st.header(":blue[Schéma de relation]")
        relation_scheme_name = st.text_input("Nom", max_chars=25)
        
        st.markdown("---")

        next = st.button("Suivant", type='primary')

        if next :
            self.page_two()
       


gui = Gui()
gui.page_one()



