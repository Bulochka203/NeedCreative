const temporaryDate = [{a:10 , b: true},{a:15, b:false},{a:10, b:false}];
var array = temporaryDate.find(el => el?.a === 10);
console.log(array);