fetch('/parts/api/parts')
    .then(r=>r.json())
    .then(r=>{

        r.data.forEach(row=>{
            let tr = document.createElement('tr');
            let tdi = document.createElement('td');
            tdi.innerText = row.id;
            tr.appendChild(tdi);
            let tdd = document.createElement('td');
            tdd.innerText = row.description;
            tr.appendChild(tdd);
            document.getElementById('lop').appendChild(tr);
        })
    })