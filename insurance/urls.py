
from django.urls import include,path
from rest_framework import routers
from insurance import views

router = routers.DefaultRouter()
router.register(r'riskname',views.RiskNameViewSet,'riskname')
router.register(r'riskdetail',views.RiskDetailsViewSet,'riskdetail')

urlpatterns = [
	path('',include(router.urls)),
	path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
	path('risk_details', views.test_vue)
]

