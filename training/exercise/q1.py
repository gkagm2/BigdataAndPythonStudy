# 컴퓨터가 몇 대 있고 연산해야할 프로그램도 몇 개 있습니다. 가장 최적화 된 프로그램 대 컴퓨터 분배를
# 수행할 수 있는 프로글매을 작성하세요
# ex) 컴퓨터는 2대가 있고, 프록램의 수행시간은 각 3분, 5,분, 2분이라면, 컴퓨터 하나는 3분, 2분짜리 프로그램을 수행하고
# 다른 컴퓨터는 5분짜리 프로그램을 수행하면 됩니다.


# 입력
# computer : 2
# program: 3, 5, 2

# 출력
# computer1 : 5
# computer2 : 3, 2

# 비유로 변환한 정보:
# 바구니를 준비한다.
# 바구니에 담을 빵들을 크기순으로 정렬한다.
# 빵을 모두 바구니에 담을 때까지 :
#   가장 가벼운 바구니에 가장 큰 빵을 담는다.
# 결과를 돌려준다.
def prog2com(inlist, coms):
    outlist = [] # 바구니(컴퓨터)
    sumout = [] # 바구니 한 개마다 담겨진 빵(수행할 프로그램)의 합계를 갖는 목록
    for x in range(coms): # 초기화
        outlist.append([])
        sumout.append(0)
    inlist.sort()
    inlist.reverse()

    for bread in inlist:
        lowbasket = sumout.index(min(sumout))
        outlist[lowbasket].append(bread)
        sumout[lowbasket] += bread

    return outlist


print(prog2com([2,4,5,1],3))