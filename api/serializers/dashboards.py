
from rest_framework.serializers import ModelSerializer

from api.models.dashboards import Dashboard


class DashboardSerializer(ModelSerializer):
    class Meta:
        model = Dashboard
        fields = (
                 'id','community_unit','school_id','name','olevel_students','alevel_students','boarding_students',
                 'day_students','boarding_fee_S3','day_fee_S3','boarding_fee_S5','day_fee_S5','female_students',
                 'male_students','number_of_students','number_of_teachers','location','date_school_enrolled'
	             )
		
