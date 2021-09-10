# README

> 이번 프로젝트는 익숙해진 부분들이 많아서 생각보다 수월하게 진행할 수 있었다.
>
> 페어 프로그래밍을 위해 git으로 협업하는 방법 대신, vs code의 live share를 이용해보았는데, 인터넷 연결 때문에 가끔씩 느려지는 것을 제외하고는 생각보다 수월하게 진행할 수 있었다.
>
> 그리고 한가지 헷갈렸던 점이 있었는데, 이를 명확히 이해하고 해결할 수 있었다.



### 헷갈렸던 부분

views.py에서 update 함수를 작성하는 부분에서 헷갈렸었다.

detail.html에서 버튼으로 update로 화면을 전환하면서,

**아무런 method를 선언해주지 않았기 때문에 원래 `GET`으로 넘어가는 게 맞다.**

하지만 원래는 왜 POST로 넘어가지 않는거지..?싶었기 때문에 이 부분이 혼동이 되었었다.



즉, detail.html에서 urls.py의 update부분을 불러오고

그리고나서 views.py의 update함수를 호출한다.

이 과정에서 우리는 GET으로 넘겨주었기 때문에 else문으로 넘어가 return을 해주는데, update.html로 render를 해주어 update.html로 넘어간다.

update.html에서는 form에서 method="POST"를 통해 POST방식으로 form을 만들어주고는 다시 urls.py의 update부분을 불러오고

그리고나서 views.py의 update함수를 호출한다.

이제는 POST방식으로 넘어왔기 때문에 update에서 if절로 넘어가게 된다.

**즉, update함수를 `2번 순회`하는 구조라는 것이다.**

지금까지 처음부터 POST로 넘어와 1번만 도는게 아닌가..했었지만,

아니라는 것을 *확실히 알게 되었다.*



### views.py에서 각 함수들의 역할

- `index`

  index함수는 초기화면(main page)을 구성한다. urls.py에서 초기화면으로 지정해주었으며, render를 통해 index.html의 내용을 화면에 출력한다.

- `create`

  create함수는 form을 통해 데이터를 입력하고, 입력받은 데이터를 데이터 베이스에 옮기는 역할을 수행한다. 각각 입력 요소에 맞춰 데이터를 저장하며, 데이터 저장 완료 시 urls.py를 따라 index를 불러낸다.

- `detail `

  detail함수는 입력받거나, 수정되거나, index화면에서 클릭된 경우 호출되는데, 데이터베이스에서 해당 pk에 해당하는 상세내용을 화면에 출력한다.

- `update`

  update함수는 create함수와 비슷하다. 차이점이 있다면, update화면에서 기존에 있던 정보들을 출력한다는 점, 해당 pk에 맞춰 데이터베이스 내의 입력된 정보를 수정한다는 차이점이 존재한다.

- `delete`

  delete함수는 POST로 입력받은 데이터에 한해서만 삭제 연산을 수행한다. 그렇지 않은 경우는 detail화면을 출력하도록 구성해주었다.



### Decorator

> 상속과 유사하게 적용하고자 하는 함수의 바로 윗부분에, @~~의 형식으로 적어준다.
>
> 데코레이터가 없다고 해서 구현을 못하는 일이 생기는 건 아니지만 코드가 복잡해진다. 즉 사용자가 편리해지기 위한 것 이라고 생각할 수 있다.

- require_http_methods

  ```python
  from django.views.decorators.http import require_http_methods
  
  @require_http_methods(["GET", "POST"])
  def my_view(request):
      # I can assume now that only GET or POST requests make it this far
      # ...
      pass
  ```

- require_POST

  ```python
  from django.views.decorators.http import require_POST
  
  @require_POST
  def my_view(request):
      # I can assume now that only POST requests make it this far
      # ...
      pass
  ```

- require_safe

  ```python
  from django.views.decorators.http import require_safe
  
  @require_safe
  def my_view(request):
      # I can assume now that only GET and HEAD requests make it this far
      # ...
      pass
  ```

위와 같은 데코레이터들을 통해 request에 들어오는 입력 method를 제한할 수 있다.









