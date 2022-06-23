
const holes=document.querySelector(".board");

holes.addEventListener("click",()=>{
    function random(number) {
        return Math.floor(Math.random() * (number+1));
      }
    
        const rndCol = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')';
        
        elements = document.getElementsByClassName('hole');
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor=rndCol;
        }
});


