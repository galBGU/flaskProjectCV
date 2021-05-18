let txt = "Gal Shaked";
let i = 0;
let speed = 60;

function loadEntryPage(){

    if (i<txt.length){
        document.getElementById("entry").innerHTML += txt.charAt(i);
        i++;
        setTimeout(loadEntryPage, speed)
    }
}

