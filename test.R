mutation_rate <- 0.002  # Petit taux de mutation

for (gen in 1:generations) {
  # Sélection naturelle
  nb_typica_survivors <- rbinom(1, round(population_size * freq_typica), survival_typica)
  nb_carbonaria_survivors <- rbinom(1, round(population_size * freq_carbonaria), survival_carbonaria)
  
  total_survivors <- nb_typica_survivors + nb_carbonaria_survivors
  if (total_survivors == 0) break  # Éviter une division par zéro
  
  # Mise à jour des fréquences après sélection
  freq_typica <- nb_typica_survivors / total_survivors
  freq_carbonaria <- nb_carbonaria_survivors / total_survivors
  
  # Appliquer le taux de mutation
  freq_typica <- max(0, freq_typica - mutation_rate) + mutation_rate * freq_carbonaria
  freq_carbonaria <- max(0, freq_carbonaria - mutation_rate) + mutation_rate * freq_typica
  
  # Reproduction avec probabilité basée sur les effectifs restants
  next_generation <- sample(c("typica", "carbonaria"), population_size, replace = TRUE, prob = c(freq_typica, freq_carbonaria))
  
  # Mise à jour des fréquences pour la prochaine génération
  freq_typica <- sum(next_generation == "typica") / population_size
  freq_carbonaria <- sum(next_generation == "carbonaria") / population_size
  
  # Enregistrement des résultats
  results[gen, "freq_typica"] <- freq_typica
  results[gen, "freq_carbonaria"] <- freq_carbonaria
}
