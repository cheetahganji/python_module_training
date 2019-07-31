"""collections 모듈 실습

공식 문서 : 
"""
import collections

if __name__ == "__main__":
    ls = ['김', '이', '박', '강', '김', '강', '이']

    # 리스트를 넣으면, 요소별로 counting
    print(collections.Counter(ls))      # Counter({'김': 2, '이': 2, '강': 2, '박': 1})
    
    # 딕셔너리를 넣으면, value가 큰 것 부터 정렬하여 딕셔너리 리턴
    print(collections.Counter({'a':2, 'b':4, 'c':3}))      # Counter({'b': 4, 'c': 3, 'a': 2})
    print(collections.Counter({'a':2, 'b':'a', 'c':3}))    # value에 숫자가 아닌게 들어있으면 정렬이 안되넹
    
    c = collections.Counter(a=1, b=2,c=3)
    print(c)    # Counter({'c': 3, 'b': 2, 'a': 1})
    print(sorted(c.elements())) # ['a', 'b', 'b', 'c', 'c', 'c']

    c = collections.Counter()
    c.update('abc') 
    print(c)    # Counter({'a': 1, 'b': 1, 'c': 1})

    c.update('aaaaaa')
    print(c)    # Counter({'a': 7, 'b': 1, 'c': 1})

    for k, v in c.items():      # key와 value를 함꼐 다룰 수 있다.
        print('key:{}, vlaue:{}'.format(k,v))       # key:a, vlaue:7 ... key:b, vlaue:1 ...

    c = collections.Counter('KIM Wanyoung')
    print(c.elements()) #<itertools.chain object at 0x1079b2750>
    print(list(c.elements()))   # ['K', 'I', 'M', ' ', 'W', 'a', 'n', 'n', 'y', 'o', 'u', 'g']
    print(sorted(c.elements())) # [' ', 'I', 'K', 'M', 'W', 'a', 'g', 'n', 'n', 'o', 'u', 'y']

    c = collections.Counter('skt, kt')
    # (요소, 개수)의 튜플 형태를 리스트로 리턴
    print(c.most_common())      # [('k', 2), ('t', 2), ('s', 1), (',', 1), (' ', 1)]
    # 갯수가 가장 많은 것 상위 n개만
    print(c.most_common(2))     # [('k', 2), ('t', 2)]

    # 각 요소별로 개수를 뺀다
    subtract1 = collections.Counter('i love you')
    subtract2 = collections.Counter('you love me?')
    subtract1.subtract(subtract2)
    print(subtract1)    # Counter({'i': 1, ' ': 0, 'l': 0, 'o': 0, 'v': 0, 'y': 0, 'u': 0, 'e': -1, 'm': -1, '?': -1})

    # 더하기, 빼기 연산
    add1 = collections.Counter('aab')
    add2 = collections.Counter('bbbc')
    print(add1 + add2)  # Counter({'b': 4, 'a': 2, 'c': 1})
    print(add1 - add2)  # Counter({'a': 2})     양수인 것만 반환한다.

    # 교집합, 합집합
    print(add1 & add2)  # Counter({'b': 1}) 교집합(두 Counter객체의 요소 중 동일한 요소만 나타나며, 개수는 최소 개수)
    print(add1 | add2)  # Counter({'b': 3, 'a': 2, 'c': 1}) 합집합(두 Counter객체의 모든 요소가 나타나며, 개수는 최대 개수)
