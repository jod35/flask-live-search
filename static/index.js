const searchInput = document.querySelector("#search");

const resultDisplay = document.querySelector("#results");

let resultlistItems=[]

let new_item=null;

// resultDisplay.innerHTML="<h1>There are no results</h1>";

searchInput.addEventListener("input", () => {
  data = { username: searchInput.value };

  fetch("/search", {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((data) => {


      for(i of data.results){

        let new_item=document.createElement('li');
        
        new_item.innerText=`${i.username} - ${i.email}`;

        resultlistItems.unshift(new_item)

      }

      
    });

    console.log(resultlistItems);
});