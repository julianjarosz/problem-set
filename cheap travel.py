# https://codeforces.com/problemset/problem/466/A
# n - num rides planned
# m - num rides covered by ticket
# a - price of one ticket
# b - price of m ticket

def min_travel_cost(text_input):
    n, m, a, b = list(map(int, text_input.split()))
    # Cost if using only single-ride tickets
    cost_single = n * a

    # Cost if using only m-ride tickets (and any extra rides covered with single tickets)
    full_m_tickets = n // m  # Number of full m-tickets needed
    remaining_rides = n % m   # Remaining rides after using m-tickets
    
    cost_m_only = full_m_tickets * b + remaining_rides * a  # Using m-tickets and remaining single rides
    cost_full_m_only = (full_m_tickets + 1) * b  # Using one more m-ticket to cover all rides

    # Find the minimum cost
    return min(cost_single, cost_m_only, cost_full_m_only)


print(min_travel_cost(input()))
