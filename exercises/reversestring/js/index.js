// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {
    
    // Solucion 1
    let a = str.split('').reverse().join('')
    // return a;    

    // Solucion 2
    let reverse = ''
    for (const char of str) {
        reverse = char + reverse
    }
    // return reverse

    // Solucion 3
    return str.split('').reduce((reverse, char) => char + reverse,'')

}
console.log(reverse('apple'))
module.exports = reverse;
