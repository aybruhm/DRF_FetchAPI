// This script fetchs data from note_restapi backend and prepopulate the frontend

const request = new Request("http://127.0.0.1:8000/api/");

// Get lists of notes
fetch(request)
.then(res => res.json())
.then(data => console.log(data))
.catch(
    err => {
        console.log(err)
    }
)

// Retrieve a note

// Updates a note

// Deletes a note
