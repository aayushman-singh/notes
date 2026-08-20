import math, json

def haversine(lat1, lon1, lat2, lon2):
    R=6371.0
    dlat=math.radians(lat2-lat1)
    dlon=math.radians(lon2-lon1)
    a=math.sin(dlat/2)**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
    return 2*R*math.asin(math.sqrt(a))

def brute_geolocate(target_bearing, target_distance_km):
    best=None
    for lat in range(-60, 61, 5):
        for lon in range(-180, 181, 5):
            for cand_lat in range(-60, 61, 5):
                for cand_lon in range(-180, 181, 5):
                    dist=haversine(lat, lon, cand_lat, cand_lon)
                    if abs(dist-target_distance_km)<10:
                        best=(lat, lon, cand_lat, cand_lon, dist)
                        return best
    return best

if __name__=="__main__":
    result=brute_geolocate(0, 100)
    print(json.dumps({"found": result is not None, "location": result}))
