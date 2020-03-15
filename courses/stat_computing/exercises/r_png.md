#### Exercises

- What happens if you call the `plot()` function twice and save it to a single file?
  ```r
  png('test.png')
  plot(1:4, 1:4, xlab="plot 1 x-axis")
  plot(4:1, 1:4, pch=16, xlab="x-axis plot 2")
  dev.off()
  ```
  Do they overlay, does the second one override the first, does the first prevent the second from being plotted?

