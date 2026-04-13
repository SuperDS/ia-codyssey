1. Docker 설치 및 기본 점검
Docker가 이미 설치되어 있다는 가정 하에, 가장 먼저 Docker가 잘 작동하는지 확인하는 과정입니다. 터미널(Windows에서는 PowerShell 또는 cmd)을 열고 아래 명령어를 입력해 보세요.

1) Docker 버전 확인
Docker Engine의 버전을 확인하는 가장 기본적인 명령어입니다.

bash
📋 복사
# 명령어
docker --version

# 예상 출력 결과
Docker version 20.10.17, build 100c701
설명: 이 명령어를 통해 Docker 클라이언트와 서버의 버전 정보를 알 수 있습니다. 설치가 잘 되었다는 첫 번째 신호죠!

2) Docker 데몬 동작 여부 확인
Docker가 실제로 시스템에서 실행 중인지 상세 정보를 확인합니다.

bash
📋 복사
# 명령어
docker info

# 예상 출력 결과 (일부)
Client:
 Context:    default
 Debug Mode: false
 Plugins:
  ...

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 5
 Server Version: 20.10.17
 ...
설명: Server 섹션에 정보가 잘 출력된다면 Docker 데몬(서비스)이 정상적으로 동작하고 있다는 의미입니다. 만약 에러가 발생한다면 Docker Desktop을 실행하거나 서비스가 중지된 상태일 수 있습니다.

3) Docker 기본 운영 명령 수행
이미지 다운로드/목록 확인
Docker Hub라는 이미지 저장소에서 ubuntu의 최신 버전을 받아오고, 내 컴퓨터에 저장된 이미지 목록을 확인해 봅시다.

bash
📋 복사
# ubuntu 최신 이미지 다운로드
docker pull ubuntu

# 로컬 이미지 목록 확인
docker images

# 예상 출력 결과
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
ubuntu       latest    a2a15feb1329   2 weeks ago    77.8MB
...
컨테이너 실행/중지/목록 확인
다운로드한 ubuntu 이미지로 컨테이너를 실행하고 상태를 확인합니다.

bash
📋 복사
# 'my-ubuntu'라는 이름으로 ubuntu 컨테이너를 백그라운드에서 실행
# -itd 옵션: 터미널을 유지(-it)하고, 백그라운드에서 실행(-d)
docker run -itd --name my-ubuntu ubuntu

# 현재 실행 중인 컨테이너 목록 확인
docker ps

# 예상 출력 결과
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS          PORTS     NAMES
a1b2c3d4e5f6   ubuntu    "bash"    5 seconds ago    Up 4 seconds              my-ubuntu

# 컨테이너 중지
docker stop my-ubuntu

# 중지된 컨테이너까지 포함한 모든 컨테이너 목록 확인
docker ps -a

# 예상 출력 결과
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS                      PORTS     NAMES
a1b2c3d4e5f6   ubuntu    "bash"    20 seconds ago   Exited (137) 5 seconds ago            my-ubuntu
로그 및 리소스 확인
컨테이너가 실행되면서 남긴 기록(로그)을 보거나, 현재 자원 사용량을 실시간으로 확인할 수 있습니다.

bash
📋 복사
# 컨테이너를 다시 시작
docker start my-ubuntu

# 컨테이너 로그 확인 (지금은 특별한 로그가 없을 수 있습니다)
docker logs my-ubuntu

# 컨테이너 리소스 사용량 실시간 확인 (Ctrl+C로 종료)
docker stats

# 예상 출력 결과 (docker stats)
CONTAINER ID   NAME        CPU %     MEM USAGE / LIMIT   MEM %     NET I/O           BLOCK I/O         PIDS
a1b2c3d4e5f6   my-ubuntu   0.00%     540KiB / 1.944GiB   0.03%     1.09kB / 0B       0B / 0B           1
정리: 이 과정들을 통해 Docker의 가장 기본적인 사이클(이미지 받기 → 컨테이너 실행 → 상태 확인 → 중지)을 익혔습니다. 아주 잘하셨어요!

2. 컨테이너 실행 실습
이제 컨테이너를 좀 더 깊이 있게 다뤄볼 시간입니다.

1) hello-world 실행
Docker 설치 후 가장 먼저 해보는 '국룰' 같은 명령어죠!

bash
📋 복사
# 명령어
docker run hello-world

# 예상 출력 결과
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
설명: 이 간단한 명령어 뒤에는 많은 일이 일어납니다.

로컬에 hello-world 이미지가 있는지 확인
없으면 Docker Hub에서 다운로드
다운로드한 이미지로 컨테이너 생성 및 실행
컨테이너가 "Hello from Docker!" 메시지를 출력하고 종료
종료된 컨테이너는 docker ps -a로 확인할 수 있습니다.
2) ubuntu 컨테이너 내부 진입 및 명령어 수행
bash
📋 복사
# ubuntu 컨테이너를 실행하고, 내부의 bash 셸로 바로 진입
docker run -it --name my-ubuntu2 ubuntu /bin/bash

# 이제 프롬프트가 컨테이너 내부로 바뀝니다 (예: root@f1g2h3i4j5k6:/#)
# 컨테이너 내부에서 명령어 수행
ls
echo "Hello from inside the container!"

# 출력 결과
bin   dev  home  lib32  libx32  mnt  proc  run   srv  tmp  var
boot  etc  lib   lib64  media   opt  root  sbin  sys  usr
Hello from inside the container!

# 'exit'를 입력하여 컨테이너에서 빠져나오기
exit
설명: docker run -it 명령어로 컨테이너와 상호작용하는 세션을 열었습니다. 마치 가상머신에 접속한 것처럼 컨테이너 내부에서 리눅스 명령어를 자유롭게 사용할 수 있죠.

3) 컨테이너 종료/유지(attach/exec 등)의 차이 관찰
이 부분이 정말 중요합니다!

일회성 실행 후 종료: 컨테이너는 주어진 임무(명령)가 끝나면 바로 종료됩니다.

bash
📋 복사
# "hello"를 출력하는 임무가 끝나면 바로 컨테이너는 종료(Exited) 상태가 됨
docker run ubuntu echo "hello"
백그라운드에서 계속 실행 (유지): -d 옵션으로 컨테이너를 백그라운드에서 계속 실행시킬 수 있습니다. 웹 서버처럼 계속 켜져 있어야 하는 서비스에 사용됩니다.

bash
📋 복사
# -d 옵션으로 백그라운드에서 실행
docker run -itd --name my-running-ubuntu ubuntu
실행 중인 컨테이너에 접속 (exec): 이미 실행 중인 컨테이너에 추가적인 명령을 내리거나 접속할 때 사용합니다.

bash
📋 복사
# 위에서 실행한 my-running-ubuntu 컨테이너에 접속
docker exec -it my-running-ubuntu /bin/bash

# 내부에서 'ls' 실행
ls
exit
핵심 정리:

docker run [이미지] [명령]: [명령]이 끝나면 컨테이너도 종료됩니다.
docker run -d [이미지]: 컨테이너를 백그라운드에서 계속 실행시킵니다.
docker exec [컨테이너] [명령]: 실행 중인 컨테이너에 새로운 명령을 내립니다. 가장 많이 쓰는 방식 중 하나입니다!
3. 기존 Dockerfile 기반 커스텀 이미지 제작
이번에는 직접 Docker 이미지를 만들어 보겠습니다. (A)안인 NGINX 웹 서버 만들기가 가장 직관적이고 재미있으니 이걸로 해볼게요!

1) 베이스 이미지 선택 및 커스텀 포인트
기존 베이스: nginx:alpine (가볍고 빠른 NGINX 공식 이미지)
커스텀 포인트: 내가 만든 간단한 index.html 파일을 NGINX의 기본 웹 페이지로 교체한다.
2) 실습 준비
먼저, 작업할 폴더를 하나 만들고 그 안에 Dockerfile과 index.html 두 개의 파일을 생성합니다.

bash
📋 복사
# 1. 작업 폴더 생성 및 이동
mkdir my-nginx-app
cd my-nginx-app

# 2. index.html 파일 생성
# 아래 내용을 index.html 파일에 저장하세요.
index.html 내용:

html
📋 복사
<!DOCTYPE html>
<html>
<head>
<title>나만의 웹 서버</title>
</head>
<body>
<h1>Docker로 만든 커스텀 웹 서버에 오신 것을 환영합니다!</h1>
<p>이 페이지는 제가 직접 만든 이미지로부터 실행되었습니다.</p>
</body>
</html>
Dockerfile 내용:

dockerfile
📋 복사
# 1. 베이스 이미지 선택
FROM nginx:alpine

# 2. 내가 만든 파일을 컨테