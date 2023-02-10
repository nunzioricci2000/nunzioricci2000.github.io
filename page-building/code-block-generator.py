import re

keywords = [
        '#available',
        '#colorLiteral',
        '#column',
        '#dsohandle',
        '#else',
        '#elseif',
        '#endif',
        '#error',
        '#file',
        '#fileID',
        '#fileLiteral',
        '#filePath',
        '#function',
        '#if',
        '#imageLiteral',
        '#keyPath',
        '#line',
        '#selector',
        '#sourceLocation',
        '#warning',
        'Any',
        'Protocol',
        'Self',
        'Type',
        'any',
        'as',
        'associatedtype',
        'associativity',
        'break',
        'case',
        'catch',
        'class',
        'continue',
        'convenience',
        'default',
        'defer',
        'deinit',
        'didSet',
        'do',
        'dynamic',
        'else',
        'enum',
        'extension',
        'fallthrough',
        'false',
        'fileprivate',
        'final',
        'for',
        'func',
        'get',
        'guard',
        'if',
        'import',
        'in',
        'indirect',
        'infix',
        'init',
        'inout',
        'internal',
        'is',
        'lazy',
        'left',
        'let',
        'mutating',
        'nil',
        'none',
        'nonmutating',
        'open',
        'operator',
        'optional',
        'override',
        'postfix',
        'precedence',
        'precedencegroup',
        'prefix',
        'private',
        'protocol',
        'public',
        'repeat',
        'required',
        'rethrows',
        'return',
        'right',
        'self',
        'set',
        'some',
        'static',
        'struct',
        'subscript',
        'super',
        'switch',
        'throw',
        'throws',
        'true',
        'try',
        'typealias',
        'unowned',
        'var',
        'weak',
        'where',
        'while',
        'willSet'
]

code = """
public init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == Int
"""

for keyword in keywords:
        code = re.sub(rf'(\s)({ keyword })(\s)', r'\1<span class="keyword">\2</span>\3', code)

code = re.sub(r'(@[A-Za-z0-9]+)', r'<span class="wrapper">\1</span>', code)
code = re.sub(r'([^A-Za-z0-9])([A-Z][A-Za-z0-9]+)', r'\1<span class="type">\2</span>', code)


print(code)