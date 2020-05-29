# How many passengers survived and how many died? (545, 342)
query1 = 'SELECT COUNT("Survived"),"Survived" FROM"Titanic" GROUP BY"Survived"'

# How many passengers were in each class? (1:216, 2:184, 3:487)
query2 = 'SELECT COUNT("Pclass"),"Pclass" FROM"Titanic" GROUP BY"Pclass"'

# How many passengers survived/died within each class? (Died, 1:80, 2:97, 3:368), (Survived, 1:136 , 2:87, 3:119)
query3 = 'SELECT count("Survived"),"Pclass" FROM"Titanic" WHERE"Survived"=0 GROUP BY"Pclass"'
query3_1 = 'SELECT count("Survived"),"Pclass" FROM"Titanic" WHERE"Survived"=1 GROUP BY"Pclass"'

# What was the average age of survivors vs nonsurvivors? (NS: 30.13, SUR: 28.40)
query4 = 'SELECT"Survived",AVG("Age")FROM"Titanic" GROUP BY"Survived"'

# What was the average age of each passenger class? (1:38.7, 2:29.8, 3:25.1)
query5 = 'SELECT AVG("Age"),"Pclass" FROM"Titanic" GROUP BY"Pclass"'

#What was the average fare by passenger class? By survival? (1:84.15, 2:20.66, 3:13.70) (22.20, 48.39)
query6 = 'SELECT AVG("Fare"),"Pclass" FROM"Titanic" GROUP BY"Pclass"'
query6_1 = 'SELECT AVG("Fare"),"Survived" FROM"Titanic" GROUP BY"Survived"'

# How many siblings/spouses aboard on average, by passenger class? By survival? (0.41, 0.40, 0.62)
query7 = 'SELECT AVG("Siblings/Spouses Aboard"),"Pclass" FROM"Titanic" GROUP BY"Pclass"'


