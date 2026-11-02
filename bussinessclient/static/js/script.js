// alert("hiii team")

const mobileIcon = document.getElementById("myMenu");
let myMenubox = document.getElementById("menuShow");

mobileIcon.addEventListener("click",()=>{
    // myMenubox.classList.add("show")
    // myMenubox.classList.remove("show")
    myMenubox.classList.toggle("show")
    if(myMenubox.classList.contains("show")){
        mobileIcon.classList.add("bi-x-lg")
        mobileIcon.classList.remove("bi-list")
    }
    else{
         mobileIcon.classList.remove("bi-x-lg")
        mobileIcon.classList.add("bi-list")
    }
})