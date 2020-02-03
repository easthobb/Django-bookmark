from django.urls import path
from .views import BookmarkListView,BookmarkCreateView,BookmarkDetailView,BookmarkUpdateView,BookmarkDeleteView

urlpatterns = [
    path('',BookmarkListView.as_view(),name='list'), #bookmark/ 이하 부분이 없다면 북마크 리스트 뷰를 호출하겠다는 의미 클래스형일경우 as_view()
    # 마지막 인자 네임은 설정한 이름을 가지고 URL패턴을 찾을 수 있도록 하는 역할을 수행한다.
    path('add/',BookmarkCreateView.as_view(),name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name ='detail'), # <int:pk> <컨버터:컨버터를 통해 반환 받은 값 or 변수명>
    path('update/<int:pk>/', BookmarkUpdateView.as_view(),name = 'update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(),name ='delete'),
    ]