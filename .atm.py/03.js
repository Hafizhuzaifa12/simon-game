let input = document.querySelector("input")
let btn = document.querySelector("button")
let ul = document.querySelector("ul")


btn.addEventListener("click" , function(){
     let item = document.createElement("li");
     item.innerText = input.value;
     let delbtn = document.createElement("button")
     delbtn.innerText= "delete"
     item.appendChild(delbtn)
     delbtn.classList.add("delete")


     ul.appendChild(item)
     input.value= "";
})  ;   
    ul.addEventListener("click",function(event){
     if (event.target.nodeName=="BUTTON") {
        let listitem = event.target.parentElement;
        listitem.remove();
     }  

    })

