from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

#from api.views.users import UserViewSet as myapp_users_views
from api.views.dashboards import DashboardViewSet as myapp_dashboards_views
from api.views.fileuploads import FileuploadListAPIView
from api.views.fileuploads import OlevelVsAlevelAndOlevelListAPIView
from api.views.fileuploads import level_Of_TutionlListAPIView
from api.views.fileuploads import Size_Of_SchoolsListAPIView
from api.views.fileuploads import Teacher_To_Student_RatioListAPIView
from api.views.fileuploads import Number_Of_EnroledSchoolsListAPIView
from api.views.fileuploads import Most_And_Least_Partner_SchoolsListAPIView


# router
router = routers.DefaultRouter()
#router.register(r'users', myapp_users_views)
router.register(r'dashboards', myapp_dashboards_views)




# swagger_view  FileUploadView
schema_view = get_swagger_view(title='SamaApp API')

urlpatterns = [
    path('docs/', schema_view),
    path('', include(router.urls)),
	path('o_level_vs_alevel_and_oleve/',OlevelVsAlevelAndOlevelListAPIView.as_view(), name='o_level_vs_alevel_and_oleve'),
	#path('level_of_tution/',level_Of_TutionlListAPIView.as_view(), name='level_of_tution'),
	#path('size_of_schools/',Size_Of_SchoolsListAPIView.as_view(), name='size_of_schools'),
	path('teacher_to_student_ratio/',Teacher_To_Student_RatioListAPIView.as_view(), name='teacher_to_student_ratio'),
	path('enrolled_schools/',Number_Of_EnroledSchoolsListAPIView.as_view(), name='enrolled_schools'),
	path('most_and_least_partner_schools/',Most_And_Least_Partner_SchoolsListAPIView.as_view(), name='most_and_least_partner_schools'),
	#path('fileuploads/',FileuploadListAPIView.as_view(), name='fileuploads'),
]
