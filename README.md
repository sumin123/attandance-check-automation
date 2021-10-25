# 출석 체크 자동화

출석 스터디용 출석 체크 자동화 프로그램입니다.

Window 환경을 전제로 동작합니다.

매일 출석 카톡을 읽어서 출석 점수 및 벌금을 계산하여 json파일로 저장합니다.

### 자동 실행

- 윈도우의 작업 스케줄러를 활용해 매일 자동 실행되도록 설정할 수 있습니다.
![image](https://user-images.githubusercontent.com/43175576/138712081-bccc345a-fd0b-4f12-91a3-ce32e44bd241.png)

### 출석 카톡 양식 예시
```
출석 - OO OO OO
통보 - OO OO
결석 - OO OO
```

### Dependency
- Python의 PyWin32를 이용했습니다.
- `pip install py32api`
