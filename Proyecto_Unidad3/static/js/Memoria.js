const card = document.querySelectorAll('.cell')
const front = document.querySelectorAll('.front')
const container = document.querySelector('.container')
const score = document.querySelector('.score span')

const felicidades = document.querySelector('.felicidades img')




suffleImage()
clicking()
function suffleImage(){


    card.forEach(c=>{

        const num = [...Array(card.length).keys()]
        const random = Math.floor(Math.random()*card.length)

        c.style.order = num[random]
    })
}


function clicking(){

    for(let i =0; i<card.length; i++){


        front[i].classList.add('show')

        setInterval(() => {
            front[i].classList.remove('show')
        }, 2000);

        card[i].addEventListener('click' ,()=>{

            front[i].classList.add('flip')
           const filppedCard = document.querySelectorAll('.flip')

            if(filppedCard.length == 2){

                container.style.pointerEvents ='none'
                
                setInterval(() => {
                    
                    container.style.pointerEvents ='all'
                }, 1000);
 
                match(filppedCard[0] , filppedCard[1])
            }
        })
    }
}




function match(cardOne , cardTwo){

    if(cardOne.dataset.index == cardTwo.dataset.index){

        score.innerHTML = parseInt(score.innerHTML) + 1
       
        cardOne.classList.remove('flip') 
        cardTwo.classList.remove('flip') 

        document.getElementById("idfelicidades").style.visibility='hidden'
        document.getElementById("span").style.visibility='hidden'

        document.getElementById("score").value = score.innerHTML



        cardOne.classList.add('match')
        cardTwo.classList.add('match')

        if(score.innerHTML == 1){
            console.log("Termino el juego")
            document.getElementById("idfelicidades").style.visibility='visible'
            document.getElementById("container").style.visibility='hidden'
            document.getElementById("Rcali").style.visibility='visible'
        }

    }else{

        setTimeout(() => {
            
            cardOne.classList.remove('flip') 
            cardTwo.classList.remove('flip') 
        }, 1000);
    }
}