users = [{"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "Clive"},
         {"id": 6, "name": "Hicks"},
         {"id": 7, "name": "Devin"},
         {"id": 8, "name": "Kate"},
         {"id": 9, "name": "Klein"}]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i

def amizades (friendships, users):

    listAmizade = []
    for x,y in friendships:
        for name in users:

            if name["id"] == x:
                for nameY in users:
                    if nameY["id"] == y:
                        amigos= {"amigos": [name["name"], nameY["name"]]}
                listAmizade.append(amigos)

            elif name["id"] == y:
                for nameY in users:
                    if nameY["id"] == x:
                       amigos= {"amigos": [name["name"], nameY["name"]]}
                listAmizade.append(amigos)
            
    return listAmizade



final = amizades(friendships, users)
print(final)



