from pyspark.sql import SparkSession


import random

def generer_liste_triplets(n):
    """
    Génère une liste de triplets (id, value1, value2)

    - id : entier unique de 0 à n
    - value1 : entier entre 0 et 50
    - value2 : entier entre 0 et 5
    """

    ids = list(range(n + 1))          # ids uniques de 0 à n
    random.shuffle(ids)               # mélange pour le côté aléatoire

    triplets = []

    for i in ids:
        value1 = random.randint(0, 50)
        value2 = random.randint(0, 5)
        triplets.append((i, value1, value2))

    return triplets

spark = SparkSession.builder \
    .appName("PySparkHomework") \
    .master("local[*]") \
    .getOrCreate()

data = generer_liste_triplets(100)
df = spark.createDataFrame(data,["id", "value1", "value2"])

df.show()