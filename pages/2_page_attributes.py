import streamlit as st
import pandas as pd
from entry import Entry

POSSIBLE_VALUES = ["Non spécifié", "Texte seulement", "Nombre seulement", "Intervalle", "Booléen", "Personalisé"]

class Page_Attributes:

    def __init__(self):
        self.entry = Entry()
        self.name_button = "Ajouter"

    def run(self):
        
        #Title section
        st.title("Projet GPT-SQL")
        st.subheader("Spécifier les :orange[noms des attributs] ainsi que leur :blue[domaine]")

        # Separator
        st.markdown("---")
        
        # Form title
        st.subheader("Ajouter un attribut")
        
        # Form
        with st.form("add_attribute"):

            # attribute name input
            self.attribute_name = st.text_input(":orange[Nom de l'attribut]")

            # attribute domain selector
            self.attribute_domain = st.selectbox(
                ":blue[Domaine]", 
                POSSIBLE_VALUES,
                index=None,
                placeholder="Sélectionner un domaine",
                label_visibility="visible")
            
            # If no item selected
            if(self.attribute_domain == None):
                self.name_button = "Ajouter"
            
            # If personalized mode selected
            if(self.attribute_domain == "Personalisé"):
                self.name_button = "Confirmer"
                self.attribute_domain = st.text_area(":gray[* entrer vos valeurs sous forme d'éléments séparés par des espaces]",
                                                     placeholder="e.i. valeur1 valeur2 valeurX")

            # If range mode selected
            if(self.attribute_domain == "Intervalle"):
                self.name_button = "Confirmer"
                min_value = st.number_input("Borne minimale")
                max_value = st.number_input("Borne maximale")
                type_of_number_value = st.radio("Type de valeur", ["entier", "décimal"], index=1)
            
            # If boolean mode selected
            if(self.attribute_domain == "Booléen"):
                self.name_button = "Confirmer"
                type_of_bool = st.radio("Booléen à utiliser", ["vrai ou faux","seulement vrai","seulement faux"])
            
            # If not specified mode selected
            if(self.attribute_domain == "Non spécifié"):
                self.name_button = "Confirmer"
                st.write(":warning: :orange[Un domaine non spécifié acceptera toutes les valeurs et n'affinera pas le résultat]")
           
            # Submit button section
            st.write(" ") # Spacing
            submit_add_attribute_form = st.form_submit_button(self.name_button)
        
        # Next button section
        st.write(" ") #Spacing
        next_state_button = st.button("Suivant", type='primary')

page_attributes = Page_Attributes()
page_attributes.run()
