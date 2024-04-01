

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement et prétraitement des données
def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    
    # Supposons que 'launched_at' est déjà dans un format de timestamp UNIX (secondes depuis epoch)
    # Convertir 'launched_at' en datetime
    df['launch_date'] = pd.to_datetime(df['launched_at'], unit='s')
    
    # Extraire l'année de lancement et créer la colonne 'launch_year'
    df['launch_year'] = df['launch_date'].dt.year
    

    
    return df



import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_state_distribution(df):
    sns.set()  # Utilise le style par défaut de Seaborn pour le graphique

    # Palette de couleurs personnalisée pour les différents états
    palette_couleurs = {
        "successful": "green",  # Réussis
        "failed": "red",        # Échoués
        "canceled": "blue"      # Annulés
    }

    plt.figure(figsize=(12, 6))  # Définit la taille du graphique
    
    # Création du graphique de répartition avec la palette de couleurs personnalisée
    ax = sns.countplot(x='state', data=df, palette=palette_couleurs, order=["successful", "failed", "canceled"])
    
    # Définition des étiquettes de l'axe des x en français
    ax.set_xticklabels(['Réussis', 'Échoués', 'Annulés'])
    plt.xlabel('État du projet')
    plt.ylabel('Nombre de projets')
    plt.title('Répartition du dataset par "État"')

    st.pyplot(plt.gcf())  # Affiche le graphique dans Streamlit en récupérant la figure courante avec plt.gcf()

# Ici, vous appelleriez la fonction plot_state_distribution en lui passant votre DataFrame






import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

# Amélioration de la visualisation des objectifs de financement
def plot_funding_goals(df, state=None, category=None, year=None):
    # Définis une palette de couleurs pour les états et les catégories
    state_colors = {'successful': 'green', 'failed': 'red', 'canceled': 'blue'}
    category_colors = ['skyblue', 'olive', 'gold', 'teal', 'coral', 'darkorchid', 'tomato', 'sienna', 'chartreuse', 'cadetblue']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    if year:
        df = df[df['launch_year'] == year]
    
    # Ajoute un code couleur par état du projet si spécifié
    if state:
        df_filtered = df[df['state'] == state]
        ax.hist(df_filtered['usd_goal'], bins=np.logspace(1, 10, 50), alpha=0.5, color=state_colors[state], label=state)
    # Sinon, ajoute un code couleur par catégorie
    elif category:
        if category != 'Tous':
            df_filtered = df[df['main_category'] == category]
            ax.hist(df_filtered['usd_goal'], bins=np.logspace(1, 10, 50), alpha=0.5, color=np.random.choice(category_colors), label=category)
    else:
        # Trace chaque état avec une couleur différente
        for state, color in state_colors.items():
            df_filtered = df[df['state'] == state]
            ax.hist(df_filtered['usd_goal'], bins=np.logspace(1, 10, 50), alpha=0.5, color=color, label=state)

    ax.set_xscale('log')
    ax.set_xlabel('Objectif de Financement (USD)')
    ax.set_ylabel('Nombre de Projets')
    ax.set_title('Distribution des Objectifs de Financement')
    ax.legend()

    # Afficher le graphique dans Streamlit en passant la figure à st.pyplot()
    st.pyplot(fig)




import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_backers_distribution(df):
    # Séparer les données en fonction de l'état du projet
    reussis = df[df['state'] == 'successful']
    echoues = df[df['state'] == 'failed']
    annules = df[df['state'] == 'canceled']
    
    # Déterminer la plage de contributeurs dans les données
    min_backers, max_backers = int(df['backers_count'].min()), int(df['backers_count'].max())
    
    # Utilisation de champs de saisie numérique pour définir la plage de contributeurs
    min_value = st.number_input('Valeur minimale de contributeurs', min_value=min_backers, max_value=max_backers, value=min_backers)
    max_value = st.number_input('Valeur maximale de contributeurs', min_value=min_backers, max_value=max_backers, value=max_backers)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(reussis['backers_count'].clip(lower=min_value, upper=max_value), bins=np.logspace(np.log10(min_value+1), np.log10(max_value+1), 50), alpha=0.5, label='Réussis', color='green')
    ax.hist(echoues['backers_count'].clip(lower=min_value, upper=max_value), bins=np.logspace(np.log10(min_value+1), np.log10(max_value+1), 50), alpha=0.5, label='Échoués', color='red')
    ax.hist(annules['backers_count'].clip(lower=min_value, upper=max_value), bins=np.logspace(np.log10(min_value+1), np.log10(max_value+1), 50), alpha=0.5, label='Annulés', color='blue')
    
    ax.set_xscale('log')
    ax.set_xlabel('Nombre de Contributeurs')
    ax.set_ylabel('Nombre de Projets')
    ax.set_title('Distribution du Nombre de Contributeurs des Projets Kickstarter')
    ax.legend()

    st.pyplot(fig)





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_project_duration_distribution(df):
    # Convertir la durée de secondes en jours
    df['duration_days'] = df['duration'] / (60 * 60 * 24)
    

    # Séparer les données en fonction de l'état du projet
    reussis = df[df['state'] == 'successful']
    echoues = df[df['state'] == 'failed']
    annules = df[df['state'] == 'canceled']

    plt.figure(figsize=(10, 6))
    
    
    # Définir les bins de manière à couvrir la plage de 0 à 100 jours
    bins_range = np.linspace(0, 100, num=40)  # Crée des bins régulièrement espacés de 0 à 100 jours
    
    plt.hist(reussis['duration_days'], bins=bins_range, alpha=0.5, label='Réussis', color='green')
    plt.hist(echoues['duration_days'], bins=bins_range, alpha=0.5, label='Échoués', color='red')
    plt.hist(annules['duration_days'], bins=bins_range, alpha=0.5, label='Annulés', color='blue')

    plt.xlim(0, 100)  # Limite l'axe des abscisses de 0 à 100 jours
    plt.xlabel('Durée des Projets (jours)')
    plt.ylabel('Nombre de Projets')
    plt.title('Distribution de la Durée des Projets Kickstarter')
    plt.legend()

    st.pyplot(plt.gcf())




import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_success_rate_by_category_and_year(df):
    # Sélection d'une année pour filtrer les données
    unique_years = sorted(df['launch_year'].unique())
    selected_year = st.selectbox('Sélectionnez une année:', options=[0] + unique_years, format_func=lambda x: 'Toutes les années' if x == 0 else x)
    
    if selected_year != 0:
        df = df[df['launch_year'] == selected_year]
    
    # Calcul du taux de succès total par catégorie principale
    stats_by_category = df.groupby('main_category').apply(lambda x: pd.Series({
        'Success_rate': (x['state'] == 'successful').mean() * 100  # Taux de succès en pourcentage
    })).reset_index()
    
    # Configuration de Seaborn pour les graphiques
    sns.set()
    
    # Création du graphique
    plt.figure(figsize=(18, 6))
    sns.barplot(x='main_category', y='Success_rate', data=stats_by_category, palette='tab10')
    
    plt.xlabel('Catégorie principale des projets')
    plt.ylabel('Taux de succès (%)')
    plt.title(f'Pourcentage de succès des projets par catégorie pour {selected_year if selected_year != 0 else ""}')
    plt.xticks(rotation=45)
    
    st.pyplot(plt.gcf())  # Affichage du graphique dans Streamlit

# Assurez-vous de charger votre DataFrame df avant d'appeler cette fonction
# df = load_and_preprocess_data('chemin_vers_votre_fichier.csv')
# plot_success_rate_by_category_and_year(df)




import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_pledged_by_state_and_category(df):
    # Configuration de Seaborn pour les graphiques
    sns.set(style="whitegrid")
    
    # Permettre à l'utilisateur de choisir une catégorie
    all_categories = df['main_category'].unique()
    selected_category = st.selectbox('Choisissez une catégorie:', options=['Toutes'] + sorted(all_categories.tolist()))
    
    # Filtrer les données par catégorie si l'utilisateur n'a pas choisi "Toutes"
    if selected_category != 'Toutes':
        df = df[df['main_category'] == selected_category]
    
    # Création du graphique : Distribution des montants engagés par état du projet
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='state', y='usd_pledged', data=df, showfliers=False)  # `showfliers=False` pour exclure les outliers
    
    plt.title(f"Distribution des montants engagés par état du projet - Catégorie: {selected_category}")
    plt.xlabel('État du projet')
    plt.ylabel('Montants engagés (USD)')
    
    st.pyplot(plt.gcf())

# Assurez-vous de charger votre DataFrame df avant d'appeler cette fonction
# df = load_and_preprocess_data('chemin_vers_votre_fichier.csv')
# plot_pledged_by_state_and_category(df)







import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_avg_pledged_per_person_by_state_and_category(df):
    # Calcul du montant moyen engagé par contributeur
    df['avg_pledged_per_person'] = df['usd_pledged'] / df['backers_count']
    
    # Remplacer les infinis et NaN générés par division par 0 ou données manquantes par 0
    df['avg_pledged_per_person'].replace([float('inf'), -float('inf')], np.nan, inplace=True)
    df['avg_pledged_per_person'].fillna(0, inplace=True)
    
    # Permettre à l'utilisateur de choisir une catégorie avec un key unique pour chaque selectbox
    all_categories = df['main_category'].unique()
    selected_category = st.selectbox('Choisissez une catégorie:', options=['Toutes'] + sorted(all_categories.tolist()), key='category_select')
    
    # Filtrer les données par catégorie si l'utilisateur n'a pas choisi "Toutes"
    if selected_category != 'Toutes':
        df = df[df['main_category'] == selected_category]
    
    # Configuration de Seaborn pour les graphiques
    sns.set(style="whitegrid")
    
    # Création du graphique : Distribution des montants engagés par personne par état du projet
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='state', y='avg_pledged_per_person', data=df, showfliers=False)  # `showfliers=False` pour exclure les outliers
    
    plt.title(f"Distribution des montants engagés par personne par état du projet - Catégorie: {selected_category}")
    plt.xlabel('État du projet')
    plt.ylabel('Montant moyen engagé par personne (USD)')
    
    st.pyplot(plt.gcf())

# N'oubliez pas d'appeler cette fonction après avoir chargé votre DataFrame
# plot_avg_pledged_per_person_by_state_and_category(df)








import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_projects_per_creator(df):
    # Compter le nombre de projets par créateur
    creator_counts = df['creator_id'].value_counts()
    
    # Convertir en DataFrame pour la visualisation
    creator_counts_df = creator_counts.reset_index()
    creator_counts_df.columns = ['creator_id', 'num_projects']
    
    # Permettre à l'utilisateur de choisir le type d'échelle pour l'axe des Y
    scale_type_y = st.radio("Choisissez le type d'échelle pour l'axe des y :", ('Linéaire', 'Logarithmique'), key='scale_type_y')
    
    plt.figure(figsize=(12, 8))
    sns.histplot(data=creator_counts_df, x='num_projects', bins=50, kde=False)
    
    plt.title('Nombre de projets par créateur')
    plt.xlabel('Nombre de projets')
    plt.ylabel('Nombre de créateurs')
    
    # Appliquer l'échelle choisie uniquement à l'axe des Y
    plt.yscale('log') if scale_type_y == 'Logarithmique' else plt.yscale('linear')
    
    # Garder l'axe des X en échelle linéaire et limiter sa plage à 0-200
    plt.xlim(0, 125)
    
    st.pyplot(plt.gcf())
