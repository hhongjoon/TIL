### 0108 _ git 설정 다루기



```bash
# git 사용자 바꾸는 법

git credential reject

protocol=https

host=github.com

이후,
git push   ==>  로그인


 - 스티커 붙이는 과정, commit할 때 정보가 들어가는 용도

git config --global user.name 'hhongjoon'				#username
git config --global user.email 'sungsung129@gmail.com'	#email
git config --global --list								#확인


git config --global color.ui true						#글씨 색칠해주는 것

```



```
# 사용자 삭제 (Windows)
제어판 -> 사용자 계정 -> 자격증명 관리 -> windows 자격증명
```



#### 0108 재귀

- 재귀 최대 횟수는 1000번

- 종료조건 존재해야 함

- 재귀는 함수호출하면서 계속 메모리 소모 / 리스트는 하나의 큰 메모리안에서 돌기때문에  시간 소모 적음

  ```
  메모리효율성은 꽝
  
  ```
