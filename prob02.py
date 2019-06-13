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

while s.find('<') != -1:
    start = s.find('<')
    end = s.find('>')
    s = s.replace(s[start:end + 1], '')

print(s)
