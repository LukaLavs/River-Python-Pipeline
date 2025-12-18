from src.river import (
    __, _,
)


if __name__ == "__main__":
    import pandas as pd 
    
    x, y, z = 3, [1, 2, 3], pd.DataFrame({"beautiful_column": [1, 2, 3, 5]})
    fib = lambda n: 0 if n == 0 else 1 if n == 1 else fib(n-1) + fib(n-2)
    example1 = (y >> _(sum)@[__] )== None
    example2 = x >> _(sum)@[[__, __, __, __]] == None
    example3 = (
        z >> 
          _(pd.concat)
          @[[z, __]]
          @{"axis": 0}
            == None
    )
    example4 = (
        y
        >> _(sum)@[__]
        >> _(lambda x: x + 5)@[__]
        >> _(lambda x: [fib(i) for i in range(x)])@[__]
        == None
    )
    example5 = (
        [1,2,3,4,5,6,7,8,9]
        >> _(filter)@[(lambda x: x % 2 == 0), __]
        >> _(list)@[__]
        >> _(map)@[(lambda x: x * x), __]
        >> _(list)@[__]
        >> _(sum)@[__]
        == None
    )
    example6 = (
        z
        >> _(lambda df: df.assign(double=df["beautiful_column"] * 2))@[__]
        >> _(lambda df: df[df["double"] > 4])@[__]
        >> _(pd.DataFrame.describe)@[__]
        == None
    )
    example7 = (
        5
        >> _(list)@[
            [
                _(lambda x: x * 2)@[__],
                _(lambda x: x ** 2)@[__],
                _(lambda x: x + 100)@[__]
            ]
        ]
         == None 
    )    
    example8 = (
        8
        >> _(lambda n: list(range(1, n + 1)))@[__]
        >> _(lambda xs: {
            "raw": xs,
            "stats": {
                "sum": sum(xs),
                "mean": sum(xs) / len(xs),
                "fib": [fib(i) for i in xs],
            },
            "powers": [
                {"x": x, "x2": x**2, "x3": x**3}
                for x in xs
            ]
        })@[__]
        >> _(lambda d: pd.DataFrame(d["powers"])
            .assign(
                fib=d["stats"]["fib"],
                centered=lambda df: df["x"] - d["stats"]["mean"]
            )
        )@[__]
        >> _(pd.concat)@[
            [
                __,
                _(lambda df: df.assign(
                    norm=lambda d: d["centered"] / d["centered"].abs().max()
                ))@[__]
            ]
        ]@{"axis": 1}
        >> _(lambda df: {
            "preview": df.head(3),
            "summary": df.describe(),
            "correlation": df[["x", "x2", "x3"]].corr()
        })@[__]
        == None
    )

    for i, example in enumerate([
        example1, example2, example3, example4, 
        example5, example6, example7, example8,
    ]): print(f"Example {i+1}:\n", example, "\n")
