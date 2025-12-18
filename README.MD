# **River** (*Python Pipeline*)

## Descriptioin 

**River** is a lightweight Python pipeline abstraction that lets you compose transformations using operators.

* `>>` passes the left-hand value into the next function in the pipeline
* `@` supplies arguments lazily, with `__` acting as a placeholder
* `_()` wraps a function into a River, making it usable inside a pipeline
* `== None` triggers evaluation
* Pipelines can nest, branch, and operate on arbitrary Python objects (including pandas)

It enables expressive, declarative data flows that read left-to-right like a DSL.

## Example: 

```python
x, y, z = 3, [1, 2, 3], pd.DataFrame({"beautiful_column": [1, 2, 3, 5]})
example1 = (y >> _(sum)@[__] ) == None
example2 = x >> _(sum)@[[__, __, __, __]] == None
example3 = (
    z >> _(pd.concat)
    @[[z, __]]@{"axis": 0}
    == None
)
```
