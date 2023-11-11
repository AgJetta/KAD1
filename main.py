import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'data.csv'

column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Load your dataset from a CSV file and specify the column names
data = pd.read_csv(file_path, names=column_names)
# print(data)

# lista headerow
header_list = data.columns.tolist()
# print('header list check:')
# print(header_list)

# jeżeli chcemy przechowywać dane w formie list
column = {}
# Loop through each header with its position
for num, header in enumerate(header_list, 1):
    # partycja przechowuje dane w formie listy
    partition = data[header].tolist()
    column[num] = partition

# Print the lists for each enumerated partition, check
#    for partition, partition_list in column.items():
#     print(f'{partition}: {partition_list}')


# JEŻELI CHCEMY WYŚWIETLAĆ NAZWY GATUNKÓW ZAMIAST CYFEREK:

# Definiuj mapowanie liczb na nazwy gatunków
species_mapping = {0: "setosa", 1: "versicolor", 2: "virginica"}

# Zmień wartości w kolumnie 'species' na odpowiadające im nazwy gatunków
data['species'] = data['species'].map(species_mapping)

counts = data['species'].value_counts()

# Oblicz udziały procentowe
percentages = (counts / counts.sum()) * 100


# Wyświetl wyniki
print("\nLiczności poszczególnych gatunków:")
print(counts)
print("\nUdziały procentowe poszczególnych gatunków:")
print(percentages)

# Wybierz tylko cechy numeryczne (bez kolumny 'species')
numeric_data = data.drop(columns=['species'])


# Obliczanie miar rozkładu dla każdej cechy za pomocą funkcji describe
distribution_measures = numeric_data.describe()

print("\nDistribution measures, deafult")
print(distribution_measures)

# Obliczanie miar położenia rozkładu, podstawowe python funkcje
minimum = numeric_data.min()
maximum = numeric_data.max()
mean = numeric_data.mean()
median = numeric_data.median()
lower_quartile = numeric_data.quantile(0.25)
upper_quartile = numeric_data.quantile(0.75)

# Oblicz miarę zróżnicowania rozkładu (odchylenie standardowe)
std_deviation = numeric_data.std()

# Wyświetlanie wyników wyniki
print("\nMiary położenia rozkładu:\n")
print(f"Minimum:\n{minimum}\n")
print(f"Maksimum:\n{maximum}\n")
print(f"Średnia arytmetyczna:\n{mean}\n")
print(f"Mediana:\n{median}\n")
print(f"Dolny kwartyl (Q1):\n{lower_quartile}\n")
print(f"Górny kwartyl (Q3):\n{upper_quartile}\n")
print("Miarę zróżnicowania rozkładu (odchylenie standardowe):")
print(std_deviation)


# Miary rozkładu, własna implementacja:

def custom_sum(data):
    sum = 0
    for value in data:
        sum += value
    return sum


def custom_minimum(data):
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum


def custom_maximum(data):
    maximum = data[0]
    for element in data[1:]:
        if element > maximum:
            maximum = element
    return maximum


def custom_mean(data):
    return custom_sum(data) / len(data)


def custom_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[(n - 1) // 2]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2


def custom_lower_quartile(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    k = 0 if n % 2 == 1 else 1
    lower_half = sorted_data[:n // 2 - k]
    return custom_median(lower_half)


def custom_upper_quartile(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    k = 0 if n % 2 == 1 else 1
    upper_half = sorted_data[n // 2 + k:]
    return custom_median(upper_half)


def custom_standard_deviation(data):
    # Calculate the standard deviation
    mean = custom_mean(data)
    deviations = [(x - mean) ** 2 for x in data]
    variance = custom_sum(deviations) / len(data)
    std_deviation = (variance) ** 0.5
    return std_deviation

# Wyświetlanie wyników wyniki

for num, header in enumerate(header_list[:-1], 1):
    minimum = custom_minimum(column[num])
    maximum = custom_maximum(column[num])
    mean = custom_mean(column[num])
    median = custom_median(column[num])
    upper_quartile = custom_upper_quartile(column[num])
    lower_quartile = custom_lower_quartile(column[num])
    std_deviation = custom_standard_deviation(column[num])

    print(f"\nData for Column : {num}")
    print(f"Custom Minimum : {minimum}")
    print(f"Custom Maximum : {maximum}")
    print(f"Custom Mean : {mean}")
    print(f"Custom Median : {median}")
    print(f"Custom Upper Quartile : {upper_quartile}")
    print(f"Custom Lower Quartile : {lower_quartile}")
    print(f"Custom Standard Deviation: {std_deviation}")



# # # WYKRESY # # #
# Single histogram for sepal_length without facet
sns.histplot(data=data, x="sepal_length", kde=False, color="skyblue", label="sepal_length")
plt.title("Długość działki kielicha", fontweight="bold")
plt.ylabel("Liczebność", fontweight="bold")  # Zmiana etykiety na osi y
plt.xlabel("Długość (cm)", fontweight="bold")  # Zmiana etykiety na osi x
plt.show()

# Single histogram for sepal_width without facet
sns.histplot(data=data, x="sepal_width", kde=False, color="skyblue", label="sepal_width")
plt.title("Szerokość działki kielicha", fontweight="bold")
plt.ylabel("Liczebność", fontweight="bold")  # Zmiana etykiety na osi y
plt.xlabel("Szerokość (cm)", fontweight="bold")  # Zmiana etykiety na osi x
plt.show()

# Single histogram for petal_length without facet
sns.histplot(data=data, x="petal_length", kde=False, color="skyblue", label="petal_length")
plt.title("Długość płatka", fontweight="bold")
plt.ylabel("Liczebność", fontweight="bold")  # Zmiana etykiety na osi y
plt.xlabel("Długość (cm)", fontweight="bold")  # Zmiana etykiety na osi x
plt.show()

# Single histogram for petal_width without facet
sns.histplot(data=data, x="petal_width", kde=False, color="skyblue", label="petal_width")
plt.title("Szerokość płatka", fontweight="bold")
plt.ylabel("Liczebność", fontweight="bold")  # Zmiana etykiety na osi y
plt.xlabel("Szerokość (cm)", fontweight="bold")  # Zmiana etykiety na osi x
plt.show()

# Wykres pudełkowy dla sepal_length
plt.figure(figsize=(8, 6))
sns.boxplot(x=data["species"], y=data["sepal_length"], width=0.3, showfliers=True, boxprops=dict(alpha=0.6))
plt.ylabel("Długość (cm)", fontweight="bold")
plt.xlabel("Gatunek", fontweight="bold")
plt.show()

# Wykres pudełkowy dla sepal_width
plt.figure(figsize=(8, 6))
sns.boxplot(x=data["species"], y=data["sepal_width"], width=0.3, showfliers=True, boxprops=dict(alpha=0.6))
plt.ylabel("Szerokość (cm)", fontweight="bold")
plt.xlabel("Gatunek", fontweight="bold")
plt.show()

# Wykres pudełkowy dla petal_length
plt.figure(figsize=(8, 6))
sns.boxplot(x=data["species"], y=data["petal_length"], width=0.3, showfliers=True, boxprops=dict(alpha=0.6))
plt.ylabel("Długość (cm)", fontweight="bold")
plt.xlabel("Gatunek", fontweight="bold")
plt.show()

# Wykres pudełkowy dla petal_width
plt.figure(figsize=(8, 6))
sns.boxplot(x=data["species"], y=data["petal_width"], width=0.3, showfliers=True, boxprops=dict(alpha=0.6))
plt.ylabel("Szerokość (cm)", fontweight="bold")
plt.xlabel("Gatunek", fontweight="bold")
plt.show()
