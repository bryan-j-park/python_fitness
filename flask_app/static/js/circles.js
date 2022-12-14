

let totalCal = document.getElementById('totalCal');
let totalCal_counter = 0;
setInterval(() => {

  if(totalCal_counter == 100){
    clearInterval();
  }
  else{
    totalCal_counter++;
    totalCal.innerHTML = totalCal_counter + '%';
  }
}, 20);


let totalCarb = document.getElementById('totalCarb');
let totalCarb_counter = 0;
setInterval(() => {
  if(totalCarb_counter == 50){
    clearInterval();
  }
  else{
    totalCarb_counter++;
    totalCarb.innerHTML = '~' + totalCarb_counter + '%';
  }
}, 40);


let totalFat = document.getElementById('totalFat');
let totalFat_counter = 0;
setInterval(() => {
  if(totalFat_counter == 25){
    clearInterval();
  }
  else{
    totalFat_counter++;
    totalFat.innerHTML = '~' + totalFat_counter + '%';
  }
}, 80);

let totalProtein = document.getElementById('totalProtein');
let totalProtein_counter = 0;
setInterval(() => {
  if(totalProtein_counter == 25){
    clearInterval();
  }
  else{
    totalProtein_counter++;
    totalProtein.innerHTML = '~' + totalProtein_counter + '%';
  }
}, 80);