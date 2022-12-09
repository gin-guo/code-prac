# As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable, before using more computationally intensive procedures for finding the optimal route.
#
# The roads on the map are rasterized and produce a matrix of boolean values - True if the road is present or False if it is not. The roads in the matrix are connected only if the road is immediately left, right, below or above it.
#
# Finish the route_exists method so that it returns True if the destination is reachable or False if it is not. The from_row and from_column parameters are the starting row and column in the map_matrix. The to_row and to_column are the destination row and column in the map_matrix. The map_matrix parameter is the above mentioned matrix produced from the map.
#
# For example, for the given rasterized map, the code below should return True since the destination is reachable:
#
# map_matrix = [
#     [True, False, False],
#     [True, True, False],
#     [False, True, True]
# ];
#
# route_exists(0, 0, 2, 2, map_matrix)

def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    visited = [[False for i in range(len(map_matrix[0]))] for j in range(len(map_matrix))]

    def route_exists2(from_row, from_column, to_row, to_column, map_matrix):
        if (from_row < 0 or
            from_row >= len(map_matrix) or
            from_column < 0 or
            from_column >= len(map_matrix[0]) or
            visited[from_row][from_column] == True):
            return False

        if map_matrix[from_row][from_column]:
            visited[from_row][from_column] = True
            if (from_row == to_row and from_column == to_column):
                return True
            return (route_exists2(from_row-1, from_column, to_row, to_column, map_matrix) or
                    route_exists2(from_row, from_column-1, to_row, to_column, map_matrix) or
                    route_exists2(from_row, from_column+1, to_row, to_column, map_matrix) or
                    route_exists2(from_row+1, from_column, to_row, to_column, map_matrix))

    if route_exists2(from_row, from_column, to_row, to_column, map_matrix):
        return True
    else:
        return False


# def route_exists(start_x, start_y, end_x, end_y, map_matrix):
#     cur_routes = [[start_x, start_y]]
#     num_new_routes = 0
#
#     while True:
#         num_routes = len(cur_routes)
#         for route in cur_routes[-num_new_routes:]:
#             # check only the active new rotes and their possible roads
#             for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
#                 road_x = route[0] + x
#                 road_y = route[1] + y
#
#                 # check if there exist any (new) paths connected to current road
#                 try:
#                     if map_matrix[road_x][road_y]:          # the road exists
#                         if [road_x, road_y] not in route:   # new path
#                             new_route = [road_x, road_y]
#                             if new_route not in cur_routes:
#                                 cur_routes.append(new_route)
#                 except:
#                     pass
#
#         num_new_routes = len(cur_routes) - num_routes
#         if num_new_routes == 0:
#             break
#
#     if [end_x, end_y] in cur_routes:
#         return True
#     else:
#         return False


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))