// Fetch data from DRF backend

var request = new Request('http://127.0.0.1:8000/note/');


fetch(request).then(res => {
    return res.json()
})
.then(data => {
    console.log(data)
});