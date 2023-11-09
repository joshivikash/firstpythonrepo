def group_by_city(scores_dataset):
  """
  Group students by cities
  
  Argument:
      scores_dataset: list of dicts
  Return:
      cities: dict: (key: string, value: list of strings)
  """
  cities = {}
  for data in scores_dataset:
    city = data['City']
    if city not in cities:
      cities[city] = []
    cities[city].append(data['Name'])
  return cities

def busy_cities(scores_dataset):
  """
  Get the busy cities
  
  Argument:
      scores_dataset: list of dicts
  Return:
      result: list of strings
  """
  cities = group_by_city(scores_dataset)
  result = []
  population = 0
  for city, names in cities.items():
    if len(names) > population:
      result = [city]
      population = len(names)
    elif len(names) == population:
      result.append(city)
  return result