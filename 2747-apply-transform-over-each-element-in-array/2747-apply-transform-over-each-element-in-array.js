/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    for (const [index, num] of arr.entries()) {
        arr[index] = fn(num, index);
    }
    return arr;
};