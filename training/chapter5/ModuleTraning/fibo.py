

def fib(n): # 피보나치 수열을 화면에 출력한다.
    a, b = 0, 1
    while b < n:
        print( b, end =' ')
        a, b = b, a + b
    print()



# 모듈을 스크립트로 실행하기. cmd 창에 python fibo.py <arguments> 형식으로 입력하면 프롬프트 창에 출력 됨.
if __name__ == "__main__": # 직접 이 파일을 실행시키면 if문은 True가 됨.  다른 파일에서 모듈을 불러서 사용할 때는 False가 됨
    import sys
    fib(int(sys.argv[1]))