
 let swap = function(a, b, array){
    let t = array[b] ;
    array[b] = array[a] ;
    array[a] = t;
    // console.log('yo')
  }
let partition = function (array, start, end){
  
    let i = start;
    let j = end - 1;
    let pivot = end;
    while (i<=j){
      if (array[i] >= array[pivot] && array[j] < array[pivot]){
        swap(i, j, array) ; 
        i += 1;
        j -= 1;
      }
      else if (array[i] >= array[pivot] && array[j] >= array[pivot]){
        j -= 1 ;
      }
      else if (array[i] < array[pivot] && array[j] < array[pivot]){
        i += 1 ;
      }
      else {
          i += 1;
          j -= 1;
      }
    }
    swap(i, pivot, array) ;
    // console.log(array) ;
    return i ;
  }

function quickSort(array, start, end) {
 
  if (start == undefined){
   start = 0;
    end = array.length - 1 ;
  }
  // console.log(start+ '--'+end)
  if (end - start < 1){
    // console.log('returning')
    return ;
  }
  let pivot = partition(array, start, end) ;
  // console.log(pivot) ;
  quickSort(array, start, pivot - 1);
  quickSort(array, pivot + 1, end) ;

  return array;
  // Only change code above this line
}

console.log(quickSort([3,2,1,6,5,5,1,4])) ;
