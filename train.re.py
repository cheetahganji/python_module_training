"""re 모듈 실습

공식 문서 : 
"""
import re

if __name__ == "__main__":
    text = '010-0981-3722 010-1234-5678'    

    p = re.compile(r'\d{3}')     # 패턴을 담는다
    rst = p.match(text)     # match는 문자열의 첫 번째 부터 검사를 한다. 1개의 결과만 반환한다.
    print(rst.group())      # 010

    rst = p.search(text)    # search는 모든 위치를 검사한 후 1개의 결과만 반환한다.
    print(rst.group())      # 010

    rst = p.findall(text)   # 모든 결과를 문자열형태로 리스트 반환
    print(rst)              # ['010', '098', '372', '010', '123', '567']
