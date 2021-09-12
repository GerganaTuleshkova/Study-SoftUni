party_size = int(input())
days = int(input())

coins_total = 0

for day in range(1, days +1):
    
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    if day % 3 == 0:
        coins_total -= 3 * party_size
    if day % 5 == 0:
        coins_total += 20 * party_size
        if day % 3 == 0:
            coins_total -= 2 * party_size
    coins_total += 50 - 2 * party_size
print(f"{party_size} companions received {int(coins_total/party_size)} coins each.")