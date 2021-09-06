// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
    // let total = {}
    // for(let i of str){
    //     total[i] = total[i] + 1 || 1
    // }
    // return Object.keys(total).reduce((previous, next) => total[previous] > total[next] ? previous : next);

    const charMaps = {}
    let max = 0
    let maxChar = ''
    for(let char of str){
        if(charMaps[char]){
            charMaps[char] ++
        }else{
            charMaps[char] = 1
        }
    }

    for(let char in charMaps){
        if(charMaps[char] > max){
            max= charMaps[char]
            maxchar = char
        }
    }
    
    return maxchar
}

console.log(maxChar("abcccccccd"))
// console.log(maxChar("apple 1231111"))
module.exports = maxChar;
