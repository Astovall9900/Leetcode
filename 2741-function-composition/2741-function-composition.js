/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        if (!functions.length) {
            return x
        };
        let n = x;
        for (let i = functions.length - 1; i >= 0; i--) {
            n = functions[i](n);
        }
        return n;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */