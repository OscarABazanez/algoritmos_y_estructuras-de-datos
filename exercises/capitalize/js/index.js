// --- Directions
// Write a function that accepts a string.  The function should
// capitalize the first letter of each word in the string then
// return the capitalized string.
// --- Examples
//   capitalize('a short sentence') --> 'A Short Sentence'
//   capitalize('a lazy fox') --> 'A Lazy Fox'
//   capitalize('look, it is working!') --> 'Look, It Is Working!'

function capitalize(str) {
    // # Solucion1
    // str = str.split(' ')
    // let comple = []
    // for (var i = 0; i < str.length; i++) {
    //     start = str[i].slice(0,1).toUpperCase()
    //     end = str[i].slice(1)
    //     comple.push(start + end+' ')
    // }
    // return comple.join('')

    // Solucion 2
    // words = []
    // for(let word of str.split(' ')){
    //     words.push(word[0].toUpperCase() + word.slice(1))
    // }
    // console.log(words.join(' '))
    // return words.join(' ')

    // Solucion 3
    let result = str[0].toUpperCase()

    for(let i = 1; i < str.length; i++) {
        if(str[i-1] === ' '){
            result += str[i].toUpperCase()
        }else{
            result += str[i]
        }
    }
    // console.log(result)
    return result
}


capitalize('a short centence')
capitalize('i love breakfast at bill miller bbq')
module.exports = capitalize;
