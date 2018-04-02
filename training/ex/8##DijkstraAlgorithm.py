from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


# Dijkstra algorithm
START_VERTICE= 0
INF = 1000
MAX_VERTICES = 7
max_vertices = 0

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






# 최소 weight를 찾기.
def choose(distance, n, found):
    min = MAX # min을 무한대로 초기화
    minpos = -1 # 최소 포지션을 -1로 설정
    for i in range(0,n): # 노드 개수까지 돌린다.

        if distance[i] < min and not found[i]: # 거리의 가중치가 최소 값보다 작고, 아직 찾지 않았다면
            min = distance[i] # 최소 값을 min에 넣는다.
            minpos = i #최소값이나온 노드를 minpo에 넣는다.
    return minpos # 그 노드 return한다.

def shortest_path(start, n, preList):
    try:
        if start < 0:
            print("vertice가 존재하기 않습니다.")
            exit()
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
    except IndexError:
        print("vertice가 존재가지 않습니다.")
        exit()

def print_shortest_path(startvertice, maxVertices, preList):

    for i in range(maxVertices):
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



def main():

    choice = input("예제 출력 : 1, 파일 입력 : 2 ")
    if int(choice) is 1:
        preList = [START_VERTICE for i in range(MAX_VERTICES)]
        shortest_path(START_VERTICE, MAX_VERTICES, preList)
        print_shortest_path(START_VERTICE,MAX_VERTICES, preList)
    elif int(choice) is 2:

        try:
            readFile = askopenfilename()
            if readFile != None:
                file = open(readFile, "r", encoding="utf-8")  # filename을 readFile로 바꿈
            # filename = input("파일 이름을 입력하시오:")

        except IOError:
            print("파일이 존재하지 않습니다.")
        else:
            startvertice = int(input("시작 vertice를 입력하세요 :"))
            flag = 0
            weight2 = []
            preList = [startvertice for i in range(MAX_VERTICES)]
            for line in file:
                if flag == 0:
                    max_vertices = int(line)
                    if startvertice >= max_vertices and startvertice < 0:
                        print("vertice가 존재하지 않습니다.")
                        file.close()
                        exit()
                        break
                    flag += 1

                r = line.rstrip()
                word_list=r.split(', ')
                weight2 += [word_list]

            file.close()

            shortest_path(startvertice, max_vertices, preList)
            print_shortest_path(startvertice,max_vertices, preList)

    else:
        print("잘못 입력하셨습니다.")


main()