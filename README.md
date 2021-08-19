## CTR TRACKER 

> 선사 정보 추적 프로그램 생성 연습
>
> 예시 사이트 ONE https://www.one-line.com/en



### ⚙설치

1. python 설치

2. selenium 설치

   ```
   $ pip install selenium
   ```

3. chormeDriver Download

   ```
   https://chromedriver.chromium.org/downloads
   ```

--------------------



### 🥊동적 웹 테이블 처리

> 선사 사이트의 경우, 행과 열 수가 고정되어있지 않음 (배송상황에 따라서 update)

✏ **문제상황** : `driver.find_elements_by_tag_name` 으로 td 테이블(각각의 행에 있는 칸)을 가지고 와서 크롤링 해야하는 3번째 td 태그 안 a태그의 링크를 찾아서 클릭해야했는데 요소를 찾을 수 없다고 에러가 남.

✏ **시도1** : xpath로 따와서 찾았더니 나옴 (그러나 이 경우에는 xpath를 알고 있어야만 접근이 가능함.) 

✏ **시도2** : td의 3번째 요소를 저장 후 css_selector로 하위 a 태그를 가지고 오려고 했으나  요소를 찾지 못함



##### ⛏동적 테이블로 크롤링하기 기본 개념

1. X-Path로 웹 테이블 요소 찾기
2. 행 및 열 수 구하기
3. 특정 행과 열에 대한 셀 값 가지고 오기



##### 💡 해결

위의 동적 테이블은 사용하지 않고(어차피 detail에 사용해야하기 때문에)

rows를 돌면서 해당하는 a tag를 **XPATH**로 찾아서 클릭해줌.

