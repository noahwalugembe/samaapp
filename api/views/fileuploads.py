
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from api.models.dashboards import Dashboard
from api.serializers.dashboards import DashboardSerializer

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

#import csv
import csv
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count
from django.db.models import Q

from datetime import datetime


	
class level_Of_TutionlListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    
    def get_queryset(self):
        queryset_results = queryset
        
    def get(self, request, *args, **kwargs): 
        queryset = Dashboard.objects.all().only("boarding_fee_S3", "day_fee_S3","boarding_fee_S5")
        
        return HttpResponse(queryset)
    
    #queryset =Dashboard.objects.filter('boarding_fee_S3','day_fee_S3,boarding_fee_S5')

    
    
    
	
class Size_Of_SchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    queryset =Dashboard.objects.filter(olevel_students='1')
	

    

class FileuploadListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()
	
    def get_queryset(self):
        queryset_results = queryset
		
    
    def get(self, request, *args, **kwargs):
	    #('C:/Users/NOAH1/Documents/samaapp/api/views/Book1.csv' )
        with open('C:/Users/NOAH1/Documents/samaapp/api/views/Book1.csv' ) as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:  
                date = datetime.strptime(row['date_school_enrolled'], "%m/%d/%Y") 
                d=datetime.strftime(date, "%Y-%m-%d")
                t= int(row['number_of_teachers'].strip())
                s= int(row['number_of_students'].strip())
                
                p = Dashboard(community_unit=row['community_unit'], school_id =row[ 'school_id'], name=row['name'],olevel_students=row[ 'olevel_students'],alevel_students=row['alevel_students'],boarding_students=row['boarding_students'],day_students=row['Day_students'], boarding_fee_S3=row['boarding _fee_for _S3'],day_fee_S3=row[ 'day_fee_S3'],boarding_fee_S5=row[ 'boarding_fee_S5'], day_fee_S5=row[ 'day_fee_S5'],female_students =row[ 'female_students'],male_students=row['male_students'], 
                              number_of_students=s,
                              number_of_teachers=t,
                              location=row['location'],
                              date_school_enrolled= d
				   ) 
                
               # p = Dashboard(community_unit=row[0], school_id =row[1], name=row[2],olevel_students=row[3],alevel_students=row[4],boarding_students=row[5],day_students=row[6], boarding_fee_S3=row[7],day_fee_S3=row[8],boarding_fee_S5=row[9], day_fee_S5=row[10],female_students =row[11],male_students=row[12], number_of_students=row[13],number_of_teachers=row[14],location=row[15],
                                  #        date_school_enrolled= d
                               # )                 
                p.save()
                
  

class OlevelVsAlevelAndOlevelListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
       
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        olevel_students=Dashboard.objects.filter(olevel_students='1').count()
        alevel_students=Dashboard.objects.filter(alevel_students='1',olevel_students='1').count()
    
        q = Dashboard.objects.annotate(num_authors=Count('olevel_students'))        
        return HttpResponse(olevel_students/alevel_students)
    
    
class Teacher_To_Student_RatioListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    queryset =Dashboard.objects.filter(olevel_students='1')
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        xnumber_of_students=Dashboard.objects.filter(number_of_students='1').count()
        xnumber_of_teachers=Dashboard.objects.filter(number_of_teachers='1').count()
        
        number_of_teachers=Dashboard.objects.aggregate(Sum('number_of_teachers'))  
        number_of_students=Dashboard.objects.aggregate(Sum('number_of_students'))
        
      
    
        
        return HttpResponse(number_of_students)
       
        
        
            
     
    

    

class Most_And_Least_Partner_SchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    num =Dashboard.objects.filter(olevel_students='1').count()
    
class Number_Of_EnroledSchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        
        num_schoole=Dashboard.objects.filter(number_of_students!="").count()
               
        return HttpResponse(num_schoole)    

    

