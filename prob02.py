# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
s = '''
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>'''

while s.find('<') != -1:    # 태그 개수만큼 반복
    start = s.find('<')     # 태그 시작 인덱스
    end = s.find('>')       # 태그 끝 인덱스
    s = s.replace(s[start:end + 1], '')  # 태그 시작부터 끝부분 지우기

print(s)
