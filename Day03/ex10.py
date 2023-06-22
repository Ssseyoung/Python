'''
    파일 입출력
    
    - 텍스트 파일에 추가하기
    
'''

# 파일 저장 경로
path = 'C:/LSY/Python/Day03/'

# 파일 열기
# rt : 읽기모드, 텍스트 파일
file = open(path + 'hello.txt', 'rt', encoding='UTF-8')

while True:
    str = file.readline()       # 파일로부터 한 줄 씩 읽어온다
    if not str:
        break
    print(str, end='')