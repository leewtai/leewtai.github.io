# Typesetting equations and code using Rstudio/RMarkdown

## RMarkdown within Rstudio
When you launch Rstudio, besides source files, you could
also create '.Rmd' files.

![launch new Rmd file](images/Rmd_newfile_rstudio.png)

This would launch a prompt that asks a default output, just choose HTML
to minimize dependencies on other software.

![Rmd new file prompt](images/rmd_newfile_prompt.png)

This should create a template file for you to easily
enter code vs LaTeX.

![Rmd demo file](images/rmd_demo_file.png)

The only piece that is missing is the mathematical equations.
In the usual text area, you can type in LaTeX code surrounded by
dollar signs `$` like `$\bar{Y}\to E(Y)$` to type out equations.

![Rmd math code example](images/rmd_math_code.png)

If you render the code, the math will look nice:

![Rmd math rendered example](images/rmd_math_rendered.png)

To tell Rstudio to output an HTML file, you have to `Knit` the
Rmd file to an HTML file. This will ask you where should the
Rmd and HTML file be saved.

![Rmd knit dropdown](images/rmd_knit_dropdown.png)

It usually takes a few second for the HTML file to appear.
You should see your Rstudio console do some work. The resulting
HTML file should be easily exported to a PDF file using your
Printer capabilities.

![Rmd knit html](images/rmd_knit_html.png)
