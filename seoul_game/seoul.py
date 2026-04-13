import json
import os

# 1. Quiz 클래스 정의
class Quiz:
    """개별 퀴즈를 표현하는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 사이의 정수

    def display(self, index):
        print(f"\n[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return self.answer == user_answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

# 2. QuizGame 클래스 정의
class QuizGame:
    def __init__(self):
        self.file_path = "state.json"
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    # [파일 불러오기]
    def load_data(self):
        default_quizzes = [
            Quiz("남산타워가 위치한 구는 어디일까요?", ["강남구", "용산구", "서초구", "종로구"], 2),
            Quiz("경복궁과 광화문 광장이 있는 구는?", ["종로구", "중구", "성동구", "마포구"], 1),
            Quiz("롯데월드타워(제2롯데월드)가 있는 구는?", ["강동구", "송파구", "광진구", "성동구"], 2),
            Quiz("서울대학교 관악캠퍼스가 위치한 구는?", ["동작구", "관악구", "금천구", "서초구"], 2),
            Quiz("가로수길과 코엑스가 위치한 구는?", ["강남구", "서초구", "송파구", "강동구"], 1)
        ]

        if not os.path.exists(self.file_path):
            self.quizzes = default_quizzes
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
                if not self.quizzes:
                    self.quizzes = default_quizzes
        except (json.JSONDecodeError, IOError):
            print("\n[알림] 데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self.quizzes = default_quizzes
            self.save_data()

    # [파일 저장하기]
    def save_data(self):
        data = {
            "best_score": self.best_score,
            "quizzes": [q.to_dict() for q in self.quizzes]
        }
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError:
            print("\n[오류] 파일 저장 중 문제가 발생했습니다.")

    # [공통 입력 및 예외 처리]
    def get_valid_input(self, prompt, min_val=None, max_val=None):
        while True:
            try:
                user_input = input(prompt).strip()
                if not user_input:
                    print(">> 빈 입력입니다. 내용을 입력해주세요.")
                    continue
                
                val = int(user_input)
                if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                    print(f">> 허용 범위를 벗어났습니다. ({min_val}~{max_val})")
                    continue
                return val
            except ValueError:
                print(">> 숫자를 입력해야 합니다. (예: 1)")

    # [메뉴 1: 퀴즈 풀기]
    def play_quiz(self):
        if not self.quizzes:
            print("\n[알림] 등록된 퀴즈가 없습니다.")
            return

        current_score = 0
        print("\n--- 퀴즈를 시작합니다! ---")
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)
            choice = self.get_valid_input("정답 번호 입력: ", 1, 4)
            
            if quiz.is_correct(choice):
                print("정답입니다!")
                current_score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n모든 문제를 풀었습니다! 내 점수: {current_score}/{len(self.quizzes)}")
        
        if current_score > self.best_score:
            print(f"축하합니다! 최고 점수 경신! ({self.best_score} -> {current_score})")
            self.best_score = current_score
            self.save_data()

    # [메뉴 2: 퀴즈 추가]
    def add_quiz(self):
        print("\n--- 새로운 퀴즈 등록 ---")
        question = input("문제 내용: ").strip()
        while not question:
            question = input("문제 내용은 필수입니다: ").strip()
            
        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            while not choice:
                choice = input(f"선택지 {i} 내용을 입력하세요: ").strip()
            choices.append(choice)
            
        answer = self.get_valid_input("정답 번호 (1~4): ", 1, 4)
        
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("\n[성공] 퀴즈가 추가되었습니다.")

    # [메뉴 3: 목록 보기]
    def list_quizzes(self):
        if not self.quizzes:
            print("\n[알림] 저장된 퀴즈가 없습니다.")
            return
        
        print("\n--- 저장된 퀴즈 목록 ---")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question} (정답: {q.answer}번)")

    # [메뉴 4: 점수 확인]
    def show_best_score(self):
        if self.best_score == 0:
            print("\n[알림] 아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"\n현재 최고 점수는 {self.best_score}점입니다.")

    # [메인 메뉴 실행]
    def run(self):
        while True:
            try:
                print("\n=== 서울 구 맞추기 게임 ===")
                print("1. 퀴즈 풀기")
                print("2. 퀴즈 추가")
                print("3. 퀴즈 목록")
                print("4. 최고 점수 확인")
                print("0. 종료")
                
                menu = self.get_valid_input("메뉴 선택: ", 0, 4)

                if menu == 1: self.play_quiz()
                elif menu == 2: self.add_quiz()
                elif menu == 3: self.list_quizzes()
                elif menu == 4: self.show_best_score()
                elif menu == 0:
                    print("\n게임을 안전하게 종료합니다. 다음에 또 봐요!")
                    self.save_data()
                    break
            except (KeyboardInterrupt, EOFError):
                print("\n\n[알림] 강제 종료를 감지했습니다. 데이터를 저장하고 종료합니다.")
                self.save_data()
                break

if __name__ == "__main__":
    game = QuizGame()
    game.run()