document.addEventListener('DOMContentLoaded', () => {
  //card options
  const cardArray = [
    {
      name: 'fries',
      img: 'https://thumbs.dreamstime.com/z/helado-de-gelato-dibujos-animados-italiano-gotas-vainilla-y-fresa-en-cono-gofre-ilustraci%C3%B3n-vectorial-clip-aislado-209107260.jpg'
    },
    {
      name: 'cheeseburger',
      img: 'images/cheeseburger.png'
    },
    {
      name: 'ice-cream',
      img: 'images/ice-cream.png'
    },
    {
      name: 'pizza',
      img: 'images/pizza.png'
    },
    {
      name: 'milkshake',
      img: 'images/milkshake.png'
    },
    {
      name: 'hotdog',
      img: 'images/hotdog.png'
    },
    {
      name: 'fries',
      img: 'https://thumbs.dreamstime.com/z/helado-de-gelato-dibujos-animados-italiano-gotas-vainilla-y-fresa-en-cono-gofre-ilustraci%C3%B3n-vectorial-clip-aislado-209107260.jpg'
    },
    {
      name: 'cheeseburger',
      img: 'images/cheeseburger.png'
    },
    {
      name: 'ice-cream',
      img: 'images/ice-cream.png'
    },
    {
      name: 'pizza',
      img: 'images/pizza.png'
    },
    {
      name: 'milkshake',
      img: 'images/milkshake.png'
    },
    {
      name: 'hotdog',
      img: 'images/hotdog.png'
    }
  ]

  cardArray.sort(() => 0.5 - Math.random())

  const grid = document.querySelector('.grid')
  const resultDisplay = document.querySelector('#result')
  let cardsChosen = []
  let cardsChosenId = []
  let cardsWon = []

  //create your board
  function createBoard() {
    for (let i = 0; i < cardArray.length; i++) {
      const card = document.createElement('img')
      card.setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkOnP1DQ2aQWD3BMH7icNTDHvPR8U3AB_nCihHL9lj3QlqwJo-aW7BVFXshj3PKhOvFSg&usqp=CAU')
      card.setAttribute('data-id', i)
      card.addEventListener('click', flipCard)
      grid.appendChild(card)
    }
  }

  //check for matches
  function checkForMatch() {
    const cards = document.querySelectorAll('img')
    const optionOneId = cardsChosenId[0]
    const optionTwoId = cardsChosenId[1]
    
    if(optionOneId == optionTwoId) {
      cards[optionOneId].setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkOnP1DQ2aQWD3BMH7icNTDHvPR8U3AB_nCihHL9lj3QlqwJo-aW7BVFXshj3PKhOvFSg&usqp=CAU')
      cards[optionTwoId].setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkOnP1DQ2aQWD3BMH7icNTDHvPR8U3AB_nCihHL9lj3QlqwJo-aW7BVFXshj3PKhOvFSg&usqp=CAU')
      alert('You have clicked the same image!')
    }
    else if (cardsChosen[0] === cardsChosen[1]) {
      alert('You found a match')
      cards[optionOneId].setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIbWL_sfVQPXo7q-DWJE0xyYyZFfcVhwsnDzrRhQx0SKVqlZ4K33BewqHz7cAC-Uky2LI&usqp=CAU')
      cards[optionTwoId].setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIbWL_sfVQPXo7q-DWJE0xyYyZFfcVhwsnDzrRhQx0SKVqlZ4K33BewqHz7cAC-Uky2LI&usqp=CAU')
      cards[optionOneId].removeEventListener('click', flipCard)
      cards[optionTwoId].removeEventListener('click', flipCard)
      cardsWon.push(cardsChosen)
    } else {
      cards[optionOneId].setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkOnP1DQ2aQWD3BMH7icNTDHvPR8U3AB_nCihHL9lj3QlqwJo-aW7BVFXshj3PKhOvFSg&usqp=CAU')
      cards[optionTwoId].setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkOnP1DQ2aQWD3BMH7icNTDHvPR8U3AB_nCihHL9lj3QlqwJo-aW7BVFXshj3PKhOvFSg&usqp=CAU')
      alert('Sorry, try again')
    }
    cardsChosen = []
    cardsChosenId = []
    resultDisplay.textContent = cardsWon.length
    if  (cardsWon.length === cardArray.length/2) {
      resultDisplay.textContent = 'Congratulations! You found them all!'
    }
  }

  //flip your card
  function flipCard() {
    let cardId = this.getAttribute('data-id')
    cardsChosen.push(cardArray[cardId].name)
    cardsChosenId.push(cardId)
    this.setAttribute('src', cardArray[cardId].img)
    if (cardsChosen.length ===2) {
      setTimeout(checkForMatch, 500)
    }
  }

  createBoard()
})
