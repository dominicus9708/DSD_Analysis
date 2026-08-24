# CS-004 / Global Case 032 — Source Notes

Status: first-pass source lock complete.

## 1. MITRE CWE-89 — SQL injection as data/directive boundary failure

Source: https://cwe.mitre.org/data/definitions/89.html

CWE-89 describes a product that constructs SQL commands from externally influenced input without correctly neutralizing special elements. The resulting downstream SQL processor can interpret what upstream logic treated as ordinary user data as SQL syntax/directives.

MITRE's structured description explicitly frames this family as a data/directive boundary error: data and directives share one stream, and special elements can cause data to be interpreted as directives.

Source-native consequence for CS-004:

`upstream data role != guaranteed downstream directive role exclusion`.

## 2. OWASP SQL Injection Prevention — parameterized query separation

Source: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

OWASP recommends prepared statements / parameterized queries. The SQL code is defined separately and values are bound later. The point is structural: the database receives a distinction between query structure and parameter data rather than one concatenated mixed stream.

Source-native consequence:

`query syntax + bound data` is not equivalent to `one concatenated query string` merely because the rendered characters could look similar.

## 3. Python sqlite3 — placeholders bind Python values

Source: https://docs.python.org/3.15/library/sqlite3.html

The Python documentation warns against assembling SQL with Python string operations and directs callers to placeholders plus a separate parameters argument. `execute(sql, parameters)` therefore presents SQL structure and data values through different API positions.

Source-native consequence:

A value's admissibility as a Python string does not determine its syntactic role inside SQL. The API boundary can preserve it as a value by binding rather than reparsing it as SQL text.

## 4. OWASP XSS Prevention — output context determines encoding

Source: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

OWASP distinguishes HTML, HTML-attribute, JavaScript, CSS, and URL output contexts. Different contexts require different encoding/placement rules because browsers parse them differently. Some contexts should not receive untrusted variable data at all.

Source-native consequence:

`same string != same parser role across contexts`.

An upstream string that is legitimate display data does not carry a context-independent guarantee that it will remain text when inserted into markup or script syntax.

## 5. MDN — textContent versus innerHTML

Sources:
- https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent
- https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML

MDN distinguishes assigning text from assigning HTML. `textContent` replaces children with a text node. `innerHTML` invokes HTML parsing and is an injection sink when fed unsafe strings.

Source-native consequence:

The same host-language string can be treated as plain text by one sink and markup by another. The difference is downstream interpretation, not a change in the string's host-language type.

## 6. Python subprocess — argument list versus shell interpretation

Source: https://docs.python.org/3/library/subprocess.html

Python documents that subprocess calls do not implicitly invoke a system shell. When a shell is explicitly invoked (`shell=True`), the application becomes responsible for quoting whitespace and metacharacters. Passing a sequence of arguments is generally preferred because the API preserves argument boundaries.

Source-native consequence:

`ordinary process argument != shell command language fragment`.

A string does not have one operational meaning independent of whether it is passed as an argument or reparsed by a shell.

## Cross-source synthesis before DSD mapping

The three source families independently reject a context-free role model for strings/values:

- SQL: value versus query syntax;
- browser: text/data versus markup/script/URL/CSS syntax;
- process execution: argument versus shell syntax.

Surviving source-native distinction:

`upstream value/data status != downstream grammar/context != parsed role != operation semantics/effect`.

No DSD term is used to define these source-native distinctions.