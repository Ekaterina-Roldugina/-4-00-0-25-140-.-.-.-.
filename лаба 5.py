import time

def calculate_taxi_fare(distance_km):
 base_fare = 4.00
 rate_per_meter = 0.25 / 140 # Convert rate to per meter
 distance_m = distance_km * 1000 # Convert distance to meters
 fare = base_fare + (rate_per_meter * distance_m)
 return fare

def taxi_fare_decorator(func):
 def wrapper(distance_km):
 start_time = time.time()
 result = func(distance_km)
 end_time = time.time()
 execution_time = end_time - start_time
 print(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
 print(f"Distance: {distance_km} km")
 print(f"Total Fare: ${result:.2f}")
 print(f"Execution Time: {execution_time:.6f} seconds")
 return wrapper

@taxi_fare_decorator
def calculate_and_display_taxi_fare(distance_km):
 return calculate_taxi_fare(distance_km)

# Example usage
calculate_and_display_taxi_fare(5.5)
