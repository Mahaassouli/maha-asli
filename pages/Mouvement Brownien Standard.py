import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("Simulation du Mouvement Brownien Standard")

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

with st.expander("Definition"):
    st.markdown(r"""
        Le mouvement brownien standard, également appelé processus de Wiener, est un modèle stochastique continu noté $W_t$. Ce processus est défini sur un intervalle de temps $t$ et possède les propriétés caractéristiques suivantes :

        1. Au temps initial ($t = 0$), le processus démarre à zéro : $W_0 = 0$.

        2. Les incréments entre deux instants de temps distincts, $W_{t_2} - W_{t_1}$, sont indépendants pour $t_2 > t_1$.

        3. La distribution des incréments suit une loi normale, c'est-à-dire que $W_{t_2} - W_{t_1}$ est distribué selon $\mathcal{N}(0, t_2 - t_1)$.

        Mathématiquement, le mouvement brownien standard est formulé par l'équation :

        $W_t = W_0 + \sum_{i=1}^{n} Z_i \sqrt{t_i - t_{i-1}}$

        où $W_0$ est la valeur initiale, $Z_i$ sont des variables aléatoires indépendantes et identiquement distribuées selon une loi normale standard ($\mathcal{N}(0, 1)$), $n$ est le nombre d'intervalles de temps, et $t_i$ est la $i$-ème valeur de la grille temporelle.

        Pour générer les incréments aléatoires ($dB$) dans le contexte d'une simulation, on utilise la formule :

        $dB = \sqrt{dt} \times \text{np.random.normal(size=(n-1, d))}$

        où $dt$ est le pas de temps, $n$ est le nombre d'intervalles de temps, et $d$ est la dimension du mouvement brownien.

        À travers la simulation, nous pouvons visualiser la trajectoire du mouvement brownien standard au fil du temps.
    """)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def simulate_brownian_motion(T, n, d):
    times = np.linspace(0., T, n)
    dt = times[1] - times[0]
    dB = np.sqrt(dt) * np.random.normal(size=(n-1, d))
    B0 = np.zeros(shape=(1, d))
    B = np.concatenate((B0, np.cumsum(dB, axis=0)), axis=0)
    return times, B

def main():
    

    # Widgets pour les paramètres de la simulation
    T_button = st.number_input("Durée de la simulation (T)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    n_button = st.number_input("Nombre d'intervalles de temps (n)", min_value=10, max_value=1000, value=100, step=10)
    dimension_button = st.number_input("Dimension du mouvement brownien (d)", min_value=1, max_value=10, value=1)

    # Bouton pour déclencher la simulation
    if st.button("Simuler le Mouvement Brownien"):
        # Simulation du mouvement brownien
        times, brownian_path = simulate_brownian_motion(T_button, n_button, dimension_button)

        # Tracé de la trajectoire
        st.line_chart(pd.DataFrame({"Valeur": brownian_path[:, 0]}))

        # Aperçu des valeurs générées
        st.subheader("Aperçu des valeurs générées:")
        df_preview = pd.DataFrame({"Temps": times[:], "Valeur": brownian_path[:, 0]})
        st.write(df_preview)

if __name__ == "__main__":
    main()
