// Fetch data from DRF backend

// fetch('http://127.0.0.1:8000/note/', {
//     mode: "no-cors"
// })
// .then(res => {
//     return res
// })
// .then(data => {
//     return data
// });

var request = new Request('http://127.0.0.1:8000/note/?format=api');

fetch(request, {mode: 'no-cors'}).then(function(response) {
    // Convert to JSON
    return response;
}).then(function(j) {
    // Yay, `j` is a JavaScript object
    console.log(JSON.stringify(j));
}).catch(function(error) {
    console.log('Request failed', error)
});