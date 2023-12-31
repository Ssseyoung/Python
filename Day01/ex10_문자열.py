# 형식을 갖춘 문자열
# %
# %d        : 정수(10진수)
# %o        : 정수(8진수)
# %x        : 정수(16진수)
# %f        : 실수
# %s        : 문자열

a = 10
b = 20
print('%d' % 10)            # 10
print('%o' % 10)            # 12
print('%x' % 10)            # a
print('%f' % 3.14)          # 3.140000
print('%s' % 'Python')      # Python
print('%d %d' % (a, b))     # 10 20

# 문자열 형식문자는 %s 로, 정수, 실수 모두 처리 가능
print('%s' % 100)           # 100
print('%s' % 3.14)          # 3.14