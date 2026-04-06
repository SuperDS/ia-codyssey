# 개발 워크스테이션 구축 미션 - 학습 가이드

안녕하세요! 이 미션은 **개발자의 기초 도구(터미널, Docker, Git)를 직접 손으로 다루며 배우는** 매우 중요한 과정입니다.

저는 이 미션을 단계별로 완성하기 위한 **학습 로드맵**과 **실행 가능한 템플릿**을 제공하겠습니다.

---

## 📋 미션 이해하기

### 핵심 목표 3가지
1. **환경 세팅의 중요성** 이해 (코드 작성 전 기반 구축)
2. **재현 가능한 개발 환경** 구축 (팀원과 동일한 환경)
3. **도구 사용 능력** 습득 (터미널, Docker, Git을 손으로 다루기)

### 왜 이게 중요한가?
- "내 컴퓨터에서만 돌아가요" 문제 해결
- 배포/협업 시 환경 차이로 인한 버그 방지
- 클라우드 배포, CI/CD로 자연스럽게 확장

---

## 🎯 단계별 실행 계획

### **Phase 1: 터미널 기초 (1-2시간)**

#### 1-1) 절대 경로 vs 상대 경로 이해하기

```bash
# 현재 위치 확인
pwd
# 출력 예: /Users/yourname/Desktop

# 절대 경로: 루트(/)에서 시작하는 전체 경로
cd /Users/yourname/Desktop/project
ls -la

# 상대 경로: 현재 위치에서 시작
cd Desktop/project  # 현재가 /Users/yourname일 때
cd ../project       # 한 단계 위로 올라가서 project 진입
cd ./src            # 현재 디렉토리의 src 진입 (./는 생략 가능)
```

**이해 포인트:**
- 절대 경로: 어디서든 동일 (이식성 ✓)
- 상대 경로: 현재 위치에 따라 변함 (간편함 ✓)

---

#### 1-2) 파일 권한 실습

```bash
# 파일 권한 확인
ls -l myfile.txt
# 출력: -rw-r--r-- 1 user group 1024 Jan 1 12:00 myfile.txt
#       ↑ 권한 부분

# 권한 읽는 법
# -rw-r--r--
# ↓ ↓↓↓ ↓↓↓ ↓↓↓
# 파일 소유자 그룹  기타

# r(읽기)=4, w(쓰기)=2, x(실행)=1
# 755 = rwx(7) r-x(5) r-x(5) → 소유자는 모든 권한, 그룹/기타는 읽기+실행만
# 644 = rw-(6) r--(4) r--(4) → 소유자는 읽기+쓰기, 그룹/기타는 읽기만
```

**실습:**

```bash
# 파일 생성
touch testfile.txt
ls -l testfile.txt
# -rw-r--r-- (기본값: 644)

# 권한 변경 - 소유자에게만 쓰기 권한
chmod 600 testfile.txt
ls -l testfile.txt
# -rw------- (소유자만 읽기/쓰기)

# 권한 변경 - 모두에게 실행 권한 추가
chmod 755 testfile.txt
ls -l testfile.txt
# -rwxr-xr-x

# 디렉토리 권한 변경
mkdir testdir
chmod 700 testdir  # 소유자만 접근 가능
ls -ld testdir
# drwx------ (d는 디렉토리)
```

**기술 문서에 기록할 내용:**
```markdown
### 권한 실습 결과

#### 파일 권한 변경
- 변경 전: `ls -l testfile.txt` → `-rw-r--r--`
- 명령: `chmod 600 testfile.txt`
- 변경 후: `ls -l testfile.txt` → `-rw-------`
- 의미: 소유자만 읽기/쓰기 가능

#### 디렉토리 권한 변경
- 변경 전: `ls -ld testdir` → `drwxr-xr-x`
- 명령: `chmod 700 testdir`
- 변경 후: `ls -ld testdir` → `drwx------`
- 의미: 소유자만 접근 가능
```

---

#### 1-3) 터미널 기본 명령 정리

```bash
# 디렉토리 작업
pwd                    # 현재 위치
cd /path/to/dir       # 이동
mkdir mydir           # 생성
rmdir mydir           # 삭제 (비어있을 때만)
rm -rf mydir          # 강제 삭제 (위험!)

# 파일 작업
touch newfile.txt     # 빈 파일 생성
cp source.txt dest.txt  # 복사
mv source.txt dest.txt  # 이동/이름변경
rm file.txt           # 삭제

# 내용 확인
cat file.txt          # 전체 출력
head -n 5 file.txt    # 처음 5줄
tail -n 5 file.txt    # 마지막 5줄
less file.txt         # 페이지 단위 보기 (q로 종료)

# 목록 확인
ls                    # 기본 목록
ls -la                # 숨김파일 포함, 상세 정보
ls -lh                # 파일 크기 읽기 쉽게
```

---

### **Phase 2: Docker 기초 (2-3시간)**

#### 2-1) Docker 설치 확인 (OrbStack 사용)

```bash
# OrbStack이 실행 중인지 확인
docker --version
# Docker version 24.0.0, build xxxxx

# Docker 데몬 상태 확인
docker info
# 출력: 클라이언트/서버 정보, 이미지 수, 컨테이너 수 등

# 간단한 테스트
docker run hello-world
# Hello from Docker!
# This message shows that your installation appears to be working correctly.
```

**기술 문서 기록:**
```markdown
### Docker 설치 및 점검

#### 버전 확인
\`\`\`bash
$ docker --version
Docker version 24.0.0, build abc1234
\`\`\`

#### 데몬 상태 확인
\`\`\`bash
$ docker info
Client:
 Version: 24.0.0
 ...
Server:
 Containers: 5
 Images: 12
 ...
\`\`\`

#### hello-world 실행
\`\`\`bash
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Hello from Docker!
\`\`\`
```

---

#### 2-2) 기본 Docker 명령 실습

```bash
# 이미지 다운로드
docker pull ubuntu:22.04
docker pull nginx:latest

# 이미지 목록 확인
docker images
# REPOSITORY  TAG      IMAGE ID      CREATED      SIZE
# ubuntu      22.04    xxxxx         2 weeks ago  77MB
# nginx       latest   xxxxx         1 week ago   187MB

# 컨테이너 실행 (대화형)
docker run -it ubuntu:22.04 /bin/bash
# 컨테이너 내부에서:
root@abc123:/# ls
root@abc123:/# echo "Hello from container"
root@abc123:/# exit

# 실행 중인 컨테이너 확인
docker ps
# CONTAINER ID  IMAGE   COMMAND  STATUS  PORTS  NAMES

# 모든 컨테이너 확인 (중지된 것 포함)
docker ps -a
# CONTAINER ID  IMAGE          COMMAND      STATUS                  NAMES
# abc123        ubuntu:22.04   /bin/bash    Exited (0) 2 min ago    happy_newton

# 컨테이너 로그 확인
docker logs abc123

# 컨테이너 삭제
docker rm abc123

# 이미지 삭제
docker rmi ubuntu:22.04
```

**실습 결과 기록:**
```markdown
### Docker 기본 명령 실습

#### 1. 이미지 다운로드 및 확인
\`\`\`bash
$ docker pull ubuntu:22.04
22.04: Pulling from library/ubuntu
...
Status: Downloaded newer image for ubuntu:22.04

$ docker images
REPOSITORY   TAG      IMAGE ID       CREATED       SIZE
ubuntu       22.04    ba6acccedd29   2 weeks ago   77.8MB
\`\`\`

#### 2. 컨테이너 실행 (대화형)
\`\`\`bash
$ docker run -it ubuntu:22.04 /bin/bash
root@a1b2c3d4:/# ls
bin  boot  dev  etc  home  lib  ...

root@a1b2c3d4:/# echo "Hello from Docker container"
Hello from Docker container

root@a1b2c3d4:/# exit
\`\`\`

#### 3. 컨테이너 목록 확인
\`\`\`bash
$ docker ps -a
CONTAINER ID   IMAGE          COMMAND       STATUS                   NAMES
a1b2c3d4       ubuntu:22.04   /bin/bash     Exited (0) 1 min ago     dreamy_hopper
\`\`\`

#### 학습 포인트
- **이미지**: 설계도 (읽기 전용)
- **컨테이너**: 실행 중인 프로세스 (격리된 환경)
- **-it 플래그**: 터미널 연결 (-i: 입력, -t: 터미널)
```

---

### **Phase 3: Dockerfile 작성 및 커스텀 이미지 (2-3시간)**

#### 3-1) 간단한 웹 서버 만들기

**디렉토리 구조:**
```
my-web-server/
├── Dockerfile
├── app/
│   └── index.html
└── README.md
```

**app/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Web Server</title>
</head>
<body>
    <h1>🐳 Docker 웹 서버</h1>
    <p>이 페이지는 Docker 컨테이너에서 실행 중입니다!</p>
    <p>현재 시간: <span id="time"></span></p>
    <script>
        document.getElementById('time').textContent = new Date().toLocaleString();
    </script>
</body>
</html>
```

**Dockerfile (방식 A: NGINX 기반):**
```dockerfile
# 베이스 이미지: NGINX
FROM nginx:1.25-alpine

# 작업 디렉토리 설정
WORKDIR /usr/share/nginx/html

# 정적 파일 복사
COPY app/index.html .

# 포트 노출
EXPOSE 80

# 기본 명령 (NGINX 실행)
CMD ["nginx", "-g", "daemon off;"]
```

**Dockerfile (방식 B: Ubuntu 기반):**
```dockerfile
# 베이스 이미지: Ubuntu
FROM ubuntu:22.04

# 패키지 업데이트 및 Python 설치
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# 작업 디렉토리
WORKDIR /app

# 간단한 Python 웹 서버 스크립트
RUN echo 'import http.server\nimport socketserver\n\nclass MyHandler(http.server.SimpleHTTPRequestHandler):\n    pass\n\nwith socketserver.TCPServer(("", 8000), MyHandler):\n    print("Server running on port 8000...")\n    socketserver.TCPServer.serve_forever(socketserver.TCPServer(("", 8000), MyHandler))' > server.py

# 정적 파일 복사
COPY app/ .

# 포트 노출
EXPOSE 8000

# 서버 실행
CMD ["python3", "-m", "http.server", "8000"]
```

---

#### 3-2) 이미지 빌드 및 실행

```bash
# 이미지 빌드
docker build -t my-web-server:1.0 .
# Sending build context to Docker daemon  2.048kB
# Step 1/5 : FROM nginx:1.25-alpine
# ...
# Successfully built abc123def456
# Successfully tagged my-web-server:1.0

# 빌드된 이미지 확인
docker images | grep my-web-server
# my-web-server  1.0  abc123def456  1 min ago  42.3MB

# 컨테이너 실행 (포트 매핑)
docker run -d -p 8080:80 --name my-server my-web-server:1.0
# a1b2c3d4e5f6g7h8i9j0

# 실행 중인 컨테이너 확인
docker ps
# CONTAINER ID  IMAGE              COMMAND                 STATUS  PORTS              NAMES
# a1b2c3d4      my-web-server:1.0  "nginx -g daemon off"   Up 10s  0.0.0.0:8080->80   my-server

# 로그 확인
docker logs my-server
# /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to process SSL certs...
```

**기술 문서 기록:**
```markdown
### 커스텀 이미지 제작

#### 선택한 방식
- **베이스 이미지**: NGINX 1.25-alpine
- **커스텀 포인트**:
  1. 정적 HTML 파일 추가 (app/index.html)
  2. 포트 80 노출 설정
  3. 경량 alpine 기반으로 이미지 크기 최소화

#### 빌