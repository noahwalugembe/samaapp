
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
from django.db import connection

from datetime import datetime
import json


	
class level_Of_TutionlListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    
    def get_queryset(self):
        queryset_results = queryset
        
    def get(self, request, *args, **kwargs): 
        
        
        cursor_boarding_fee_S3 = connection.cursor()
        cursor_boarding_fee_S3_avg = connection.cursor()
        
        cursor_day_fee_S3 = connection.cursor()
        cursor_day_fee_S3_avg = connection.cursor()     
        
        cursor_boarding_fee_S5 = connection.cursor()
        cursor_boarding_fee_S5_avg = connection.cursor()
    
        cursor_day_fee_S5 = connection.cursor()
        cursor_day_fee_S5_avg = connection.cursor()                
        
        cursor_boarding_fee_S3.execute("SELECT  name,boarding_fee_S3 FROM api_dashboard")
        cursor_boarding_fee_S3_avg.execute("SELECT  AVG(boarding_fee_S3) FROM api_dashboard")
        
        cursor_day_fee_S3.execute("SELECT  name,day_fee_S3 FROM api_dashboard")
        cursor_day_fee_S3_avg.execute("SELECT  AVG(day_fee_S3) FROM api_dashboard") 
        
        cursor_boarding_fee_S5.execute("SELECT  name,boarding_fee_S5 FROM api_dashboard")
        cursor_boarding_fee_S5_avg.execute("SELECT  AVG(boarding_fee_S5) FROM api_dashboard")
    
        cursor_day_fee_S5.execute("SELECT  name,day_fee_S5 FROM api_dashboard")
        cursor_day_fee_S5_avg.execute("SELECT AVG(day_fee_S5) FROM api_dashboard")  
        
        boarding_fee_S3 = cursor_boarding_fee_S3.fetchall() 
        boarding_fee_S3_json_data = json.dumps(boarding_fee_S3)  
        
        boarding_fee_S3_avg = cursor_boarding_fee_S3_avg.fetchall()
        boarding_fee_S3_avg_json_data = json.dumps(boarding_fee_S3_avg)  
        
        day_fee_S3 = cursor_day_fee_S3.fetchall()
        day_fee_S3_json_data = json.dumps(day_fee_S3)  
        
        day_fee_S3_avg = cursor_day_fee_S3_avg.fetchall()
        day_fee_S3_avg_json_data = json.dumps(day_fee_S3_avg)  
        
        boarding_fee_S5 = cursor_boarding_fee_S5.fetchall()
        boarding_fee_S5_json_data = json.dumps(boarding_fee_S5)  
        
        boarding_fee_S5_avg = cursor_boarding_fee_S5_avg.fetchall()
        boarding_fee_S5_avg_json_data = json.dumps(boarding_fee_S5_avg)  
    
        day_fee_S5 = cursor_day_fee_S5.fetchall()
        day_fee_S5_json_data = json.dumps(day_fee_S5)  
        
        day_fee_S5_avg = cursor_day_fee_S5_avg.fetchall()
        day_fee_S5_avg_json_data = json.dumps(day_fee_S5_avg )  
        
        data = {}
        data['boarding_fee_S3'] = boarding_fee_S3_json_data 
        data['boarding_fee_S3_avg'] =  boarding_fee_S3_avg_json_data
        
        data['day_fee_S3'] = day_fee_S3_json_data
        data['day_fee_S3_avg'] =  day_fee_S3_avg_json_data
       
        data['boarding_fee_S5'] =boarding_fee_S5_json_data 
        data['boarding_fee_S5_avg'] =  boarding_fee_S5_avg_json_data

        data['day_fee_S5'] = day_fee_S5_json_data
        data['day_fee_S5_avg'] =  day_fee_S5_avg_json_data       
        
        
        
        json_data = json.dumps(data)          
        
        
        
        
        
        
        
        
        
        return HttpResponse(json_data)
    
   
    

class FileuploadListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()
	
    def get_queryset(self):
        queryset_results = queryset
		
    
    def get(self, request, *args, **kwargs):
	    
        with open('C:/Users/NOAH1/Documents/samaapp/api/views/Book1.csv' ) as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:  
                date = datetime.strptime(row['date_school_enrolled'], "%m/%d/%Y") 
                d=datetime.strftime(date, "%Y-%m-%d")
                #t= int(row['number_of_teachers'].strip())
                #s= int(row['number_of_students'].strip())
                
                p = Dashboard(community_unit=row['community_unit'], school_id =row[ 'school_id'], name=row['name'],olevel_students=row[ 'olevel_students'],alevel_students=row['alevel_students'],boarding_students=row['boarding_students'],day_students=row['Day_students'], boarding_fee_S3=row['boarding _fee_for _S3'],day_fee_S3=row[ 'day_fee_S3'],boarding_fee_S5=row[ 'boarding_fee_S5'], day_fee_S5=row[ 'day_fee_S5'],female_students =row[ 'female_students'],male_students=row['male_students'], 
                              number_of_students=row['number_of_students'].strip(),
                              number_of_teachers=row['number_of_teachers'].strip(),
                              location=row['location'],
                              date_school_enrolled= d
				   ) 
                
                              
                p.save()
                
  

class OlevelVsAlevelAndOlevelListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
       
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        olevel_students=Dashboard.objects.filter(olevel_students='1').count()
        alevel_students=Dashboard.objects.filter(alevel_students='1',olevel_students='1').count()
    
        data = {}
        data['olevel_students'] = olevel_students
        data['olevel_students_and_alevel_students'] =  alevel_students
        json_data = json.dumps(data)              
        
         
        
        return HttpResponse(json_data)
    
    

       
        


    
class Number_Of_EnroledSchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        
        cursor = connection.cursor()
        
        cursor.execute("SELECT  COUNT(number_of_students) FROM api_dashboard")
        school_number = cursor.fetchall() 
        
        s=school_number.pop(0)
    
        data = {}
        data['schools'] = s
        
        json_data = json.dumps(data)       
             
        return HttpResponse(json_data)    
    
    
class Most_And_Least_Partner_SchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        
        cursor_min = connection.cursor()
        cursor_max = connection.cursor()
        
        #cursor.execute("SELECT community_unit, school_id,name FROM api_dashboard GROUP BY community_unit")
        cursor_min.execute("SELECT community_unit, COUNT(community_unit) as c FROM api_dashboard GROUP BY community_unit ORDER BY c ASC     LIMIT 1")
        cursor_max.execute("SELECT community_unit, COUNT(community_unit) as c FROM api_dashboard GROUP BY community_unit ORDER BY c DESC LIMIT 1")
        
        schools_min = cursor_min.fetchall()
        schools_max = cursor_max.fetchall() 
        
        #schools_min.append("min")
        #schools_max.append("max")
        
        jsonObjmin = json.dumps(schools_min)
        jsonObjmax = json.dumps(schools_max) 
        
        data = {}
        data['least'] =  schools_min
        data['most'] =  schools_max
        json_data = json.dumps(data)          
    
        return HttpResponse(json_data)  
    
class Size_Of_SchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()

    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        
        cursor = connection.cursor()
       
        
        #cursor.execute("SELECT name,number_of_students, (number_of_students* 100) /isnull (sum(number_of_students),0) as Total_Percentage FROM api_dashboard ")
       
        cursor.execute("SELECT name,CAST(number_of_students AS int) FROM api_dashboard ")
        

       
        school_percentage_level = cursor.fetchall() 
        
       
        
       # t=school_percentage_level.pop(0)
        #s=school_percentage_level.pop(1)
    
        #num_teachers = t[0]
        #num_students = int(s[1])        
        
        
        #tuple1 = []
        #tuple1.append(school_percentage_level)
        
        tuple1 = [('Duhaga Secondary School', 70), ('Green Hill Academy School', 120), ('Katuuso Community Secondary School', 24), ('Kitara Secondary School', 47), ('Light High School, Seguku', 50), ('Midland High School', 130), ('Nabumali High School', 120), ('Sir Tito Winyi Secondary School', 46), ('Taibah International School', 50), ('King James', 200), ('Lango College', 67), ('Rachelle Comprehensive School', 58), ('St. Katherine', 63), ("St. Paul's College, Mbale", 95), ('Aidan College', 150), ('Chemwania High School', 70), ('Gamatui Girls', 19), ('Iganga High School', 300), ('Iganga Secondary School', 157), ('Kabuwoko Secondary School', 50), ('Kako Senior Secondary School', 80), ('Kakungulu Memorial School', 220), ('Kapchorwa Secondary School', 70), ('Mbale Comprehensive High School', 250), ('Najjanankumbi Young Christian Secondary School', 73), ('Our Lady of Africa Secondary School, Namilyango', 200), ('Sebei College, Tegeres', 76), ("St. Andrew's Senior Secondary School", 40), ("St. John's Secondary School, Wakitaka", 100), ("St. Mary's College, Lugazi", 300), ('Victoria High School', 50), ('Wanyange Girls Secondary School', 120), ('Kalinabiri Secondary School, Ntinda', 105), ('Kitebi Secondary School', 250), ('Lubiri Senior Secondary School', 700), ('Mackay Memorial College School', 84), ('Sipi Secondary School', 42), ("St. Peter's Nsambya Secondary School", 200), ('Tropical High School, Nsambya', 135), ('Africana High School', 25), ('Alliance High School, Soroti', 32), ('Archbishop Kiwanuka Secondary School, Kitovu', 78), ('Asinge Secondary School', 48), ('Asuret Parents Senior Secondary School', 76), ('Atiri Secondary School', 13), ('Balawoli Senior Secondary School', 20), ('Bexhill High School', 29), ('Bilal Islamic Secondary School, Bwaise', 56), ('Bright College Nawanende Secondary School', 61), ('Bugiri High School', 65), ('Bugulumbya Secondary School', 15), ('Bukooli College, Bugiri', 138), ('Bukoyo Secondary School', 210), ('Bukulula Secondary School', 45), ('Busembatia Secondary School', 14), ('Busiu Secondary School', 48), ('Busoga College, Mwiri', 93), ('Busoga High School', 54), ('Busoga Senior Secondary School', 82), ('Buwunga Senior Secondary School', 9), ('Buzaya Secondary School', 15), ('Bweyogerere High School', 28), ('Caltec Academy', 126), ('Cardinal Nsubuga Secondary School, Nyenga', 65), ('Central View High School, Mukono', 30), ('Crane High School, Soroti', 86), ('Cross Roads Secondary School', 65), ('Eastland High School', 30), ('Equator College, Lugazi', 52), ('Excel High School, Mbikko', 25), ('Fairland High School', 40), ('Fairmount High School', 18), ('Forest Hill College', 61), ('Global Skills Secondary School, Nakulabye', 20), ('Gloryland Christian College', 22), ('Gloryland High School', 30), ('Good Heart Secondary School', 103), ('Green Hill College, Bulopa', 60), ('He Reigns Secondary School', 15), ('Helping Hand Secondary School, Tororo', 10), ('Hillside Secondary School, Kamuli', 70), ('Holy Cross Lake View Secondary School', 75), ('Hometek High School', 3), ('Honest Hill Secondary School', 85), ('Hope Community High School', 45), ('Iganga Parents Secondary School', 120), ('Iganga Progressive Secondary School', 138), ('Iki-Iki High School', 120), ('Iqra Secondary School, Jinja', 9), ('James Ochola Memorial Secondary School', 15), ('Jinja Parents School, Kagoma', 11), ('Jinja Progressive Secondary School', 527), ('Joy Dominion Academy, Musita', 24), ('Kabowa High School', 200), ('Kabukunge Muslim Secondary School', 20), ('Kakira High School', 73), ('Kakoola High School', 52), ('Kampala Apostolic Secondary School', 48), ('Kampala Citizens College School', 50), ('Kampala High School', 82), ('Kampala Secondary School', 180), ('Kamuda Parents Secondary School', 20), ('Kamuli College', 37), ('Kamuli Girls College', 20), ('Kamuli Progressive College', 100), ('Kapchorwa Parents School', 35), ('Kasambira High School', 11), ('Katerema Secondary School', 23), ('Katikamu SDA Secondary School', 50), ('Katwe Noor Secondary School', 24), ('Kawempe Muslim Secondary School', 15), ('Kawempe Royal College', 80), ('Kibuli Secondary School', 260), ('Kigulu College', 48), ('Kiira College, Butiki', 185), ('Kijjabwemi Secondary School', 96), ('Kingstone High School', 20), ('Kiribaki Secondary School', 30), ('Kisowera Secondary School', 60), ('Kisozi Progressive Secondary School', 10), ('Kololo High School', 40), ('Kubusa Secondary School', 20), ('Kyadondo Secondary School', 160), ('Lakeside Secondary School, Gayaza', 15), ('Liahona High School', 10), ('Light Secondary School, Kitoma', 17), ('Light Secondary School, Soroti', 120), ('London High School', 20), ('Lords Meade Vocational College', 31), ('Lugazi Mixed School, Naalya', 57), ('Lutengo United Secondary School', 30), ('Luzinga Secondary School', 30), ('Lwanda High School', 30), ('Lweru Senior Secondary School', 40), ('Apas Secondary School', 35), ('Magogo Secondary School', 45), ('Maluku Secondary School', 32), ('Manafwa High School', 180), ('Manjasi High School', 33), ('Mapeera Secondary School', 64), ('Marta Secondary School', 15), ('Masese Girls Boarding Secondary School', 10), ('Matuumu Secondary School', 35), ('Mazzoldi College, Nakaseke', 6), ('Mbale Secondary School', 683), ('Mbogo High School', 150), ('Mbogo Mixed Senior Secondary School', 230), ('Millenium Universal College', 12), ('Mirembe Islamic Secondary School', 10), ('Mukono High School', 120), ('Mukono Kings High School', 24), ('Mukono Parents High School', 48), ('Mukono Senior Secondary School', 6), ('Muljibhai Madhvani College, Wairaka', 60), ('Mulusa Academy, Wobulenzi', 140), ('Musese Secondary School', 35), ('Muterere Secondary School', 7), ('Nakalama Secondary School', 22), ('Nakaloke Islamic Secondary School', 60), ('Nakaloke Secondary School', 48), ('Nakanyonyi Girls Secondary School', 30), ('Nakigo Secondary School', 15), ('Namasagali College', 10), ('Namwezi Secondary School', 160), ('Nateete Muslim High School', 48), ('Nawanyago College', 20), ('Notre Dame High School', 45), ('Numasa Secondary School', 64), ('Nyondo Secondary School', 98), ('Okasha High School', 23), ('Olila High School', 48), ('Our Lady of Africa Secondary School, Mukono', 52), ('Pearl High School, Makindye', 56), ('Rena College, Mayuge', 102), ('Risah Standard Academy', 50), ('Rock High School', 341), ('Royal College, Kamuli', 45), ('Rubongi Army Secondary School', 90), ('Rubongi Secondary School', 9), ('Seeta College', 10), ('Seeta Senior Secondary School', 13), ('Soroti Community Secondary School', 94), ('St. Andrew Kaggwa Secondary School, Kasaala', 40), ("St. Andrew's Secondary School, Naminage", 100), ('St. Anthony Secondary School, Kayunga', 74), ('St. Benedict High School', 9), ('St. Charles Lwanga Secondary School', 45), ('St. Daniel Comboni College, Kasaala', 0), ('St. Gonzaga Secondary School, Kagoma', 10), ('St. John Bosco Secondary School, Kamuli', 15), ("St. John's Secondary School, Kabuwoko", 45), ("St. John's Secondary School, Nandere", 15), ('St. Kizito Secondary School, Katikamu Kisule', 80), ('St. Lawrence Secondary School, Idudi', 20), ("St. Luke's Secondary School, Mengo", 32), ('St. Mbuga Vocational Secondary School', 84), ('St. Micheal Vocational Secondary School', 11), ('St. Monica Girls Secondary School', 25), ('St. Monica High School, Kabuwoko', 5), ('St. Paul Secondary School, Mbulamuti', 30), ('St. Paul Secondary School, Nasuti', 50), ("St. Peter's College, Buweera", 65), ("St. Peter's, Ndiwulira Namugongo", 20), ('St. Stephen Secondary School, Soroti', 25), ("St. Stephen's Bugiri Secondary School", 22), ('St. Stephen Secondary School', 138), ('Standard Central College, Namwendwa', 100), ('Nkutu Memorial Secondary School', 200), ('Standard High School, Bulumagi', 45), ('Target Community College', 45), ('Teso College, Aloet', 180), ('Tororo Comprehensive Secondary School', 20), ('Tororo Universal College', 43), ('Trinity Secondary School, Nakibizzi', 25), ('Tropical College, Tororo', 12), ('Uganda Martyrs College, Ssonde', 27), ('Uganda Martyrs High School, Rubaga', 141), ('University Link High School', 108), ('Uplands High School', 40), ('Waitambogwe Secondary School', 55), ('Winston Stardard Secondary School', 56), ('Wobulenzi College School', 0), ('Wobulenzi Town Academy', 45), ('Yefe High School', 14), ('St. Denis Ssebugwawo Secondary School, Ggaba', 56), ("Giants' College, Luwero", 15), ('Luzira Secondary School', 170), ('Namakwa Senior Secondary School', 50), ('Paul Mukasa Secondary School, Kigunga', 60), ('St. Antonios Orthodox Secondary School, Monde', 13), ("St. Mary's College Kisubi", 140), ('Trinity Senior Academy', 70), ("Tororo Girls' School", 112), ("PMM Girls' School, Jinja", 250), ('Lira Town College', 250), ('Dr Obote College, Boroboro', 160), ('Comboni College, Lira', 39), ('Leo Atubo Secondary School', 24), ('Townside High School', 47), ('The Vision High School, Lira', 46), ('DJRA Comprehesive Secondary School', 52), ('St. Balikuddembe Secondary School, Kisoga', 50), ('Wakyato Seed Secondary School', 0), ('Bright Light College', 46), ("St. Peter's Secondary School, Magwa", 115), ('Namugongo Secondary and Vocational School', 0), ('Kawanda Secondary School', 0), ('Green Hill College, Mukono', 0), ('Joy Secondary School', 0), ('Jinja Secondary School', 0), ('Tororo Town College', 0), ('Gweri Secondary School', 0), ('Arua Secondary School', 0), ('Standard College Arua', 0), ('Ushindi Secondary School', 0), ('Kitgum High School', 0), ('Aboke High School', 0)]
        total = sum(t[1] for t in tuple1)
        tuple_new = [(x, float(y) * 100 /total) for x, y in tuple1]
        
        #tuple_new        
        jsonObj = json.dumps(tuple_new) 
             
        return HttpResponse(jsonObj)   

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

        cursor = connection.cursor()
        cursor_teachers = connection.cursor()
        cursor_students = connection.cursor()

        cursor_teachers.execute("SELECT  SUM(number_of_teachers) FROM api_dashboard")

        cursor_students.execute("SELECT  SUM(number_of_students) FROM api_dashboard")

        row_teachers = cursor_teachers.fetchall()  
        row_students = cursor_students.fetchall() 

        t=row_teachers.pop(0)
        s=row_students.pop(0)

        num_teachers = int(t[0])
        num_students = int(s[0])
        
        data = {}
        data['teachers'] =  num_teachers
        data['students'] =  num_students
        json_data = json.dumps(data)              


        return HttpResponse(json_data)

