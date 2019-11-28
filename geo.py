import geoip2.database

read = geoip2.database.Reader("./GeoLite2-City.mmdb")

def get(ip):
    response  = read.city(ip)
    city      = response.city.name
    country   = response.country.name
    postal    = response.country.iso_code
    post_code = response.postal.code
    latitude  = response.location.latitude
    longitude = response.location.longitude

    print(f"[*] Target: {ip} Geo-located ~ {postal} ")
    print(f"[+] City: {city}, Country: {country}, Postal-Code: {post_code}")
    print(f"[+] Latitude: {latitude}, Longitude: {longitude}")

get(input("Enter the IP: "))
read.close()
