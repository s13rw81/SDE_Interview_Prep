def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    K = year % 100
    J = year // 100

    # Zeller's Congruence formula
    h = (day + (13 * (month + 1) // 5) + K + (K // 4) + (J // 4) - 2 * J) % 7

    # Adjust result to match ISO weekday representation (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
    return (h + 5) % 7

# Example usage:
day = 4
month = 8
year = 2024

day_names = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

day_of_week = zellers_congruence(day, month, year)
print(f"The day of the week for {year}-{month:02d}-{day:02d} is {day_names[day_of_week]}.")