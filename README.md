# 코디세이 1차 과제 수행 보고서

## 프로젝트 개요(미션요약)
터미널, Docker, Git. 이 세 가지를 직접 손으로 세팅해보기


* git version 2.53.0
* Docker version 28.5.2, build ecc6942


---

## 2) 수행 체크리스트(터미널, 권한, 도커, 도커파일, 포트, 볼륨, 깃, 깃허브)
- [x] 터미널 기본 조작 및 폴더 구성
- [x] 권한 변경 실습
- [x] Docker 설치/점검
- [x] hello-world 실행
- [x] Dockerfile 빌드/실행
- [x] 포트 매핑 접속(2회) 8080, 8081
- [x] 바인드 마운트 반영
- [x] 볼륨 영속성
- [x] Git 설정 + VSCode GitHub 연동

---

- **현재 위치 확인**: 현재 작업 중인 디렉토리 경로를 확인한다.  
  예: `pwd`

- **목록 확인(숨김 파일 포함)**: 현재 위치의 파일과 폴더 목록을 숨김 파일까지 포함하여 확인한다.  
  예: `ls -al`
  -l : 자세히 보기
  -a : 숨김파일까지보기
  -t : 최근 수저왼 파일 순으로 정렬
  

- **이동**: 다른 디렉토리로 이동한다.  
  예: `cd 폴더명`

- **생성**: 새 폴더를 생성한다.  
  예: `mkdir 폴더명`

- **복사**: 파일 또는 폴더를 복사한다.  
  예: `cp 파일명 복사본이름`

- **이동/이름변경**: 파일이나 폴더를 다른 위치로 옮기거나 이름을 바꾼다.  
  예: `mv 기존이름 새이름`

- **삭제**: 파일 또는 폴더를 삭제한다.  
  예: `rm 파일명`, `rm -r 폴더명`

- **파일 내용 확인**: 파일 안에 저장된 내용을 확인한다.  
  예: `cat 파일명`

- **빈 파일 생성**: 내용이 없는 새 파일을 만든다.  
  예: `touch 파일명`

---
mkdir
touch

생성 이후  
ex : chmod 777 [파일 혹은 폴더명]


소유자(owner)
그 파일이나 디렉토리를 직접 만든 사용자 또는 현재 주인입니다.
보통 가장 강한 권한을 가집니다.

그룹(group)
같은 그룹에 속한 사용자들에게 주는 권한입니다.
예를 들어 같은 팀원끼리 같은 그룹으로 묶어둘 수 있습니다.

기타(other)
소유자도 아니고, 해당 그룹도 아닌 나머지 모든 사용자입니다.

---

권한 숫자는 r, w, x를 숫자로 바꿔서 더한 것입니다.

r = 4
w = 2
x = 1

그래서 각 자리 숫자는 읽기/쓰기/실행 권한의 조합 결과입니다.

맨 앞의 - 와 d 는
“이게 파일이냐, 디렉토리냐”를 나타내는 문자입니다.

예를 들어:
-rw-r--r--

맨 앞 - 는 일반 파일이라는 뜻입니다.
drwxr-xr-x
맨 앞 d 는 디렉토리(폴더) 라는 뜻입니다.
r w x 1 2 4



---
## Docker

## Docker 기본 명령어 정리

- `docker -v`  
  Docker 버전을 간단히 확인한다.

- `docker --version`  
  Docker 버전을 확인한다.

- `docker info`  
  Docker 설치 및 실행 환경 점검 결과를 확인한다.

- `docker images`  
  현재 로컬에 저장된 Docker 이미지 목록을 확인한다.
  (docker rmi repository -> 도커 이미지 삭제)

- `docker ps -a`  
  실행 중인 컨테이너와 종료된 컨테이너를 모두 확인한다.

- `docker logs 컨테이너명`  
  해당 컨테이너가 실행 중 또는 종료 전에 남긴 로그를 확인한다.

- `docker stats`  
  실행 중인 컨테이너의 CPU, 메모리 등 자원 사용량을 실시간으로 확인한다.

---

## `docker run` 명령

`run`은 Docker에서 아주 중요한 명령이다.

의미:
- 이미지를 바탕으로
- 새 컨테이너를 생성하고
- 바로 실행한다.

즉, `run` 하나 안에는 보통 다음 두 동작이 포함된다.

- `create` : 컨테이너 생성
- `start` : 컨테이너 시작

---

* hello-world 이미지 실행시키기
- docker run hello-world -> 이미지다운로드 및 실행 -> docker logs [id]로 확인가능

* 우분투 실행 bash 로
- docker run -it --name myubuntu ubuntu bash

* 도커 Index.html 실행
- docker build -t codyssey-web .

build : 이미지 만들기
-t codyssey-web : 이미지 이름을 codyssey-web으로 지정 . : 현재 폴더 기준으로 빌드

* 도커 포트 매핑
docker run -d -p 8080:80 --name codyssey-nginx codyssey-web

-d : 백그라운드 실행
-p 8080:80 : 내 컴퓨터 8080 포트를 컨테이너 80 포트와 연결
-p 8080:80 : 내 컴퓨터 8081 포트를 컨테이너 81 포트와 연결
--name codyssey-nginx : 컨테이너 이름 지정(컨테이너 이름이 다르면 오류)
codyssey-web : 방금 만든 이미지 이름

lsof -i :8080 
명령으로 8080 포트 사용 여부를 사전 확인

* docker exec -it [컨테이너id]] bash 
- 실행중인 도커 접속

* docker stop [컨테이너 id]
- 도커 정지

* docker start 컨테이너이름
- 도커 다시 시작


* docker run -it --name vol-test-1 --mount type=volume,src=mydata,dst=/data ubuntu bash
echo "docker volume persistence test" > /data/test.txt



* docker run -it --name vol-test-2 --mount type=volume,src=mydata,dst=/data ubuntu bash
- 도커볼륨 영속성 확인


* docker volume ls -> 도커 볼륨 확인
* docker volume inspect mydata -> 도커볼륨 마이데이타 확인

---
## `-it` 옵션

`-it`는 사실 `-i`와 `-t`가 합쳐진 옵션이다.

### `-i`
- `interactive`
- 표준 입력을 열어둔다는 뜻이다.
- 사용자가 키보드로 직접 입력할 수 있게 한다.

### `-t`
- `tty`
- 터미널 화면처럼 보이게 해준다.
- 컨테이너 내부 셸을 일반 터미널처럼 사용할 수 있게 한다.

즉, `-it`를 사용하면 컨테이너 안에 들어가 직접 명령어를 입력할 수 있다.

---

## `--name vol-test-2`

이 옵션은 컨테이너 이름을 직접 지정하는 역할을 한다.

- `--name`  
  컨테이너 이름을 사용자가 직접 지정하겠다는 뜻이다.

- `vol-test-2`  
  지정한 컨테이너 이름이다.

즉, 이 컨테이너의 이름을 `vol-test-2`로 설정하겠다는 의미이다.

---

## `--mount type=volume,src=mydata,dst=/data`

이 부분은 Docker 볼륨을 컨테이너에 연결하는 옵션이다.

### `--mount`
- 저장공간을 어디에, 어떤 방식으로 연결할지 지정한다.

### `type=volume`
- 연결할 저장공간의 종류가 `volume`이라는 뜻이다.
- 즉, bind mount나 tmpfs가 아니라 Docker volume을 사용한다.

### `src=mydata`
- `source`의 약자이다.
- Docker 안에 있는 `mydata`라는 이름의 볼륨을 사용하겠다는 뜻이다.
- 쉽게 말하면 바깥 저장소 이름이 `mydata`이다.

### `dst=/data`
- `destination`의 약자이다.
- 컨테이너 내부의 `/data` 경로에 연결하겠다는 뜻이다.
- 쉽게 말하면 컨테이너 안에서 보이는 연결 위치가 `/data`이다.

즉, `mydata`라는 Docker 볼륨을 컨테이너 내부 `/data` 폴더에 연결하는 설정이다.



---
* 트러블슈팅 2건 이상(문제-> 원인가설 -> 확인 -> 해결/대안)

* 도커 삭제 안됨 -> 도커 실행중인가? -> 확인함 -> 도커 중지 -> 도커 컨테이너 삭제

* 포트매핑 실패 -> 포트를 누군가 사용하고있으면 매핑이 안됨 -> 포트매핑 확인 -> 재설정 -> 해결
명령으로 8080 포트 사용 여부를 사전 확인
--- 