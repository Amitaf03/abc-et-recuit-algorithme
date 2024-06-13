import numpy as np
import random
import matplotlib.pyplot as plt
import time
import random
import statistics







# 150 Villes marocaines
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

# Générer une matrice de distance pour 50 villes marocaines
def generate_distance_matrix():
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = random.randint(50, 1000)  # Distance aléatoire entre 50 et 1000 km
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance
    return distance_matrix

# Calculer la distance totale pour une tournée donnée
def calculate_total_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path)):
        total_distance += distance_matrix[path[i], path[(i + 1) % len(path)]]
    return total_distance

# Générer une solution aléatoire
def generate_random_solution(num_cities):
    solution = list(range(num_cities))
    random.shuffle(solution)
    return solution

# Modifier une solution en permutant deux villes
def neighborhood_solution(solution):
    new_solution = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Algorithme des abeilles
def bees_algorithm(distance_matrix, num_bees, num_elite_sites, num_best_sites, num_iterations, elite_site_size, best_site_size):
    num_cities = len(distance_matrix)
    # Initialisation
    solutions = [generate_random_solution(num_cities) for _ in range(num_bees)]
    best_solution = min(solutions, key=lambda s: calculate_total_distance(s, distance_matrix))
    
    for _ in range(num_iterations):
        new_solutions = []

        # Recherche dans les sites élitistes
        for i in range(num_elite_sites):
            for _ in range(elite_site_size):
                new_solution = neighborhood_solution(solutions[i])
                new_solutions.append(new_solution)
        
        # Recherche dans les meilleurs sites
        for i in range(num_elite_sites, num_best_sites):
            for _ in range(best_site_size):
                new_solution = neighborhood_solution(solutions[i])
                new_solutions.append(new_solution)

        # Générer des solutions aléatoires pour les autres abeilles
        for _ in range(num_bees - num_best_sites * best_site_size - num_elite_sites * elite_site_size):
            new_solutions.append(generate_random_solution(num_cities))
        
        # Sélection des meilleures solutions
        solutions = sorted(new_solutions, key=lambda s: calculate_total_distance(s, distance_matrix))[:num_bees]
        
        # Mise à jour de la meilleure solution trouvée
        current_best_solution = min(solutions, key=lambda s: calculate_total_distance(s, distance_matrix))
        if calculate_total_distance(current_best_solution, distance_matrix) < calculate_total_distance(best_solution, distance_matrix):
            best_solution = current_best_solution
    
    return best_solution, calculate_total_distance(best_solution, distance_matrix)

# Exemple d'utilisation avec 50 villes marocaines
distance_matrix = generate_distance_matrix()
num_bees = 50
num_elite_sites = 5
num_best_sites = 15
num_iterations = 50
elite_site_size = 10
best_site_size = 5

num_runs = 10
execution_times = []
best_distances = []

for _ in range(num_runs):
    start_time = time.time()

    # Exécution de l'algorithme de l'abeille
    best_solution, best_distance = bees_algorithm(distance_matrix, num_bees, num_elite_sites, num_best_sites, num_iterations, elite_site_size, best_site_size)
    
    end_time = time.time()

    # Calcul du temps d'exécution
    execution_time = end_time - start_time
    execution_times.append(execution_time)

    # Ajout de la meilleure distance trouvée à la liste
    best_distances.append(best_distance)
    
    # Affichage de la meilleure distance trouvée pour chaque exécution
    print(f"Distance totale pour l'exécution {_ + 1}: {best_distance}")

# Calcul des statistiques sur les meilleures distances
mean_distance = np.mean(best_distances)
std_distance = np.std(best_distances)

# Calcul du temps d'exécution moyen
average_execution_time = statistics.mean(execution_times)

# Affichage des résultats globaux
print(f"Temps d'exécution moyen sur {num_runs} exécutions : {average_execution_time:.4f} secondes")
print(f"Algorithme de l'Abeille : Distance moyenne = {mean_distance:.2f} km, Écart-type = {std_distance:.2f}")

print("Meilleure solution:", [cities[i] for i in best_solution])
print("Distance totale:", best_distance)
start_time = time.time()
generate_distance_matrix()
end_time = time.time()

computation_time = end_time - start_time
print(f"Computation time : {computation_time} seconds")

# Visualiser le chemin
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
    plt.title('Meilleur chemin trouvé par l\'algorithme des abeilles')
    plt.legend() 
    plt.show()

plot_path(cities, best_solution)



