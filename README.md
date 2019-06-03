# lab-sport-buildings-py

3rd Lab in Python

### Test REST

##### GET

<code>curl -v localhost:5000/sportBuildings</code>

<code>curl -v localhost:5000/sportBuildings/1</code>

##### POST

<code>curl -X POST localhost:5000/sportBuildings -H 'Content-type:application/json' -d '{"name":"Large Pool","location":"Central st 83","construction_year":2002,"viewers_number":800}'</code>

##### PUT

<code>curl -X PUT localhost:5000/sportBuildings/1 -H 'Content-type:application/json' -d '{"name":"Another Pool","location":"Silent st 83","construction_year":2000,"viewers_number":700}'</code>

##### DELETE

<code>curl -X DELETE localhost:5000/sportBuildings/1</code>
