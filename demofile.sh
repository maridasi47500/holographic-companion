
mkdir templates 
python3 scaffold.py user email username phone password country_id:references
python3 scaffold.py city name country_id:references
python3 scaffold.py cafe_bar name city_id:references
python3 scaffold.py cafe_drinks name user_id cafe_bar_id date time
python3 scaffold.py musicgenre name
python3 scaffold.py celeb name country_id:references musicgenre_id
python3 scaffold.py sport name season
python3 scaffold.py sportpracticed user_id sport_id city_id
python3 scaffold.py userwaypoints sportpracticed_id user_id lat lon cafe_bar_id:references
python3 scaffold.py userhasholographiccompanion celeb_id:references user_id waypoint_id
python3 scaffold.py street name city_id
python3 scaffold.py flat name_or_number street_id:references lat lon
python3 scaffold.py flathasuser user_id:references flat_id:references
python3 scaffold.py Flathasmusicgenre flat_id:references musicgenre_id:references
python3 scaffold.py musicalinstrument name
python3 scaffold.py Userplaysinstrument musicallinstrument-id user-id flat-id
python3 scaffold.py Flathasshopsnearby shopname lat lon
