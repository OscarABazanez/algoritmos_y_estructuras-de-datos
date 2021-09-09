// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

function anagrams(stringA, stringB) {
    resultado = {}
    stringA = stringA.replace(/[^\w]/g,"").toLowerCase()
    stringB = stringB.replace(/[^\w]/g,"").toLowerCase()
    for(let char of stringA){
        resultado[char] = resultado[char] + 1 || 1
    }
    for(let char of stringB){
        if(!resultado[char]){
            return false
        }
        resultado[char] = resultado[char] +1
    }
    return Object.values(resultado).every((value) => value === 0)
}
anagrams('rail safety', 'fairy tales')
module.exports = anagrams;
