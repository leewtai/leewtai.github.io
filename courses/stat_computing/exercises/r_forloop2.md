#### Exercises

- Given an arbitrary vector `arb_vec <- 1:10`
  Please use a for-loop to calculate the sum over each
  element in `arb_vec`
  - Hint: the sum over 10 numbers can be thought as the sum
    over 9 numbers plus the remaining number
- Challenge, write the above for-loop in 2 different ways, depending
  how you solved the problem above, one strategy lets the `i` value
  take on the values within `arb_vec` where one strategy let's `i`
  increment from 1 until the length of `arb_vec` (likely you have code
  that looks like `arb_vec[i]`). Please try to write the loop above
  in the strategy that you did not employ!
- Given arbitrary vector with random length, this
  can be achieved using this code: `arb_vec <- runif(sample(100, 1))`.
  (Don't worry if you don't understand this line yet)
  How could you calculate the length of `arb_vec` without using the
  function `length()` and only using a for-loop over the values
  of `arb_vec`?


