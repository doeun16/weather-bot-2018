# 1. 야외활동하기 좋은 날씨
# 비 x / 미세먼지 좋음/ 온도/최고온도가 25 미만 / 최저온도가 15

precipitation_probability < 60
int(fine_dust_concentration) <=30
hightest_ temperature <25
lowest_ temperature >15

# 2. 온도별 옷차림 기준

average_temperature = round((int(lowest_ temperature) + int(hightest_ temperature))/2 , 0)

if average_temperature >=28 :
    print(“민소매/반팔 + 반바지/치마를 추천합니다”)
elif average_temperature >= 24 and average_temperature<28 :
    print(“반팔/얇은 긴팔 + 반바지를 추천합니다”)
elif average_temperature >=20 and average_temperature<24 :
    print(“얇은 니트/가디건/긴팔티/후드티 + 면바지/슬랙스를 추천합니다”)
elif average_temperature >=17 and average_temperature<20 :
    print(“니트/가디건/맨투맨/ + 청바지/면바지/슬랙스/원피스를 추천합니다”)
elif average_temperature >= 11 and average_temperature<17:
    print(“자켓/셔츠/가디건/간절기 야상(안에 두꺼운 옷)을 추천합니다”)
elif average_temperature >= 6 and average_temperature<11:
    print(“코트/간절기 야상을 추천합니다”)
elif average_temperature >= 0 and average_temperature<6 :
    print(“코트/가죽자켓/패딩을 추천합니다”)
else:
    print(“두꺼운 코트/패딩/퍼를 추천합니다”)
#
# 3. 미세먼지 기준

def fine_dust_info(fine_dust_concentration, ) :
    if int(fine_dust_concentration) <=30:
        print( “좋음” )
    elif int(fine_dust_concentration) >30 and int(fine_dust_concentration) <=80 :
        print( “보통” )
    elif int(fine_dust_concentration) >80 and int(fine_dust_concentration) <=150 :
        print( “나쁨” )
    else :
        print( “매우 나쁨” )

# 4. 마스크 착용 기준
if int(fine_dust_concentration) >30 :
	print(“마스크 착용을 권고합니다”)

# 5. 우산 챙기는 기준
if int(precipitation_probability) >= 60:
    print(“우산을 챙기세요”)
