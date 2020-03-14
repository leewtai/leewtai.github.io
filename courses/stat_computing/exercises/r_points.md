#### Exercises

- What happens if you run `points(illinois$year, illinois$yield_bu_per_ac)` **before**
  calling the `plot()` function
- What happens if you **try** to overwrite the axis labels with `points()`?
  ```r
  plot(idaho$year, idaho$yield_bu_per_ac,
       xlab='Year', ylab='Yield (bu/ac)',
       main='Idaho Corn Yields have Increased Since 2000',
       col="blue")
  points(illinois$year, illinois$yield_bu_per_ac,
         col="red", xlab="Years (from 2000)",
         ylab="Yield (bushel/acre)",
         main="Comparable yields")
  ```
