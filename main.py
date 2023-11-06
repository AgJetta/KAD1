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
# for partition, partition_list in column.items():
#     print(f'{partition}: {partition_list}')


#JEŻELI CHCEMY WYŚWIETLAĆ NAZWY GATUNKÓW ZAMIAST CYFEREK:

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

# Oblicz miary rozkładu dla każdej cechy
distribution_measures = numeric_data.describe()

print("\nDistribution measures, deafult")
print(distribution_measures)

# Oblicz miary położenia rozkładu, funkcje
minimum = numeric_data.min()
maximum = numeric_data.max()
mean = numeric_data.mean()
median = numeric_data.median()
lower_quartile = numeric_data.quantile(0.25)
upper_quartile = numeric_data.quantile(0.75)

# Oblicz miarę zróżnicowania rozkładu (odchylenie standardowe)
std_deviation = numeric_data.std()

# Wyświetl wyniki
print("\nMiary położenia rozkładu:\n")
print(f"Minimum:\n{minimum}\n")
print(f"Maksimum:\n{maximum}\n")
print(f"Średnia arytmetyczna:\n{mean}\n")
print(f"Mediana:\n{median}\n")
print(f"Dolny kwartyl (Q1):\n{lower_quartile}\n")
print(f"Górny kwartyl (Q3):\n{upper_quartile}\n")

print("Miarę zróżnicowania rozkładu (odchylenie standardowe):")
print(std_deviation)

#Miary rozkładu, własna implementacja:
def custom_minimum(data):
    return min(data)

def custom_maximum(data):
    return max(data)

def custom_mean(data):
    return sum(data) / len(data)

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
    k = 1 if n % 2 == 1 else 2
    lower_half = sorted_data[:n // 2]
    return custom_median(lower_half)

def custom_upper_quartile(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    k = 1 if n % 2 == 1 else 2
    upper_half = sorted_data[n // 2 + k:]
    return custom_median(upper_half)

def custom_standard_deviation(data):
    # Calculate the standard deviation
    mean = custom_mean(data)
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / len(data)
    std_deviation = (variance) ** 0.5
    return std_deviation



for num, header in enumerate(header_list, 1):

    minimum = custom_minimum(column[num])
    maximum = custom_maximum([num])
    mean = custom_mean([num])
    median = custom_median([num])
    upper_quartile = custom_upper_quartile(column[num])
    lower_quartile = custom_lower_quartile(column[num])
    std_deviation = custom_standard_deviation(column[num])

    print(f"\nData for Column : {num}")
    print(f"Custom Minimum : {minimum}")
    print(f"Custom Maximum : {maximum}")
    print(f"Custom Mean : {mean}")
    print(f"Custom Median : {median}")
    print(f"Custom Upper Quartile : {upper_quartile}")
    print(f"Custom Lower Quartile : {upper_quartile}")
    print(f"Custom Standard Deviation: {std_deviation}")



# Ustaw styl Seaborn (opcjonalne)
sns.set(style="whitegrid")

# # Histogramy dla każdej cechy (łącznie dla wszystkich gatunków)
# plt.figure(figsize=(12, 6))  # Rozmiar wykresu
# for column in data.columns[:-1]:  # Pomijamy ostatnią kolumnę 'species'
#     sns.histplot(data[column], kde=True, label=column)

# # Dodaj etykiety osi i legendę
# plt.xlabel("Wartości cechy")
# plt.ylabel("Liczność")
# plt.legend()
#
# # Wyświetl histogramy
# plt.title("Histogramy ogólne (łącznie dla wszystkich gatunków)")
# plt.show()

# Wykresy pudełkowe z rozróżnieniem na gatunki
plt.figure(figsize=(12, 6))  # Rozmiar wykresu
sns.boxplot(x="species", y="sepal_length", data=data)
plt.title("Wykres pudełkowy dla sepal_length")
plt.show()

plt.figure(figsize=(12, 6))  # Rozmiar wykresu
sns.boxplot(x="species", y="sepal_width", data=data)
plt.title("Wykres pudełkowy dla sepal_width")
plt.show()

plt.figure(figsize=(12, 6))  # Rozmiar wykresu
sns.boxplot(x="species", y="petal_length", data=data)
plt.title("Wykres pudełkowy dla petal_length")
plt.show()

plt.figure(figsize=(12, 6))  # Rozmiar wykresu
sns.boxplot(x="species", y="petal_width", data=data)
plt.title("Wykres pudełkowy dla petal_width")
plt.show()