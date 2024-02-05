import streamlit as st
import numpy as np
from scipy.stats import norm

def black_scholes_option_price(S, K, T, r, sigma, option_type='call'):
    """
    Calcule le prix d'une option européenne (CALL ou PUT) en utilisant le modèle de Black-Scholes-Merton.

    :param S: Prix actuel de l'actif sous-jacent
    :param K: Prix d'exercice de l'option
    :param T: Durée jusqu'à l'expiration de l'option (en années)
    :param r: Taux sans risque (annuel)
    :param sigma: Volatilité de l'actif sous-jacent (annuelle)
    :param option_type: Type d'option ('call' ou 'put')
    :return: Prix de l'option
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Le type d'option doit être 'call' ou 'put'.")

    return option_price

def options_simulation():
    st.title("Simulation des Options Européennes CALL et PUT")

    # Paramètres de l'option
    st.subheader("Paramètres de l'option:")
    S = st.number_input("Prix actuel de l'actif sous-jacent (S)", value=100.0)
    K = st.number_input("Prix d'exercice de l'option (K)", value=100.0)
    T = st.number_input("Durée jusqu'à l'expiration de l'option (T en années)", value=1.0)
    r = st.number_input("Taux sans risque (r)", value=0.05)
    sigma = st.number_input("Volatilité de l'actif sous-jacent (sigma)", value=0.2)

    # Type d'option
    option_type = st.radio("Type d'option:", ('Call', 'Put'))

    # Bouton pour lancer la simulation
    if st.button("Lancer la simulation", key="simulate_button"):
        option_type = option_type.lower()
        option_price = black_scholes_option_price(S, K, T, r, sigma, option_type)

        # Afficher le résultat
        st.subheader(f"Résultat de la simulation ({option_type.capitalize()} Option):")
        st.write(f"Le prix de l'option est estimé à : {option_price:.4f}")

if __name__ == "__main__":
    options_simulation()
