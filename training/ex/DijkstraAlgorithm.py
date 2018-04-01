# Dijkstra algorithm
startvertice = 0
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
preList= [startvertice for i in range(MAX_VERTICES)]

# 최소 weight를 찾기.
def choose(distance, n, found):
    min = MAX # min을 무한대로 초기화
    minpos = -1 # 최소 포지션을 -1로 설정
    for i in range(0,n): # 노드 개수까지 돌린다.

        if distance[i] < min and not found[i]: # 거리의 가중치가 최소 값보다 작고, 아직 찾지 않았다면
            min = distance[i] # 최소 값을 min에 넣는다.
            minpos = i #최소값이나온 노드를 minpo에 넣는다.
    return minpos # 그 노드 return한다.

def shortest_path(start, n):

    for i in range(0,n): # 초기화
        distance[i] = weight[start][i]
        found[i] = False
    found[start] = True # 시작 정점 방문

    flag = 0

    distance[start] = 0
    for i in range(0, n-2):
        u = choose(distance, n, found)
        found[u] = True # u의 정점 방문

        if flag == 0:
            preList[u] = start
            flag = 1
        for w in range(0,n): # 최대 정점의 개수까지 돌린다.

            if not found[w]: #found[w]가 true이면서
                if distance[u] + weight[u][w] < distance[w]: # 방문했었던 u의 가중치와 현재 u에서 w 까지의 거리를 더한 값이 이전의 가중치보다 작으면
                    distance[w] = distance[u] + weight[u][w] #
                    preList[w] = u #방문했던 u의 정점을 preList에 넣는다.



def main():

    shortest_path(startvertice, MAX_VERTICES)

    for i in range(MAX_VERTICES):
        if startvertice != i:
            print(startvertice,"에서 ,",i,"까지의 경로")
            m = i
            print(m,end="<-")
            while True:
                if preList[m] != startvertice : # 같은 경로가 아니면
                    print(preList[m],end="<-")
                    m = preList[m]
                else:
                    break
            print(startvertice)

            print("최단거리는 : ", distance[i])
            print("")






    #shortest_path(0,"mygaph.txt") # file

    # try:
    #     path = input("파일 이름을 입력하세요:")
    #     fileName = open(path, "r")
    # except IOError:
    #     print("파일이 존재하지 않습니다")
    # else:
    #     print("파일이 존재합니다.")
    #
    # for i in weight:
    #     print(i)


    # count =0
    # for i in found:
    #     print("found ",count, " is " , found[i])
    #     count += 1



main()