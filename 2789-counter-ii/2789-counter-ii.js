/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var num = init;
    function increment(init) {
        console.log(num, "inc")
        return num += 1;
    };
    function decrement(init){
        console.log(num, "DEC")
        return num -= 1;
    }
    function reset() {
        num = init;
        console.log(num, "RESET")
        return num;
    }

    return {
        increment: increment,
        decrement: decrement,
        reset: reset,
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */