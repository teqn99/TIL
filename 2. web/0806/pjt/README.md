# 반응형 웹 페이지 구성

생각보다는 쉽게 하겠지..? 생각했는데, 전혀 아니었다..

화면 크기에 따라 변화되는 화면을 이어주는게 너무 헷갈렸다.

그리드 시스템에 대해 더 공부해야할 듯 하다...



### A. 01_nav_footer

>nav를 만들면서 가장 상단에 계속 고정 시켜야 하기 때문에 sticky-top을 이용해주었다.
>
>또한, 768px기준으로 버튼이 생겼다 없어졌다 해야하기 때문에 navbar-expand-md를 이용해 주었는데, 이 부분이 살짝 이해가 안가서 어려웠다.
>
>>  navbar-expand-md
>>
>> - 화면너비가 md 기준보다 넓으면 navbar-collapse이 표시되고, navbar-toggle은 숨겨짐
>> - 화면너비가 md 기준보다 작으면 navbar-collapse은 숨겨지고, navbar-toggle은 표시됨
>
>```html
><!-- 01_nav_footer.html -->
>  <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top py-0">
>    <div class="container-fluid">
>      <!-- logo -->
>      <a href="02_home.html" class="navbar-brand py-0">
>        <img class="home-logo-img" src="images/logo.png" alt="Logo Image">
>      </a>
>
>      <!-- button -->
>      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
>        <span class="navbar-toggler-icon"></span>
>      </button>
>
>      <!-- menus -->
>      <div class="collapse navbar-collapse row" id="navbarNavAltMarkup">
>        <ul class="navbar-nav justify-content-end">
>          <li class="navbar-item">
>            <a class="nav-link active" href="02_home.html">Home</a>
>          </li>
>          <a class="nav-link" href="03_community.html">Community</a>
>          <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
>        </ul>
>      </div>
>
>    </div>
>  </nav>
>```
>
>
>
>그리고 footer를 만들어 주었는데,
>
>이 부분은 하단에 고정시키면서 글씨 정렬만 필요했기 때문에 쉽게 fixed-bottom을 이용해서 구현할 수 있었다.



### 02_home

> 이 부분은 getbootstrap에서 carousel과 grid cards를 이용해서 쉽게 구현할 수 있었다.
>
> 예시 코드를 빌려 구성만 조금 바꿔주어서 grid cards 부분에서는 화면크기가 작으면 1열, 크면 3열로 구성하여 출력하도록 구현해주었다.
>
> ```html
> <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
>       <div class="carousel-inner">
>         <div class="carousel-item active" data-bs-interval="10000">
>           <img src="images/header1.jpg" class="d-block w-100" alt="header1">
>         </div>
> ```
>
> ```html
> <section class="container">
>     <div class="row row-cols-1 row-cols-md-3 g-4">
>       <div class="col">
>         <div class="card">
>           <img src="images/movie1.jpg" class="card-img-top" alt="movie1">
>           <div class="card-body">
>             <h5 class="card-title">Movie title</h5>
>             <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
>           </div>
>         </div>
>       </div>
> ```
>
> 위의 코드들을 다중 반복하여 구현해주었다.



### 03_community

> 이 부분이 제일 어려웠다.
>
> 사이드바와 리스트를 col-lg-2, col-lg-10으로 나누어 1/6, 5/6으로 크기를 나누어주었고, pagination을 통해 페이지 번호 칸을 만들어 주었다.
>
> col-lg 구현으로 화면 크기에 따라 사이드바와 리스트의 위치 변경이 가능해졌지만,
>
> ~~리스트를 바꾸는 구현은 하지 못했다.~~
>
> **변경사항**
>
> >d-none, d-lg-block, d-block, d-lg-none을 이용하여 lg기준에 따라 숨기고 출력하고 하는 것을 구현했다.
> >
> >위 d-코드들에 의해 list와 table로 표현한 게시판이 조건에 맞는 크기별로 출력된다.
>
> ```html
> <!-- Sidebar -->
>    <aside class="col-12 col-lg-2">
>      <ul class="list-group">
>        <li class="list-group-item list-group-item-action text-primary">Boxoffice</li>
>        <li class="list-group-item list-group-item-action text-primary">Movies</li>
>        <li class="list-group-item list-group-item-action text-primary">Genres</li>
>        <li class="list-group-item list-group-item-action text-primary">Actors</li>
>      </ul>
>    </aside>
> ```
>
> ```html
> <!-- Board_table -->
> <section class="col-12 col-lg-10">
>         <div class="d-none d-lg-block">
>           <table class="table table-striped">
>             <thead>
>               <tr class="table-dark">
>                 <th scope="col">영화 제목</th>
>                 <th scope="col">글 제목</th>
>                 <th scope="col">작성자</th>
>                 <th scope="col">작성 시간</th>
>               </tr>
>             </thead>
>             <tbody>
>               <tr>
>                <!-- 중략 -->
> 
> <!-- Board_list -->
>       <article class="col-12">
>         <div class="d-block d-lg-none">
>           <br><br>
>             <hr class="m-3">
>             <ul class="list-group list-group-flush">
>               <li class="list-group-item">
>                 <div class="d-flex w-100 justify-content-between">
>                   <h5 class="mb-1">Best Movie ever</h5>
>                   <small class="text-muted">user</small>
>                 </div>
>                 <p class="mb-1">Great Movie Title</p>
>                 <small class="text-muted">1 minutes ago</small>
>               </li>
>             </ul>
>             <!-- 중략 -->
> ```
>
> ```html
> <nav aria-label="Page navigation example" class="col-12">
>      <ul class="pagination justify-content-center">
>        <li class="page-item"><a class="page-link" href="#">Previous</a></li>
>        <li class="page-item"><a class="page-link" href="#">1</a></li>
>        <li class="page-item"><a class="page-link" href="#">2</a></li>
>        <li class="page-item"><a class="page-link" href="#">3</a></li>
>        <li class="page-item"><a class="page-link" href="#">Next</a></li>
>      </ul>
>    </nav>
> ```
>
> 위의 코드들의 반복을 통해 게시판을 조건에 맞춰 구현할 수 있었고, 모든 명령들을 잘 수행하는 코드를 완성할 수 있었다.