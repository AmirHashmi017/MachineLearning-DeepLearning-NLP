document.getElementById("addform").addEventListener("submit",function(e){
    e.preventDefault()
    let name=document.getElementById("name").value.trim();
    let description=document.getElementById("description").value.trim();

    if(name && description)
    {
        fetch('http://127.0.0.1:5000//tasks',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({name:name,description:description})
            
        }).then(response=>response.json()).then(data => {
            console.log("Server Response:", data);
            
        })
        .catch(error => {
            console.error("Error sending task:", error);
        });
    }
    location.reload()
})