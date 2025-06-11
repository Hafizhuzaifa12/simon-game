let gameseq = [];
let userseq = [];
let btns = [ "yellow", "blue", "purple", "pink" ]; 
let gamestart = false;
let level = 0;
let p = document.querySelector("p");
document.addEventListener("keypress", function () {
    if (gamestart == false) {
        console.log("game is started");
        gamestart = true;
        levelup();
    }
});
function flashbtn(btn) {
    btn.classList.add("flash");
    setTimeout(function () {
        btn.classList.remove("flash");
    }, 250);
}
function flashuser(btn) {
    btn.classList.add("userflash");
    setTimeout(function () {
        btn.classList.remove("userflash");
    }, 250);
}

function levelup() {
    level++;
    userseq =[];
    p.innerText = `Level ${level}`;
    let redidx = Math.floor(Math.random() * btns.length); 
    let rdmclr = btns[redidx];
    let rdmbtn = document.querySelector(`.${rdmclr}`);
    gameseq.push(rdmclr);
    console.log(gameseq);
    flashbtn(rdmbtn);
}
function checkans (){
    let idx = userseq.length - 1;
 if (userseq[idx] === gameseq[idx]){
       if(userseq.length==gameseq.length){
        setTimeout(levelup,1000)
        // levelup()
       }
    }
    else{
        p.innerHTML = `Game Over! your score is <b> ${level}</b> <br>Try again ! Press any key to start`
        reset();
    }
     }
function btnpress() {
    let btn = this;
    flashuser(btn);
    userclr = btn.getAttribute("id");
    userseq.push(userclr);
    console.log(userclr)
    checkans();
}
let allbtns = document.querySelectorAll(".btn");
for (let btn of allbtns) {
    btn.addEventListener("click", btnpress);
}
function reset(){
    gamestart = false;
    gameseq  = [];
    userseq = [];
    level = 0
}
