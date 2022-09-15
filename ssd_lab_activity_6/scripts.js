document.addEventListener('keydown', keyDownDarkMode)
function keyDownDarkMode(event){
    if ((event.ctrlKey || event.metaKey) && (event.key === "m" || event.key === "M")){
        toggleMode();
    }
}
function toggleMode(){
    if (document.body.style.backgroundColor == "white"){
        document.body.style.backgroundColor = "darkgray";
    }
    else{
        document.body.style.backgroundColor = "white";
    }
}
function checkSubmit(){
    var mname = document.getElementById("managername").value;
     
}