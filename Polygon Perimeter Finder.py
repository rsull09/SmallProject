import pandas

def main(file_name):
  # Importing data with pandas
  points=pandas.read_csv(file_name)
  # calculating distance, summing return value
  length = sum(get_distances(points))
  print length


if __name__ == "__main__":
  file_name = sys.argv[1]
  main(file_name)

def get_distances(points):
  # convert a list of points into a list of distances
  distances = []
  # iterating through points, calculating distances
  for i in range(len(points)):
    point = points.loc[i,:]
    # Using modulus to allow distance calculation between last and first points
    next_point = points[(i+1) %(len(points)),:]
    a = point.x - next_point.x
    b = point.y - next_point.y
    c = (a*a + b*b)**(½)
    distances.append(c)
  return distances
