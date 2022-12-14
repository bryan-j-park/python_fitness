let number = document.getElementById('dailyGoal');
let counter = 0;
setInterval(() => {
  if(counter == 65){
    clearInterval();
  }
  else{
    counter++;
    number.innerHTML = counter + '%';
  }
}, 30);

// Function runs when the form on dash/index is submitted 
function search(event){
  event.preventDefault();
  const searchForm = document.getElementById('searchForm');
  const form = new FormData(searchForm);

  fetch('http://127.0.0.1:5000/call_api', {method: 'POST', body:form})
  .then(res => res.json())
  .then(res => {
    measurementValue();
    nutritionValues(res);
  })
  .catch(err => {
    console.log('Somthing went wrong');
    console.log(err);
  })
}

// Assigns values to the HTML tag wtih ID "food" depending on if "measurement" is present
function measurementValue(){
  const amount = document.querySelector('#amount');
  const measurement = document.querySelector('#measurement');
  const ingr = document.querySelector('#ingr');
  
  if(measurement.value == "null"){
    let food = document.querySelector('#food');
    food.value = `${amount.value} ${ingr.value}`;
  } else{
    let food = document.querySelector('#food')
    food.value = `${amount.value} ${measurement.value} ${ingr.value}`;
  }
}

// Assigns values from API to the HTML tags in the nutrition information section of the index/dashboard
function nutritionValues(res){
  let calories = document.querySelector('#calories');
  calories.value = res.calories;

  let fat = document.querySelector('#fat');
  fat.value = Math.floor(res.totalNutrients.FAT.quantity);

  let carbs = document.querySelector('#carbs');
  carbs.value = Math.floor(res.totalNutrients.CHOCDF.quantity);

  let protein = document.querySelector('#protein');
  protein.value = Math.floor(res.totalNutrients.PROCNT.quantity);
}

