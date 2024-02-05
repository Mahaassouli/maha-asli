import streamlit as st

# Styles personnalisés
custom_styles = """
    body {
        color: #1e1e1e;
        background-color: #00ff00;
    }
    .header {
        color: #e60000;
        text-align: center;
    }
    .objectifs {
        font-weight: bold;
        color: #3333cc;
    }
"""

# Ajouter les styles au document HTML
st.markdown(f'<style>{custom_styles}</style>', unsafe_allow_html=True)

# Page de présentation
def presentation_page():
    st.title("Projet de Simulations Monte Carlo et Mouvement Brownien")

    st.markdown(
        "Bienvenue sur la page de présentation de mon projet de simulations Monte Carlo et Mouvement Brownien.",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='header'>Objectifs du Projet</div>", unsafe_allow_html=True)

    st.markdown(
        "Cette présentation est faite dans le cadre du projet du module Processus Stochastique et vise à réaliser les simulations suivantes:",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='objectifs'>- Simulation du mouvement Brownien Standard</div>", unsafe_allow_html=True)
    st.markdown("<div class='objectifs'>- Simulation du mouvement Brownien géométrique</div>", unsafe_allow_html=True)
    st.markdown("<div class='objectifs'>- Simulation de la valeur du Put et du Call Européen</div>", unsafe_allow_html=True)
    st.markdown("<div class='objectifs'>- Simulation de Monte Carlo pour le Prix d'une Action</div>", unsafe_allow_html=True)

# Exécuter la page de présentation
if __name__ == "__main__":
    presentation_page()



