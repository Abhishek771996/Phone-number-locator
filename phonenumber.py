import phonenumbers

from phonenumbers import geocoder
# it will show the number location on map
import folium                                      
# it is the api key of open cage
key='01d4070bf657424c90a3fe7f9a36aee7'   

number=input('Enter your no with +__:') 

#it will show the  country of a sim
check_number=phonenumbers.parse(number)            
number_location=geocoder.description_for_number(check_number,'en')    
print(number_location)   


# it will show the first service provider
from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
car=carrier.name_for_number(service_provider,'en')  
print(car)


#install the opencage              
# provide the location of sim
from opencage.geocoder import OpenCageGeocode 
geocoder=OpenCageGeocode(key)
query=str(number_location)     
results=geocoder.geocode(query)  
# print(results)         

# this will show the longitute and latitute of a location
lat=results[0]['geometry']['lat']        
lng=results[0]['geometry']['lng']       
print(lat,lng)

# point out in map
map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)  
map_location.save('mylocation.html')

# show the time zone
from phonenumbers import timezone
car=phonenumbers.parse(number)
time=timezone.time_zones_for_number(car)
print(time)   




