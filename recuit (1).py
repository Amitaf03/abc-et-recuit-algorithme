import numpy as np
import matplotlib.pyplot as plt
import random
import time
import statistics





# Définir les distances entre les villes manuellement
def generate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    
    # Remplir la matrice des distances
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = random.randint(50, 1000)  # Distance aléatoire entre 50 et 1000 km
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance
    
    return distance_matrix

# Calcul de la distance totale pour une tournée donnée
def total_distance(distance_matrix, tour):
    distance = 0
    for i in range(len(tour)):
        distance += distance_matrix[tour[i], tour[(i + 1) % len(tour)]]
    return distance

# Perturbation de la solution actuelle (échange de deux villes)
def perturb_tour(tour):
    new_tour = tour.copy()
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

# Algorithme de recuit simulé
def simulated_annealing(distance_matrix, initial_temp, cooling_rate, min_temp):
    num_cities = len(distance_matrix)
    current_tour = list(range(num_cities))
    random.shuffle(current_tour)
    current_cost = total_distance(distance_matrix, current_tour)
    
    best_tour = current_tour
    best_cost = current_cost
    
    temp = initial_temp
    
    while temp > min_temp:
        new_tour = perturb_tour(current_tour)
        new_cost = total_distance(distance_matrix, new_tour)
        delta_e = new_cost - current_cost
        
        if new_cost < current_cost or random.uniform(0, 1) < np.exp(-delta_e / temp):
            current_tour = new_tour
            current_cost = new_cost
        
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
        
        temp *= cooling_rate
    
    return best_tour, best_cost
 

 
# Visualisation de la tournée
def plot_path(cities, path):
    coords = np.random.rand(len(cities), 2)  # Coordonnées aléatoires pour la visualisation
    
    x = [coords[i][0] for i in path] + [coords[path[0]][0]]
    y = [coords[i][1] for i in path] + [coords[path[0]][1]]
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'bo-', label='Chemin') 
    for i, (cx, cy) in enumerate(coords):
        plt.text(cx, cy, f'{cities[i]}', fontsize=8, ha='right')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Meilleur chemin trouvé par l\'algorithme Recuit')
    plt.legend() 
    plt.show()


# Paramètres
initial_temp = 1000
cooling_rate = 0.995
min_temp = 1

# Définition des 150 villes marocaines
cities = [
    'Casablanca', 'Rabat', 'Marrakech', 'Fes', 'Tangier', 'Agadir', 'Oujda', 'Meknes', 'Tetouan', 'Kenitra',
    'Safi', 'Essaouira', 'El Jadida', 'Nador', 'Taza', 'Khouribga', 'Beni Mellal', 'Laayoune', 'Ouarzazate', 'Errachidia',
    'Chefchaouen', 'Dakhla', 'Khemisset', 'Tiznit', 'Ifrane', 'Larache', 'Mohammedia', 'Azrou', 'Sefrou', 'Ouezzane',
    'Guelmim', 'Asilah', 'Boujdour', 'Ksar el-Kebir', 'Oualidia', 'Berkane', 'Settat', 'Tantan', 'Sidi Ifni', 'Tinghir',
    'Youssoufia', 'Sidi Bennour', 'Sidi Slimane', 'Taroudant', 'Ait Melloul', 'Sidi Kacem', 'Taourirt', 'Zagora', 'Midelt',
    'Guercif', 'Fnideq', 'Martil', 'El Kelaa des Sraghna', 'Sidi Yahya El Gharb', 'Ouazzane', 'Sidi Slimane', 'Benslimane', 
    'Bouznika', 'Skhirat', 'Temara', 'Sale', 'Tamansourt', 'Ait Ourir', 'Chichaoua', 'Amizmiz', 'Imintanoute', 'Tnine Chtouka', 
    'Sidi Bou Othmane', 'Ben Guerir', 'Ras El Ain', 'Sidi Rahal', 'Boujdour', 'Es Smara', 'Akhfennir', 'Tarfaya', 'Sidi Ifni', 
    'Massa', 'Tata', 'Akka', 'Assa', 'Bouizakarne', 'Inezgane', 'Drargua', 'Belfaa', 'Taliouine', 'Ida Ougnidif', 'Aoulouz', 
    'Biougra', 'Temsia', 'El Arba Tighza', 'Tamegroute', 'Agdz', 'Tamgrout', 'Beni Tajjite', 'Outat El Haj', 'Boumia', 'Bouanane', 
    'El Aaiun', 'Goulmima', 'Boumalne Dades', 'El Hajeb', 'El Hoceima', 'Taounate', 'Sefrou', 'Jerada', 'Figuig', 'Sidi Ifni',
    'Smara', 'Azilal', 'Tahala', 'Kasbah Tadla', 'Moulay Yacoub', 'Rissani', 'Imilchil', 'Anza', 'Sidi Bouzid', 'Oued Zem',
    'Ain Harrouda', 'Mellilia', 'Bouskoura', 'Dar Bouazza', 'Mediouna', 'Tit Mellil', 'Chichaoua', 'Lakhyayta', 'Ouled Teima',
    'Azemmour', 'Oulad Berhil', 'Moulay Bousselham', 'Asilah', 'Merzouga', 'Ain Taoujdat', 'Beni Ayat', 'Ait Ishaq', 'Ait Baha',
    'Ait Youssef Ou Ali', 'Ait Daoud', 'Afourar', 'Tamesna', 'Bouarfa', 'Beni Oukil', 'Gourrama', 'Tan-Tan', 'Boumia', 'Sidi Yahya',
    'Tarfaya', 'Sidi Allal Tazi', 'Bir Jdid', 'El Aioun Sidi Mellouk', 'Ain Dorij', 'Jorf', 'El Kbab', 'Lalla Takerkoust',
    'Bni Chiker', 'Jorf El Melha', 'Taza', 'Demnate', 'Sidi Ifni', 'Boumalne Dades', 'Moulay Bousselham', 'Ain Leuh', 'Oulad Teima',
    'Zag', 'Boujdour', 'El Guerdane', 'Khemis Sahel', 'Had Kourt', 'Sidi Bouafif', 'Zawiya Ahansal', 'El Ksiba'
]



# Génération de la matrice des distances
distance_matrix = generate_distance_matrix(cities)
start_time = time.time()
# Exécution de l'algorithme de recuit simulé

num_runs = 10
execution_times = []
best_distances = []

for _ in range(num_runs):
    start_time = time.time()

    best_tour, best_cost = simulated_annealing(distance_matrix, initial_temp, cooling_rate, min_temp)
    
    end_time = time.time()

    # Calcul du temps d'exécution
    execution_time = end_time - start_time
    execution_times.append(execution_time)

    # Ajout de la meilleure distance trouvée à la liste
    best_distances.append(best_cost)
    
    # Affichage de la meilleure distance trouvée pour chaque exécution
    print(f"Distance totale pour l'exécution {_ + 1}: {best_cost}")

# Calcul des statistiques sur les meilleures distances
mean_distance = np.mean(best_distances)
std_distance = np.std(best_distances)

# Calcul du temps d'exécution moyen
average_execution_time = statistics.mean(execution_times)

# Affichage des résultats globaux
print(f"Temps d'exécution moyen sur {num_runs} exécutions : {average_execution_time:.4f} secondes")
print(f"Algorithme du recuit : Distance moyenne = {mean_distance:.2f} km, Écart-type = {std_distance:.2f}")




# Coordonnées fictives pour la visualisation (si nécessaire, ajustez les coordonnées réelles)
city_coords = np.random.rand(len(cities), 2)

# Visualisation
plot_path(cities, best_tour)
