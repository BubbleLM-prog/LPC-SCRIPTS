1er Request
curl --request POST \
  --url https://www.virustotal.com/api/v3/urls \
  --header 'x-apikey: f5d6b96f4b5c6cfa0ed51193f872bafc9c078b74ab8156f4c80423eed2f8dc56' \
  --form url='https://www.instagram.com/?hl=es-la'

2do Request
curl --request GET \
  --url https://www.virustotal.com/api/v3/ip_addresses/{192.168.0.10} \
  --header 'x-apikey:f5d6b96f4b5c6cfa0ed51193f872bafc9c078b74ab8156f4c80423eed2f8dc56'

3er Request
curl --request POST \
  --url https://www.virustotal.com/api/v3/urls \
  --header 'x-apikey:f5d6b96f4b5c6cfa0ed51193f872bafc9c078b74ab8156f4c80423eed2f8dc56' \
  --form url='https://twitter.com/?lang=es
  '
