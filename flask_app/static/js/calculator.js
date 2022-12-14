// output variables to show the data
const calories = document.getElementById('calories');
const carbs = document.getElementById('carbs');
const fat = document.getElementById('fat');
const protein = document.getElementById('protein');

function calculate(){
  const activityLevel = document.querySelector('#activityLevel');
  const weight = document.querySelector('#weight');
  const goal = document.querySelector('#goal');

//Checks to see if the user is entering valid data, if not then alerts
  if(activityLevel.value == ''){
    if(goal.value == '' && weight.value == ''){
      alert('Please Input All Values')
      return;
    }
    else if(goal.value == ''){
      alert('Please Select An Activity Level and Goal')
      return;
    }
    else if(weight.value == ''){
      alert('Please Select An Activity Level And Input Weight')
      return;
    }
    else{
      alert('Please Select An Activity Level');
      return;
    }
  }
  if(goal.value == ''){
    if(weight.value == ''){
      alert('Please Select A Goal And Input Weight')
      return;
    }
    else{
      alert('Please Select A Goal')
      return;
    }
  }
  if(weight.value == ''){
    alert('Please Select Provide A Weight');
    return;
  }
//Calls the functions based on the user input data 
  if(goal.value == -1){
    loseWeight();
  }
  else if(goal.value == 0){
    maintainWeight();
  }
  else{
    gainWeight();
  }
}

// calculations for people who want to lose weight 
function loseWeight(){
  totalCalories = (activityLevel.value - 1) * weight.value;
  totalProtein = Math.floor(weight.value * 1.05);
  totalFat = Math.floor(weight.value * 0.35);
  
  calorieDiff = totalCalories - (totalFat * 9) - (totalProtein * 4);
  totalCarb = Math.floor(calorieDiff / 4);

//Calorie count up feature
  let calorieCounter = 800;
  setInterval(() => {
    if(calorieCounter == totalCalories){
      clearInterval();
    }
    else{
      calorieCounter++;
      calories.innerHTML = calorieCounter;
    }
  }, 2);

  let carbCounter = 0;
  setInterval(() => {
    if(carbCounter == totalCarb){
      clearInterval();
    }
    else{
      carbCounter++;
      carbs.innerHTML = carbCounter;
    }
  }, 28);

  let fatCounter = 0;
  setInterval(() => {
    if(fatCounter == totalFat){
      clearInterval();
    }
    else{
      fatCounter++;
      fat.innerHTML = fatCounter;
    }
  }, 110);

  let proteinCounter = 0;
  setInterval(() => {
    if(proteinCounter == totalProtein){
      clearInterval();
    }
    else{
      proteinCounter++;
      protein.innerHTML = proteinCounter;
    }
  }, 37);
}

// calculations for people who want to maintain weight 
function maintainWeight(){
  totalCalories = activityLevel.value * weight.value;
  totalProtein = Math.floor(weight.value * 0.9);
  totalFat = Math.floor(weight.value * 0.35);
  
  calorieDiff = totalCalories - (totalFat * 9) - (totalProtein * 4);
  totalCarb = Math.floor((calorieDiff / 4));

  //Calorie count up feature
  let calorieCounter = 800;
  setInterval(() => {
    if(calorieCounter == totalCalories){
      clearInterval();
    }
    else{
      calorieCounter++;
      calories.innerHTML = calorieCounter;
    }
  }, 2);

  let carbCounter = 0;
  setInterval(() => {
    if(carbCounter == totalCarb){
      clearInterval();
    }
    else{
      carbCounter++;
      carbs.innerHTML = carbCounter;
    }
  }, 25);

  let fatCounter = 0;
  setInterval(() => {
    if(fatCounter == totalFat){
      clearInterval();
    }
    else{
      fatCounter++;
      fat.innerHTML = fatCounter;
    }
  }, 130);

  let proteinCounter = 0;
  setInterval(() => {
    if(proteinCounter == totalProtein){
      clearInterval();
    }
    else{
      proteinCounter++;
      protein.innerHTML = proteinCounter;
    }
  }, 50);
}

// calculations for people who want to gain weight
function gainWeight(){
  totalCalories = (activityLevel.value * weight.value) + 250;
  totalProtein = weight.value;
  totalFat = Math.floor(weight.value * 0.4);
  
  calorieDiff = totalCalories - (totalFat * 9) - (totalProtein * 4);
  totalCarb = Math.floor((calorieDiff / 4));

  //Calorie count up feature
  let calorieCounter = 800;
  setInterval(() => {
    if(calorieCounter == totalCalories){
      clearInterval();
    }
    else{
      calorieCounter++;
      calories.innerHTML = calorieCounter;
    }
  }, 2);

  let carbCounter = 0;
  setInterval(() => {
    if(carbCounter == totalCarb){
      clearInterval();
    }
    else{
      carbCounter++;
      carbs.innerHTML = carbCounter;
    }
  }, 26);

  let fatCounter = 0;
  setInterval(() => {
    if(fatCounter == totalFat){
      clearInterval();
    }
    else{
      fatCounter++;
      fat.innerHTML = fatCounter;
    }
  }, 125);

  let proteinCounter = 0;
  setInterval(() => {
    if(proteinCounter == totalProtein){
      clearInterval();
    }
    else{
      proteinCounter++;
      protein.innerHTML = proteinCounter;
    }
  }, 50);
}