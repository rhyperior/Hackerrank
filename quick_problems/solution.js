function checkCashRegister(price, cash, cid) {

  const currency = ['ONE HUNDRED', 'TWENTY', 'TEN', 'FIVE', 'ONE', 'QUARTER', 'DIME', 'NICKEL', 'PENNY'] ;

  const currency_value = {
    'PENNY' : 0.01,
    'NICKEL' : 0.05,
    'DIME' : 0.1,
    'QUARTER': 0.25,
    'ONE': 1,
    'FIVE' : 5,
    'TEN' : 10,
    'TWENTY' : 20,
    'ONE HUNDRED' : 100
  }

  // console.log(currency.indexOf(''))

  // console.log(cid)
  cid.sort((a, b) => currency.indexOf(a[0])- currency.indexOf(b[0])) ;

  // console.log(cid)
  
  
  ;

  let change = cash - price ;

  const change_amount = [] ;

  for (let i = 0; i<currency.length; i++){
    if (change == 0){
      break ; 
    }
    else {
      if (change >= cid[i][1]){
        change -= cid[i][1] ;
        change_amount.push(cid[i][0], cid[i][1]) ;
        cid[i][1] = 0 ;
      }

      // currency_value[cid[i][0]
      else{
          if(Math.floor(change / currency_value[cid[i][0]]) > 0  ){
              change_amount.push([cid[i][0], Math.floor(change / currency_value[cid[i][0]]  ) * currency_value[cid[i][0]]] ) ;
console.log(change+'--'+cid[i][0])

              cid[i][1] -= Math.floor(change / currency_value[cid[i][0]]) *  currency_value[cid[i][0]];
              change -= Math.floor(change / currency_value[cid[i][0]]) *  currency_value[cid[i][0]] ;
          }  
          
      }
    }
  }
  // console.log(change)
  if (change > 0){
    console.log(change_amount)
    return {'status': 'INSUFFICIENT_FUNDS', 'change' : []}
  }
  else {
    for (let i = 0; i<currency.length; i++){
      console.log(cid[i][1]) ;
      if(cid[i][1] > 0){
        return {'status': 'OPEN', 'change' : change_amount}
      }
    }
  }
  // let change;
  return {'status': 'CLOSED', 'change' : cid};
}

// console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));
console.log(checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])) ;