# Dijkstra algorithm
INF = 1000
MAX_VERTICES = 7
MAX = 2147483647
distance = [0 for i in range(MAX_VERTICES)] # distance = []
found = [0 for i in range(MAX_VERTICES)]
weight = [[0,7, INF, INF, 3, 10, INF],
          [7, 0, 4, 10, 2, 6, INF],
          [INF, 4, 0, 2, INF, INF, INF],
          [INF, 10, 2, 0, 11, 9, 4],
          [3, 2, INF, 11, 0, INF, 5],
          [10, 6, INF, 9, INF, 0, INF],
          [INF, INF, INF, 4, 5, INF, 0]]

def choose(distance, n, found):
    min = MAX
    minpos = -1
    for i in range(0,n):
        if distance[i] < min and not found[i]:
            min = distance[i]
            minpos = i
    return minpos

def shortest_path(start, n):
    for i in range(0,n): # 초기화
        distance[i] = weight[start][i]
        found[i] = False
    found[start] = True # 시작 정점 방문
    distance[start] = 0
    for i in range(0, n-2):
        u = choose(distance, n, found)
        found[u] = True
        for w in range(0,n):
            if not found[w]:
                if distance[u] + weight[u][w] < distance[w]:
                    distance[w] = distance[u] + weight[u][w]

def main():
    shortest_path(0, MAX_VERTICES)

    #shortest_path(0,"mygaph.txt") # file

    try:
        path = input("파일 이름을 입력하세요:")
        fileName = open(path, "r")
    except IOError:
        print("파일이 존재하지 않습니다")
    else:
        print("파일이 존재합니다.")

    for i in weight:
        print(i)


    print(found)
    departure= 0
    destination =3
    print("[", departure, "->" , destination, "]")
main()