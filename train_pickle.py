"""pickle 모듈 실습

공식 문서 : https://docs.python.org/3/library/pickle.html#module-pickle
"""
import pickle
import os.path

if __name__ == "__main__":
    ls_to_save = [1, 'a']   # 저장할 객체 생성
    filename = 'pickle_test.bin'

    if not os.path.exists(filename):
        with open(filename, 'wb') as f: 
            pickle.dump(ls_to_save, f)  # 파일명 'pickle_test.bin'로 쓰기

    with open(filename, 'rb') as f:
        ls_loaded = pickle.load(f)  # 'pickle_test.bin' 파일 읽기
            
        print(ls_loaded)

    a = pickle.dumps(ls_to_save)
    print(a)    # b'\x80\x03]q\x00(K\x01X\x01\x00\x00\x00aq\x01e.'

    b = pickle.loads(a)
    print(b)    # [1, 'a']


    '''
    참고
    pickle.dump와 pickle.load는 파일로 쓰고 읽는 것이고,
    pickle.dumps와 pickle.loads는 문자열로 변환
    '''
