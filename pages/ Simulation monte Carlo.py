import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

def monte_carlo_simulation():
    st.title("Simulation de Monte Carlo pour le Prix d'une Action")

    # Saisie du ticker de l'action
    ticker = st.text_input("Entrez le ticker de l'action", "GOOGL")

    # Période de simulation
    start_date = st.date_input("Date de début de simulation", pd.to_datetime('2022-01-01'))

    # Nombre de simulations
    num_simulations = st.number_input("Nombre de simulations", value=1, step=1)

    # Bouton pour lancer la simulation
    if st.button("Lancer la simulation", key="simulate_button"):
        # Récupération des données historiques de l'action
        try:
            stock_data = yf.download(ticker, start=start_date)
        except:
            st.warning("Erreur : Impossible de récupérer les données historiques. Vérifiez le ticker et les dates sélectionnées.")
            return

        # Afficher les données historiques
        st.subheader("Données historiques de l'action:")
        st.dataframe(stock_data.style.set_properties(**{'background-color': '#f0f0f0', 'color': 'green'}), use_container_width=True)

        # Prix initial de l'action
        initial_price = stock_data['Adj Close'].iloc[-1]
        st.subheader("Informations sur l'action:")
        st.write(f"Le prix initial du stock est : {initial_price:.2f}")

        # Volatilité du stock
        returns = np.log(1 + stock_data['Adj Close'].pct_change())
        volatility = returns.std()
        st.write(f"La volatilité du stock est : {volatility:.4f}")

        # Afficher la formule mathématique
        st.subheader("Formule mathématique de la simulation de Monte Carlo :")
        st.latex(r'''
            \text{{Simulated Prices}}_i = \text{{Initial Price}} \times \prod_{j=1}^{N} (1 + \text{{Simulated Returns}}_j)
        ''')

        # Simulation de Monte Carlo
        all_sims = []

        for i in range(num_simulations):
            # Génération de rendements aléatoires basés sur les rendements historiques
            simulated_returns = np.random.normal(returns.mean(), volatility, len(stock_data))
            simulated_prices = initial_price * (1 + simulated_returns).cumprod()
            all_sims.append(simulated_prices)

        # Dataframe avec les simulations
        df_info = pd.DataFrame(all_sims)
        df_info_transposed = df_info.transpose()

        # Tracé des simulations
        st.subheader("Graphique des simulations:")
        fig = px.line(df_info_transposed, title="Simulation de Monte Carlo pour le Prix d'une Action")
        fig.update_layout(xaxis_title="Jours", yaxis_title="Prix simulé")
        st.plotly_chart(fig)

        # Calcul des métriques supplémentaires
        average_final_price = df_info_transposed.iloc[-1].mean().mean()
        min_final_price = df_info_transposed.min().min()
        max_final_price = df_info_transposed.max().max()
        st.write(f"Le prix final moyen est : {average_final_price:.2f}")
        st.write(f"Le prix  minimum est : {min_final_price:.2f}")
        st.write(f"Le prix  maximum est : {max_final_price:.2f}")
        # Afficher le code généré
        st.subheader("Code généré:")
        code = '''
initial_price = stock_data['Adj Close'].iloc[len(stock_data)-1]
st.write(initial_price)

all_sims = []
returns = np.log(1 + stock_data['Adj Close'].pct_change())
volatility = returns.std()

# Simulation de Monte Carlo
all_sims = []

for i in range(num_simulations):
    # Génération de rendements aléatoires basés sur les rendements historiques
    simulated_returns = np.random.normal(returns.mean(), volatility, len(stock_data))
    simulated_prices = initial_price * (1 + simulated_returns).cumprod()
    all_sims.append(simulated_prices)
'''
        st.code(code, language='python')

if __name__ == "__main__":
    monte_carlo_simulation()
