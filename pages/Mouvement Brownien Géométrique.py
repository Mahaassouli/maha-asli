import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


T = 1
def simulate_geometric_brownian_motion(S0, mu, sigma, T, n):
    



    
    dt = T/n
    t = np.linspace(0., T, n+1)
    W = np.random.standard_normal(size=n+1) 
    W = np.cumsum(W)*np.sqrt(dt) 
    X = (mu-0.5*sigma**2)*t + sigma*W
    S = S0*np.exp(X) 
    return t, S

def main():
    st.title("Simulation du Mouvement Brownien Géométrique")

    # Widgets pour les paramètres de la simulation
    S0 = st.number_input("Prix initial de l'actif (S0)", min_value=1, value=100)
    mu = st.number_input("Rendement moyen par unité de temps (mu)", min_value=0.0, value=0.1, step=0.06)
    sigma = st.number_input("Volatilité (sigma)", min_value=0.0, value=0.2, step=0.01)
    
    n = st.number_input("Nombre d'intervalles de temps (n)", min_value=10, value=100, step=10)

    # Bouton pour déclencher la simulation
    if st.button("Simuler le Mouvement Brownien Géométrique"):
        # Simulation du mouvement brownien géométrique
        times, prices = simulate_geometric_brownian_motion(S0, mu, sigma, T, n)

        # Tracé de la trajectoire
        st.subheader("Graphe generé")
        st.line_chart(pd.DataFrame({ "Prix": prices}))

        # Aperçu des valeurs générées
        st.subheader("Aperçu des valeurs générées:")
        df_preview = pd.DataFrame({"Temps": times[:], "Prix": prices[:]})
        st.write(df_preview)

if __name__ == "__main__":
    main()
