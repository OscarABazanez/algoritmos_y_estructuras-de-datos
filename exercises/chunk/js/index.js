// --- Directions
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size
// --- Examples
// chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

function chunk(array, size) {
    // Solucion 1
    resultado = []
    for (let i = 0; i < array.length; i+=size) {
        if(i % size === 0){
            resultado.push(array.slice(i, i+size))
        }else{
            resultado.push(array[i])
        }
    }
    return resultado

    // Solucion 2
    const chunked = [];
    let index =0
    while(index < array.length){
        chunked.push(array.slice(index, index+size))
        index += size
    }
    return chunked
}
chunk([1, 2, 3, 4], 2)
chunk([1, 2, 3, 4, 5], 2)
module.exports = chunk;
