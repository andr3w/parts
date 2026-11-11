fetch('/parts/api/parts')
    .then(r=>r.json())
    .then(r=>{
        console.log(r);
    })