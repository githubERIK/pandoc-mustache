# pandoc-mustache: Variable Substitution in Pandoc

> This repo is forked from <https://github.com/BayLibre/pandoc-mustache> which is
a fork of <https://github.com/michaelstepner/pandoc-mustache.**>.

The **pandoc-mustache** filter allows you to put variables into your pandoc document text, with their values stored in a separate file. When you run `pandoc` the variables are replaced with their values.

_Technical note:_ This pandoc filter is not a complete implementation of the [Mustache template spec](https://mustache.github.io/). Only variable replacement is supported: other [tag types](https://mustache.github.io/mustache.5.html#TAG-TYPES) are not currently supported.

## Example

This document, in `document.md`:

```
---
mustache: ./le_gaps.yaml
---
The richest American men live {{diff_le_richpoor_men}} years longer than the poorest men,
while the richest American women live {{diff_le_richpoor_women}} years longer than the poorest women.
```

Combined with these variable definitions, in `le_gaps.yaml`:

```yaml
diff_le_richpoor_men: "14.6"
diff_le_richpoor_women: "10.1"
```

Will be converted by `pandoc document.md --filter pandoc-mustache` to:

> The richest American men live 14.6 years longer than the poorest men, while the richest American women live 10.1 years longer than the poorest women.

## Usage

1. Within a pandoc document, variables are referenced by enclosing the variable name in double "mustaches", i.e. curly brackets, like `{{this}}`.

2. The variables are defined in one or more separate files, using YAML formatted key-value pairs. For example:

   ```yaml
   place: Montreal
   temperature: "7"
   ```

3. The pandoc document containing the mustache variables points to the YAML file (or files) which contain the variable definitions. These files are indicated using the mustache field in a [YAML metadata block](https://pandoc.org/MANUAL.html#metadata-blocks), typically placed at the top of the pandoc document. Absolute paths and relative paths are supported: relative paths are evaluated relative to the working directory where `pandoc` is being run.

   An example:

   ```yaml
   ---
   title: My Report
   author: Jane Smith
   mustache: ./vars.yaml
   ---
   The temperature in {{place}} was {{temperature}} degrees.
   ```

   Or, with more than one file:

   ```yaml
   ---
   title: My Report
   author: Jane Smith
   mustache:
     - ./vars.yaml
     - ./additional_vars.yaml
   ---
   The temperature in {{place}} was {{temperature}} degrees.
   The humidity was {{humidity}}%.
   ```

4. Run pandoc and replace all variables in the document with their values by adding `--filter pandoc-mustache` to the pandoc command.

### Tips and Tricks

- When defining variables in YAML, there is no need to enclose strings in quotes. But you should enclose numbers in quotes if you want them to appear in the document using the exact same formatting. Some examples:

  ```yaml
  unquoted_string: Montreal # becomes: Montreal
  quoted_string: "Montreal" # becomes: Montreal
  trailingzero_num: 7.40 # becomes: 7.4
  trailingzero_string: "7.40" # becomes: 7.40
  ```

- If you're writing a document that reports computed numerical results, you can program your code (in R, Python, Stata, etc.) to write those numbers to a YAML file automatically each time they are generated. By referencing your numerical results using variables instead of hard-coding them into the text, the document can be updated instantly if the results change. And you can be certain that all the numbers in the output document reflect the latest results of your analysis.

## License

All of the files in this repository are released to the public domain under a [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/) to permit the widest possible reuse.
