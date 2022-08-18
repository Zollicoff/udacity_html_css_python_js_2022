test.forEach(function(item, index){
  if(item%3===0){
      test[index]=test[index]+100;
  }
});
console.log(test);