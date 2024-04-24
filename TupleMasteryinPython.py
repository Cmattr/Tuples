flight_info = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def flight_list(flight_info):
    for info, (name, leaving, arriving) in enumerate(flight_info, start=1 ):
        print(f"itinerery {info}: {name} - From {leaving} to {arriving}")

flight_list(flight_info)

