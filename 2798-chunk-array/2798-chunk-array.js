/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    if (!arr.length) {
        return []
    }
    const res = []
    let arrChunk = []
    for (let i = 0; i < arr.length; i++) {
        arrChunk.push(arr[i]);
        if (arrChunk.length === size || i === arr.length - 1) {
            res.push(arrChunk);
            arrChunk = [];
        }
    }
    return res;
};