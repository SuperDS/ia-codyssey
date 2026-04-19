# 코디세이 1차 과제 수행 보고서

## 프로젝트 개요(미션요약)
터미널, Docker, Git. 이 세 가지를 직접 손으로 세팅해보기


* git version 2.53.0
* Docker version 28.5.2, build ecc6942


---

## 2) 수행 체크리스트(터미널, 권한, 도커, 도커파일, 포트, 볼륨, 깃, 깃허브)
- [v] 터미널 기본 조작 및 폴더 구성
- [v] 권한 변경 실습
- [x] Docker 설치/점검
- [x] hello-world 실행
- [x] Dockerfile 빌드/실행
- [x] 포트 매핑 접속(2회)
- [x] 바인드 마운트 반영
- [x] 볼륨 영속성
- [x] Git 설정 + VSCode GitHub 연동



* 트러블슈팅 2건 이상(문제-> 원인가설 -> 확인 -> 해결/대안)




* 터미널 조작 로그-> 터미널 수행한 핵심명령과 출력결과를 기술문서에 저장

* docker
docker --version
docker info 설치 점검 결과

docker images
docker ps -a
docker logs
docker stats



2. run

run은 도커에서 아주 중요한 명령입니다.

뜻:

이미지를 바탕으로
새 컨테이너를 생성하고
바로 실행한다

즉 run 하나 안에 보통 두 동작이 들어 있습니다.

create(생성)
start(시작)

-it

이건 사실 -i와 -t가 붙은 것입니다.

-i

interactive
표준 입력을 열어둔다는 뜻입니다.

즉, 내가 키보드로 입력할 수 있게 해줍니다.

-t

tty
터미널 화면처럼 보이게 해줍니다.

즉, 셸에 들어갔을 때 우리가 익숙한 터미널 형태로 사용할 수 있게 합니다.

---

--name vol-test-2

이건 컨테이너 이름을 지정하는 옵션입니다.

--name

“이 컨테이너 이름을 내가 직접 정할게”라는 뜻

vol-test-2

정해준 컨테이너 이름

즉,
이 컨테이너 이름을 vol-test-2로 하겠다는 뜻입니다.

---
--mount type=volume,src=mydata,dst=/data

이 부분이 제일 중요합니다.
볼륨을 연결하는 부분입니다.

--mount는 “저장공간을 어디에 어떻게 연결할지” 정하는 옵션입니다.

이 안을 다시 나누면:

type=volume

연결할 저장공간의 종류가 volume이라는 뜻입니다.

즉:

bind mount 아님
tmpfs 아님
Docker volume 사용
src=mydata

source = 원본 이름

즉, 도커 안에 있는 mydata라는 볼륨을 쓰겠다는 뜻입니다.

쉽게 말하면:

바깥 저장소 이름 = mydata
dst=/data

destination = 컨테이너 안에서 붙일 위치

즉, 컨테이너 내부의 /data 경로에 연결하겠다는 뜻입니다.

쉽게 말하면:

컨테이너 안에서 보이는 연결 위치 = /data

docker run -it --name vol-test-2 --mount type=volume,src=mydata,dst=/data ubuntu bash