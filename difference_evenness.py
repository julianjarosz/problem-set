def find_different_evenness(n, numbers):
    numbers = list(map(int, numbers.split()))
    
    # Sprawdzenie parzystości dla wszystkich liczb
    even_indices = [i + 1 for i in range(n) if numbers[i] % 2 == 0]  # Indeksy liczb parzystych
    odd_indices = [i + 1 for i in range(n) if numbers[i] % 2 != 0]   # Indeksy liczb nieparzystych
    
    # Wybór indeksu, który się różni parzystościa
    #Jeżeli lista ma dlugosc jeden to znaczy ze znalezlismy typ liczby i jej indeks, bo ona stanowi wyjatek w calej liscie
    if len(even_indices) == 1:
        return even_indices[0]
    else:
        return odd_indices[0]

# Przykład użycia
n = int(input())
numbers = input()
print(find_different_evenness(n, numbers))
