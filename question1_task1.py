our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#1
intersect = our_routes.intersection(competitor_routes)
print("Destinations that both airlines fly to:",intersect)

#2
diff = our_routes.difference(competitor_routes)
print("Destinations unique to your airline:",diff)

#3
neither = our_routes.symmetric_difference(competitor_routes)
print("Destinations that neither airline shares:",neither)








