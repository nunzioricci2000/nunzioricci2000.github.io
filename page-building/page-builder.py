from typing import List

code == """

# 1. Wrappers

## 1.1. What wrappers do

Let’s say that we have a wrapper called `@Wrapper` what happens when you wrap a variable with it? 

```swift
@Wrapper var variable: Int
```

```swift
var _variable = Wrapper()
var variable: Int {
		get {
				_variable.wrappedValue
		}
		set {
				_variable.wrappedValue = newValue
		}
}
```

Two blocks above have pretty the same behavior. When we wrap a variable we are declaring that the var we are wrapping is a computed property that simply access to the wrappedValue property of a Wrapper instance. `_variable` is an effective variable that you can indeed use in the code (you can try with a state variables in SwiftUI).

## 1.2. But how can we create it?

Creating it is pretty simple you have to create an object in the such way:

```jsx
@propertyWrapper
struct Wrapper {
    var wrappedValue: Int = 0
}
```

As you can see is only a struct wrapped with propertyWrapper and with a property called wrappedValue. Obviously this is the variable we spoke about in the previous chapter, the one that you access by calling the wrapped variable.

But written like this isn’t really useful, right? So lets se a real use case:

```jsx
@propertyWrapper
struct Wrapper {
    var projectedValue: Int = 0
    
    var wrappedValue: Int {
        get { projectedValue }
        set { projectedValue = min(projectedValue, 100) }
    }
}
```

Now we declared a new property called `projectedValue` and the `wrappedValue` is a computed property that set projectedValue with `100` as max possible value.

Come on, now do a couple of tests and come back here as soon as you encounter any problems.

## 1.3 Set initial value

If you tried something like this:

```jsx
@Wrapper var variable = 0
```

You probably noticed that Xcode gives you this error: `Extra argument 'wrappedValue' in call`. If you remember the Chapter 1.1, when we wrap a variable we create an instance of the wrapper in the variable `_variable`. In this case when we give an initial value to the property this value is passed to the initializer of `Wrapper` in that way:

```jsx
@Wrapper var variable = 0
```

```jsx
var _variabe = Wrapper(wrappedValue: 0)
var variable: Int {
		get {
				_variable.wrappedValue
		}
		set {
				_variable.wrappedValue = newValue
		}
}
```

So we can update the wrapper in the previous chapter with our new knowledge:

```jsx
@propertyWrapper
struct HighScore {
    var projectedValue: Int
    
    var wrappedValue: Int {
        get { projectedValue }
        set { projectedValue = min(projectedValue, 100) }
    }
    
    init() {
        self.projectedValue = 0
    }
    
    init(wrappedValue: Int) {
        self.projectedValue = wrappedValue
    }
}
```

So now we created two new initializers: 

- The first one is the initializer that is called when you don’t get an initial value;
- The second one is the initializer that take the initial value and save it in the projectedValue.

## 1.4. Custom initializer

What if we want to pass custom values to our wrapper? If you already seen a wrapper like `AppStorage` you might have noticed that it accepts an attribute, es.:

```jsx
@AppStorage("highScore") var highScore: Int = 0
```

As you can see in the brackets we have a string that is passed to AppStorage initializer. How it works? If you are on Xcode you can do option+click on @AppStorage to see the definition and we can find this code:

```swift
/// Creates a property that can read and write to an integer user default.
///
/// - Parameters:
///   - wrappedValue: The default value if an integer value is not specified
///     for the given key.
///   - key: The key to read and write the value to in the user defaults
///     store.
///   - store: The user defaults store to read and write to. A value
///     of `nil` will use the user default store from the environment.
public init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == Int
```

From this you will have understood the mechanism: When you passing an argument to the wrapper is the same thing as passing to initializer. In the following scheme you will be able to see things more clearly:

![Senza nome.001.png](Understand%20@AppStorage%20through%20their%20procedural%20al%206d494de483c744698739206ed5a69c7e/Senza_nome.001.png)

"""

nil_chars = " \n\t"

elements = []

class State:
    parser: Parser = None

    def __init__(self, parser) -> None:
        self.parser = parser

    def perform(self, char: str) -> None:
        raise Exception("You can't use pure State class!")

class SearchingState:
    def perform(self, char: str) -> None:
        if char in nil_chars:
            return

class Parser:
    state: State = SearchingState()

    def parse(self, code: str) -> List[str]:
        for char in code:
            self.state.perform(char)
