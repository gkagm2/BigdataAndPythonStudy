'''
o 수행단위: 팀/개인 단위
 - 홍종화, 김태경

o 데이터 선정 및 수집
 - 총 데이터 건수: 86874 rows x 30 columns
 - 데이터 출처 후보 : 공공데이터 포털의 2013년 서울1~4호선 지하철 승하차 인원 통계

o 분석
 - 분석 종류: 각각 3건 이상 (총 6건)
 - 분석 프로그램: 인라인 코멘트 필수 (블록단위 코멘트 요망)
 - 분석 결과: 테이블, 그래프

o 분석 보고서
 1) 포함 내용
 - 데이터 출처
 - 데이터 가공
   . 수가공 내용
   . 프로그램 가공 내용
   . 원본 vs 수정된 데이터 파일의 헤더 비교
 - 분석 포함 내용: (3종류 각각)
   . 분석 설명: 분석 목적, 분석내용을 자유롭게 설명
   . 분석 결과 테이블
   . 분석 결과 그래프 차트
   . 분석 결과 의미 설명
 2) 자료 형식: PPT 10~15장 내외

o 제출 항목
 - 데이터 파일: 원본, 수정후 구분한 파일
 - 데이터 수집(있을 경우), 가공 프로그램
 - 데이터 분석 프로그램
 - 분석보고서

o 채점 기준
 - 데이터 수집 및 가공의 난이도 및 결과: 20%
 - 데이터 분석의 유효성, 난아도 및 분석결과 평가: 20%/종 x 3종 =60%
 - 분석 보고서: 20%
 - 지연 제출 감점: 30% (받은 점수의 30%  감점)

'''

import matplotlib.pyplot as plt
from matplotlib import font_manager
from pandas import Series, DataFrame
import pandas as pd

# figure 사이즈 설정 
plt.rc('figure', figsize=(18, 9))
# 그래프 출력시 한글깨짐 해결
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)
# 시리즈나 데이터프레임을 콘솔창에 출력할시 보여주는 행 최대개수
pd.options.display.max_rows = 500
pd.options.display.max_columns = 17
pd.set_option('display.width', 320)
# 인덱스슬라이서 사용
idx = pd.IndexSlice


'''
데이터 전처리
- 불필요 데이터, 공백 제거
- 원활한 분석과정을 위해
'''
def dataPreparation():
    # csv파일 불러오기 ( 86874rows x 30columns )
    df = pd.read_csv('2013.csv', encoding='CP949')
    # 2013년 당시 5호선은 미완공, 데이터 없음으로 df에서 제거
    df = df.loc[df['호선'] != '5호선', :]
    # 역이름들 중에 공백있는 이름 있어서 공백 제거
    df['역명'] = df['역명'].apply(lambda x: x.replace(' ', ''))

    return df


'''
데이터분석 1
- 2013년 호선별 총 이용객 비율 그래프
- 전체 호선(1~4호선) 월별 총 이용객 그래프
'''
def analysisSet1(df):
    # 00~01부터 23~24 시까지 모든 이용객수 더하기
    data1 = df.iloc[:, 6:].sum(axis=1)
    # 월과 호선별로 그룹화한 뒤 더하기 >> 월,호선별 이용객 수 도출
    data2 = data1.groupby([df['월'], df['호선']]).sum()
    # 직관적인 데이터 시각화 위해 월을 컬럼으로
    data3 = data2.unstack(0); print(data3)

    fig = plt.figure()
    axes = []
    for i in range(2):
        axes.append(fig.add_subplot(1, 2, i + 1))
        if i==0:
            data3.T.plot(ax=axes[i])
            axes[i].set_title('1~4 호선 월별 총 이용객 수')
            axes[i].set_xlabel('월')
            axes[i].set_ylabel('이용객 수\n(단위 : 1억 명)')
        else:
            data3.mean(axis=1).plot(kind='pie', ax=axes[i])
            axes[i].set_title('2013년 호선별 총 이용객 비율')
            axes[i].set_xlabel('')
            axes[i].set_ylabel('')
            axes[i].legend()
    plt.show()


'''
데이터분석 2
- 전체 호선(1~4호선) 역,월별 이용객 비율 누적막대그래프 
>> 분기별로 바꾸자? 아니면 연별로
>> 얘는 (~~)이거 없애도 되겟다
'''
def analysisSet2(df):
    # 00~01부터 23~24 시까지 모든 이용객수 더하기
    data1 = df.iloc[:, 6:].sum(axis=1)
    # 월,호선,역명으로 그룹화한 뒤 더하기 >> 월,호선,역별 이용객 수 도출
    data2 = data1.groupby([df['월'], df['호선'], df['역명']], sort=False).sum()
    # 직관적인 데이터 시각화 위해 월을 컬럼으로
    data3 = data2.unstack(0); print(data3)

    sname = data3.index.get_level_values(0).unique()
    for i,d in enumerate(sname):
        data3.loc[d].T.plot(kind='barh', stacked=True)
        plt.title(d + ' 역,월별 총 이용객 비율')
        plt.xlabel('이용객 수\n(단위 : 1천만 명)')
        plt.ylabel('월')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.show()


'''
데이터분석 3
- 전체 호선(1~4호선)별 총 이용객 수 TOP5
'''
def analysisSet3(df):
    # 00~01부터 23~24 시까지 모든 이용객수 더하기
    data1 = df.iloc[:, 6:].sum(axis=1)
    # 호선,역,구분(승,하차)으로 그룹화한 뒤 더하기 >> 호선,역,구분(승,하차) 별 이용객 수 도출
    data2 = data1.groupby([df['호선'], df['역명'], df['구분']], sort=False).sum()
    # 직관적인 데이터 시각화 위해 구분(승,하차)을 컬럼으로
    data3 = data2.unstack(2)
    # 승하차 인원 합 열을 추가
    data4 = pd.concat([data3, data3.sum(axis=1)], axis=1).rename(columns={0:'승하차 합'}); print(data4)

    sname = data4.index.get_level_values(0).unique()
    for i, d in enumerate(sname):
        print(data4.loc[d].sort_values(by='승하차 합')[['승차','하차']].tail())
        data4.loc[d].sort_values(by='승하차 합')[['승차','하차']].tail().plot(kind='bar', stacked=True)
        plt.title(d+' 총 이용객 수 TOP5 승하차 비율')
        plt.ylabel('이용객 수\n(단위 : 1천만 명)')
        plt.show()


'''
데이터분석 4
- 전체 호선(1~4호선) 이용시간대별 이용객 수 평균
'''
def analysisSet4(df):
    # 00~01부터 23~24 시까지 모든 이용객수 구하기
    data1 = df.iloc[:, 6:]
    # 호선별로 그룹화한뒤 평균 구하기 >> 1~4호선 이용시간대별 평균 도출
    data2 = data1.groupby(df['호선'], sort=False).mean().sort_index(axis=1, ascending=False); print(data2)

    sname = data2.index.get_level_values(0).unique()
    for i, d in enumerate(sname):
        data2.loc[d].plot(kind='barh', color='b')
        plt.title('2013년 '+d+' 이용시간대별 이용객 수 평균')
        plt.ylabel('이용시간대')
        plt.xlabel('이용객 수\n(단위 : 1 명)')
        plt.show()


'''
데이터분석 5
- 전체 호선중 평일 출퇴근 시간대 승하차 비율 계산해서 비율 높은 곳을 탑 5
>> 출근시간대(08~09)에 하차비율 높은곳이 직장밀집구역, 승차비율 높은곳이 거주밀집구역
>> 퇴근시간대(18~19)에 하차비율 높은곳이 거주밀집구역, 승차비율 높은곳이 직장밀집구역
'''
def analysisSet5(df):
    # 평일인 요일들만 구해서 저장
    data1 = df[df['요일'].isin(list('월화수목금'))]
    # 이용시간대 중 출퇴근 시간대(08~09, 18~19)만 구해서 저장
    data2 = data1[['08~09', '18~19']]
    # 역명,구분(승,하차)로 그룹화한뒤 평균 구하기 >> 전체 역 승하차 이용객 평균 도출
    data3 = data2.groupby([df['역명'], df['구분']], sort=False).mean()
    # 직관적인 데이터 시각화 위해 인덱스와 컬럼을 조정
    data4 = data3.unstack(1).stack(0)
    # 총 이용객 수를 기반으로 승하차의 비율을 구함
    data5 = data4.div(data4.sum(1), axis=0); print(data5)

    fig = plt.figure()

    sname = data5.index.get_level_values(1).unique()
    axes = []
    for i, d in enumerate(sname):
        axes.append(fig.add_subplot(1, 2, i + 1))
        data5.loc[idx[:, d], :].sort_values(by='하차', ascending=True).tail(10).plot(kind='bar', stacked=True, ax=axes[i])
        if i==0:
            axes[i].set_title('출근 시간대(08~09)')
            axes[i].set_xlabel('')
        else:
            axes[i].set_title('퇴근 시간대(08~09)')
            axes[i].set_xlabel('')
        axes[i].set_ylabel('백분율')
        axes[i].set_ylim([0.0,0.4])
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.23, right=None, top=0.9)
    plt.suptitle('평일 출퇴근 시간대별 이용객 승하차 비율 TOP5')
    plt.show()


'''
데이터분석 6
- 전체 호선중 주말.공휴일 이용객 가장 많은 역 탑5
>> 분명 휴일에 붐비는 역이 있음, 얘는 비율로 계산하면 안됨
'''
def analysisSet6(df):
    # 주말,공휴일인 요일들만 구해서 저장
    data1 = df[df['요일'].isin(list('공토일'))]
    # 00~01부터 23~24 시까지 모든 이용객수 더하기
    data2 = data1.iloc[:, 6:].sum(axis=1)
    # 역명으로 그룹화한뒤 더함 >> 주말,공휴일에 가장 많은 이용객수를 가진 역을 도출
    data3 = data2.groupby([df['역명']], sort=False).sum()
    # 이용객수를 이용해 정렬한뒤 탑5 선정
    data4 = data3.sort_values().tail(); print(data4)

    data4.plot(kind='bar', stacked=True)
    plt.title('주말,공휴일 이용객 수 TOP5 역')
    plt.ylabel('이용객 수\n(단위 : 1천만 명)')
    plt.xlabel('')
    plt.tight_layout()
    plt.show()


# 데이터 전처리 과정
dataFrame = dataPreparation()

# 2012151014 김태경 제출자의 데이터분석구조
analysisSet1(dataFrame)
analysisSet4(dataFrame)
analysisSet6(dataFrame)

# 홍종화 팀원의 데이터분석구조
# analysisSet2(dataFrame)
# analysisSet3(dataFrame)
# analysisSet5(dataFrame)
# 원본 csv파일!
# print(dataFrame)