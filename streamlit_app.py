import os; print(os.getcwd()) 



import streamlit as st
from data_processing_and_visualization import load_and_preprocess_data, plot_funding_goals, plot_backers_distribution, plot_state_distribution, plot_project_duration_distribution, plot_success_rate_by_category_and_year, plot_pledged_by_state_and_category, plot_avg_pledged_per_person_by_state_and_category, plot_projects_per_creator


# Chargement des données
df = load_and_preprocess_data('Kickstarter_4.csv')


st.sidebar.title("Sommaire")
pages=["Projet Kickstarter", "Analyse des Données"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
  

  
  st.header("Bienvenue sur Notre Analyse Kickstarter")
  container = st.container()
  container.write("Kickstarter est une plateforme de financement participatif qui permet aux créateurs de projets de toutes sortes de lever des fonds auprès du grand public. Depuis son lancement, des milliers de projets ont vu le jour grâce à la générosité et à l'engagement des contributeurs du monde entier. Mais qu'est-ce qui fait le succès d'un projet sur Kickstarter ? C'est la question centrale de notre analyse.")
  
  st.header("Contexte du Projet")
  container = st.container()
  container.write("Dans ce projet, nous plongeons au cœur de Kickstarter pour explorer et analyser les facteurs qui influencent le succès d'un projet. Notre but est de dégager des tendances, identifier des caractéristiques clés et, éventuellement, prédire la réussite d'un projet basée sur des données historiques. Nous avons collecté et traité un ensemble de données représentatif des projets Kickstarter pour mener notre étude.")

  st.header("Objectifs de l'Analyse")
  container = st.container()
  container.write("Notre analyse vise à :")
  container.write("- Comprendre les dynamiques de succès des projets sur Kickstarter.")
  container.write("- Identifier les éléments et caractéristiques communs aux projets réussis.")
  container.write("- Explorer l'impact de différents facteurs, tels que la catégorie du projet, l'objectif de financement, la durée de la campagne, et bien plus, sur le succès d'un projet.")
  container.write("- Fournir des insights précieux pour les futurs créateurs de projet sur Kickstarter.")


  st.header("À quoi s'attendre ?")
  container = st.container()
  container.write("Dans les pages suivantes de cette application, vous découvrirez :")
  container.write("- **Analyse des Données** : Une exploration détaillée de notre jeu de données Kickstarter, offrant un aperçu des tendances, des statistiques descriptives, et un examen des données manquantes ou aberrantes.")
  container.write("- **Visualisations Interactives** : Plongez dans une série de graphiques et visualisations dynamiques qui vous permettront d'interagir avec les données. Explorez la répartition des projets par catégorie, l'évolution du financement au fil du temps, et bien plus.")
  container.write("- **Insights et Conclusions** : Basé sur notre analyse, nous partagerons des observations clés et des recommandations pour maximiser les chances de succès d'un projet Kickstarter.")
            

if page == pages[1] : 

    plot_state_distribution(df)
    container = st.container()
    container.write("Ce graphique fournit un aperçu clair de la répartition des projets Kickstarter en fonction de leur état final (réussi, échoué, annulé, etc.). En visualisant ces données, les utilisateurs peuvent rapidement évaluer la proportion de projets qui ont atteint leur objectif par rapport à ceux qui ne l'ont pas fait, offrant une perspective précieuse sur la réussite globale des initiatives sur la plateforme.")


    # Sélection des filtres
    state = st.selectbox('État du projet', options=['Tous'] + list(df['state'].unique()), index=0)
    category = st.selectbox('Catégorie', options=['Tous'] + list(df['main_category'].unique()), index=0)
    year = st.selectbox('Année de lancement', options=['Tous'] + list(sorted(df['launch_year'].unique())), index=0)
    # Application des filtres
    if state == 'Tous':
        state = None
    if category == 'Tous':
        category = None
    if year == 'Tous':
        year = None
    else:
        year = int(year)
    
    plot_funding_goals(df, state=state, category=category, year=year)
    container = st.container()
    container.write("Ce graphique présente la distribution des objectifs de financement des projets Kickstarter, permettant aux utilisateurs de comprendre les ambitions financières des créateurs. Il met en évidence les montants que les porteurs de projets espèrent lever, fournissant un aperçu de la gamme d'objectifs de financement et de la manière dont ils sont répartis à travers la plateforme")


    plot_backers_distribution(df)  # Affichage de la distribution du nombre de contributeurs
    container = st.container()
    container.write("Cette visualisation montre comment le nombre de contributeurs varie sur Kickstarter. Il est possible de zoomer sur des segments spécifiques de données en sélectionnant une plage de nombres de contributeurs.")
    
    plot_project_duration_distribution(df)
    container = st.container()
    container.write("Ce graphique révèle la durée des campagnes Kickstarter, de leur lancement à leur conclusion. Il offre un aperçu de combien de temps les créateurs allouent à leurs campagnes pour atteindre leur objectif de financement, soulignant les stratégies de durée qui prévalent au sein de la communauté Kickstarter.")

    plot_success_rate_by_category_and_year(df)
    container = st.container()
    container.write("En explorant le taux de succès des projets Kickstarter divisés par catégorie, ce graphique fournit une analyse comparative de la performance des projets selon leur domaine. Cela permet de détecter les secteurs où les projets ont tendance à réussir davantage, ainsi que ceux où les défis semblent plus prononcés.")

    plot_pledged_by_state_and_category(df)
    container = st.container()
    container.write("Ce graphique examine les montants financiers effectivement engagés en fonction de l'état du projet et offre un filtre par catégorie. Il éclaire sur la générosité des contributeurs selon que les projets sont réussis, échoués, ou annulés, et permet d'observer ces dynamiques au sein de catégories spécifiques.")
    
    plot_avg_pledged_per_person_by_state_and_category(df)
    container = st.container()
    container.write("Cette visualisation se focalise sur le montant moyen engagé par contributeur en analysant à la fois l'état final du projet et sa catégorie. Elle permet d'identifier non seulement comment les contributions varient selon l'issue des projets, mais également la générosité relative des contributeurs dans différents domaines.")

    plot_projects_per_creator(df)
    container = st.container()
    container.write("Ce graphique met en lumière le nombre de projets lancés par chaque créateur sur Kickstarter, offrant une fenêtre sur le niveau d'expérience et d'activité des créateurs sur la plateforme. L'option pour choisir entre des échelles linéaire et logarithmique facilite l'examen de cette répartition à travers toute la gamme d'expérience, des novices aux vétérans très actifs.")