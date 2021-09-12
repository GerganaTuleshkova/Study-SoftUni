import re

pattern = r"(?P<surrounding>[\=|\/])(?P<location>[A-Z][a-zA-Z]{2,})(?P=surrounding)"
valid_destinations = []
travel_points = 0
text = input()

destinations_found_iter = re.finditer(pattern, text)
for destination_match in destinations_found_iter:
    destination_name = destination_match.group("location")
    valid_destinations.append(destination_name)
    travel_points += len(destination_name)

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")

