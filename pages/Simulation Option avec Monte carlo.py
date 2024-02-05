import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt



def monte_carlo_option_pricing(S, K, T, r, sigma, option_type='call', num_simulations=1000, num_steps=252):
    """
    Calcule le prix d'une option européenne (CALL ou PUT) en utilisant la méthode de Monte Carlo.

    :param S: Prix actuel de l'actif sous-jacent
    :param K: Prix d'exercice de l'option
    :param T: Durée jusqu'à l'expiration de l'option (en années)
    :param r: Taux sans risque (annuel)
    :param sigma: Volatilité de l'actif sous-jacent (annuelle)
    :param option_type: Type d'option ('call' ou 'put')
    :param num_simulations: Nombre de simulations Monte Carlo
    :param num_steps: Nombre de pas temporels dans chaque simulation
    :return: Liste des prix d'option pour chaque simulation
    """
    option_prices = []

    dt = T / num_steps

    for _ in range(num_simulations):
        price_path = [S]
        for _ in range(num_steps):
            z = np.random.normal(0, 1)
            price_path.append(price_path[-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z))

        if option_type == 'call':
            payoff = np.maximum(price_path[-1] - K, 0)
        elif option_type == 'put':
            payoff = np.maximum(K - price_path[-1], 0)
        else:
            raise ValueError("Le type d'option doit être 'call' ou 'put'.")

        discounted_payoff = payoff * np.exp(-r * T)
        option_prices.append(discounted_payoff)

    return option_prices

def monte_carlo_simulation():
    st.title("Simulation des Options Européennes par Monte Carlo")

    # Paramètres de l'option
    st.subheader("Paramètres de l'option:")
    S = st.number_input("Prix actuel de l'actif sous-jacent (S)", value=100.0)
    K = st.number_input("Prix d'exercice de l'option (K)", value=100.0)
    T = st.number_input("Durée jusqu'à l'expiration de l'option (T en années)", value=1.0)
    r = st.number_input("Taux sans risque (r)", value=0.05)
    sigma = st.number_input("Volatilité de l'actif sous-jacent (sigma)", value=0.2)

    # Type d'option
    option_type = st.radio("Type d'option:", ('Call', 'Put'))

    # Bouton pour lancer la simulation Monte Carlo
    if st.button("Lancer la simulation Monte Carlo", key="monte_carlo_button"):
        option_type = option_type.lower()
        option_prices = monte_carlo_option_pricing(S, K, T, r, sigma, option_type, num_steps=252)

        # Afficher le résultat
        st.subheader(f"Résultat de la simulation Monte Carlo ({option_type.capitalize()} Option):")
        st.write(f"Le prix de l'option est estimé à : {np.mean(option_prices):.4f}")

        

if __name__ == "__main__":
   
    monte_carlo_simulation()
