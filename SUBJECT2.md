# 서울 구(區) 기반 퀴즈 게임 완벽 구현 가이드

학생분을 위해 **처음부터 끝까지** 단계별로 구현하겠습니다! 🎯

---

# 📌 Phase 1: Git 저장소 설정

## 1-1) GitHub 저장소 생성

### Step 1: GitHub에서 새 저장소 생성
```
1. github.com 접속
2. 우측 상단 + 클릭 → "New repository"
3. Repository name: seoul-quiz-game
4. Description: 서울 구(區) 기반 퀴즈 게임
5. Public 선택
6. "Create repository" 클릭
```

---

## 1-2) 로컬 저장소 설정

### Step 1: 프로젝트 디렉토리 생성
```bash
mkdir seoul-quiz-game
cd seoul-quiz-game
```

### Step 2: Git 초기화
```bash
git init
```

**출력:**
```
Initialized empty Git repository in /Users/student/seoul-quiz-game/.git/
```

### Step 3: 원격 저장소 연결
```bash
# <YOUR_USERNAME>을 자신의 GitHub 사용자명으로 변경
git remote add origin https://github.com/<YOUR_USERNAME>/seoul-quiz-game.git
```

### Step 4: 원격 저장소 확인
```bash
git remote -v
```

**출력:**
```
origin  https://github.com/<YOUR_USERNAME>/seoul-quiz-game.git (fetch)
origin  https://github.com/<YOUR_USERNAME>/seoul-quiz-game.git (push)
```

---

## 1-3) .gitignore 파일 생성

### 📄 .gitignore
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
*.log
.env
```

---

## 1-4) README.md 파일 생성

### 📄 README.md
```markdown
# 서울 구(區) 퀴즈 게임 🏙️

## 📖 프로젝트 개요
서울의 25개 구(區)에 대한 지리, 역사, 문화, 특징을 다루는 **대화형 퀴즈 게임**입니다.
사용자는 퀴즈를 풀면서 서울의 각 구에 대해 학습할 수 있습니다.

## 🎯 퀴즈 주제와 선정 이유
**주제**: 서울의 25개 구(강남구, 강북구, 강동구, 강서구, 관악구, 광진구, 구로구, 금천구, 
노원구, 도봉구, 동대문구, 동작구, 마포구, 서대문구, 서초구, 성동구, 성북구, 송파구, 
양천구, 영등포구, 용산구, 은평구, 종로구, 중구, 중랑구)

**선정 이유**: 
- 서울 시민이 알아야 할 기본 지식
- 각 구의 특징과 역사를 재미있게 학습
- 지리 교육과 연계 가능

## 🚀 실행 방법

### 필수 요구사항
- Python 3.8 이상
- 터미널/명령 프롬프트

### 설치 및 실행
```bash
# 1. 저장소 복제
git clone https://github.com/<YOUR_USERNAME>/seoul-quiz-game.git
cd seoul-quiz-game

# 2. 프로그램 실행
python main.py
```

## 📋 기능 목록

| 기능 | 설명 |
|------|------|
| **퀴즈 풀기** | 저장된 퀴즈를 순서대로 풀고 점수 확인 |
| **퀴즈 추가** | 새로운 퀴즈를 등록 |
| **퀴즈 목록** | 저장된 모든 퀴즈 확인 |
| **점수 확인** | 최고 점수 확인 |
| **종료** | 프로그램 안전 종료 |

## 📁 파일 구조
```
seoul-quiz-game/
├── main.py                 # 프로그램 진입점
├── quiz.py                 # Quiz 클래스
├── game.py                 # QuizGame 클래스
├── state.json              # 퀴즈 데이터 및 최고 점수 저장
├── .gitignore              # Git 무시 파일
└── README.md               # 이 파일
```

## 📊 데이터 파일 설명 (state.json)

### 경로
```
프로젝트 루트/state.json
```

### 역할
- 사용자가 추가한 퀴즈 데이터 저장
- 최고 점수 기록
- 프로그램 재시작 후에도 데이터 유지

### 스키마 (JSON 구조)
```json
{
  "quizzes": [
    {
      "question": "서울에서 가장 넓은 구는?",
      "choices": ["강남구", "강서구", "송파구", "강동구"],
      "answer": 2
    }
  ],
  "best_score": {
    "correct": 5,
    "total": 10,
    "percentage": 50.0
  }
}
```

### 필드 설명
- `quizzes`: 퀴즈 목록 배열
  - `question`: 문제 텍스트
  - `choices`: 선택지 배열 (4개)
  - `answer`: 정답 번호 (1~4)
- `best_score`: 최고 점수 기록
  - `correct`: 정답 개수
  - `total`: 전체 문제 수
  - `percentage`: 정답률 (%)

## 💡 사용 예시

```
=== 서울 구 퀴즈 게임 ===

1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료

선택: 1

[1/5] 서울에서 가장 넓은 구는?
1) 강남구
2) 강서구
3) 송파구
4) 강동구

정답: 2
✅ 정답입니다!

...

최종 점수: 5/5 (100%)
🏆 새로운 최고 점수입니다!
```

## 📝 개발 노트

### 예외 처리
- 숫자 입력 검증 (공백 제거, 범위 확인)
- 파일 손상 시 기본 데이터로 복구
- Ctrl+C 안전 종료

### 데이터 영속성
- JSON 파일로 자동 저장
- UTF-8 인코딩 사용

## 🔄 Git 커밋 히스토리

```
1. Initial commit: .gitignore, README.md
2. feat: 메뉴 기능 구현
3. feat: Quiz 클래스 구현
4. feat: 기본 퀴즈 데이터 추가
5. feat: 퀴즈 풀기 기능
6. feat: 퀴즈 추가 기능
7. feat: 퀴즈 목록 기능
8. feat: 점수 확인 기능
9. refactor: QuizGame 클래스 정리
10. feat: 파일 입출력 기능
```

## 👨‍💻 작성자
- 학생 이름

## 📄 라이선스
MIT License
```

---

## 1-5) 첫 번째 커밋 및 푸시

### Step 1: 파일 추가
```bash
git add .gitignore README.md
```

### Step 2: 커밋
```bash
git commit -m "Initial commit: .gitignore, README.md"
```

**출력:**
```
[main (root-commit) a1b2c3d] Initial commit: .gitignore, README.md
 2 files changed, 50 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
```

### Step 3: 푸시
```bash
# 첫 푸시는 -u 옵션 사용
git push -u origin main
```

**출력:**
```
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.23 KiB | 1.23 MiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/<YOUR_USERNAME>/seoul-quiz-game.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

---

# 📌 Phase 2: 메뉴 기능 구현

## 2-1) main.py 작성

### 📄 main.py
```python
"""
서울 구(區) 퀴즈 게임 - 메인 진입점
"""

def display_menu():
    """메뉴 출력"""
    print("\n" + "="*40)
    print("🏙️  서울 구(區) 퀴즈 게임")
    print("="*40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("="*40)


def get_menu_choice():
    """메뉴 선택 입력"""
    while True:
        try:
            choice = input("선택: ").strip()
            
            # 빈 입력 처리
            if not choice:
                print("❌ 입력이 비어있습니다. 1~5 중 선택하세요.")
                continue
            
            # 숫자 변환
            try:
                choice_num = int(choice)
            except ValueError:
                print(f"❌ '{choice}'는 숫자가 아닙니다. 1~5 중 선택하세요.")
                continue
            
            # 범위 확인
            if choice_num < 1 or choice_num > 5:
                print(f"❌ {choice_num}은 범위를 벗어났습니다. 1~5 중 선택하세요.")
                continue
            
            return choice_num
            
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  프로그램을 종료합니다.")
            raise SystemExit(0)


def main():
    """메인 함수"""
    print("프로그램을 시작합니다...")
    
    while True:
        try:
            display_menu()
            choice = get_menu_choice()
            
            if choice == 1:
                print("✅ 퀴즈 풀기 기능 (구현 예정)")
            elif choice == 2:
                print("✅ 퀴즈 추가 기능 (구현 예정)")
            elif choice == 3:
                print("✅ 퀴즈 목록 기능 (구현 예정)")
            elif choice == 4:
                print("✅ 점수 확인 기능 (구현 예정)")
            elif choice == 5:
                print("\n👋 프로그램을 종료합니다.")
                break
                
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 예상치 못한 오류: {e}")
            continue


if __name__ == "__main__":
    main()
```

---

## 2-2) 메뉴 기능 테스트

### 실행
```bash
python main.py
```

**출력:**
```
프로그램을 시작합니다...

========================================
🏙️  서울 구(區) 퀴즈 게임
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1
✅ 퀴즈 풀기 기능 (구현 예정)

========================================
🏙️  서울 구(區) 퀴즈 게임
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: abc
❌ 'abc'는 숫자가 아닙니다. 1~5 중 선택하세요.

========================================
...
선택: 5

👋 프로그램을 종료합니다.
```

---

## 2-3) 메뉴 기능 커밋

```bash
git add main.py
git commit -m "feat: 메뉴 기능 구현 - 메뉴 출력, 선택, 예외 처리"
git push origin main
```

**출력:**
```
[main a1b2c3d] feat: 메뉴 기능 구현 - 메뉴 출력, 선택, 예외 처리
 1 file changed, 80 insertions(+)
```

---

# 📌 Phase 3: Quiz 클래스 구현

## 3-1) quiz.py 작성

### 📄 quiz.py
```python
"""
Quiz 클래스 - 개별 퀴즈 표현
"""


class Quiz:
    """
    개별 퀴즈를 표현하는 