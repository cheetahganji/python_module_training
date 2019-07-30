"""openpyxl 모듈 실습
"""

import openpyxl

xl = openpyxl.Workbook()    # 엑셀파일 생성(추후 xl.save()를 해야 엑셀파일이 생성됨)

sheet = xl.active   # 활성화되어있는 시트 객체 가져오기(처음엔 시트가 1개('Sheet')밖에 없어서 명칭이 'Sheet'인 시트를 가져옴)
print(sheet.title)  # 시트명 출력 : Sheet

xl.create_sheet('Sheet2')   # 신규 시트 생성(생성했다고 활성화되진 않음!)
print(sheet.title)  # 시트명 출력 : Sheet

sheet = xl['Sheet2']    # 이렇게 특정 시트 객체를 가져올 수 있는데 이러면 sheet. 할 때 관련 메소드가 안나옴... 근데 안나와도 sheet.title 이런거 하면 오류는 안남
print(sheet.title)  # 시트명 출력 : Sheet2

xl._active_sheet_index = 1  # 이렇게 쓰면 안될 것 같긴한데.. 잘 작동은 함
sheet = xl.active
print(sheet)    # <Worksheet "Sheet2">

sheet.cell(1, 1, 'abc') # 1행 1열에 abc 문자열 쓰기(row, col은 1부터 시작함)
sheet.append([1,2,3,4,5])   # 데이터가 있는 마지막 행 다음 행에 1열에 1, 2열에 2 3열에 3, ... 쓰기
xl.save('openpyxl_test.xlsx')


xl = openpyxl.load_workbook('openpyxl_test.xlsx')   # 엑셀 로드


xl.close()
