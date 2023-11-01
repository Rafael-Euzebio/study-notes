# HTML
HTML (Hypertext Markup Language) is a markup language, the one interpreted by web browsers to show Web Pages

## Syntax
HTML consists of Tags, attributes and text  
A tag indicates how the text between the tags must be rendered  
An attribute changes the behavior of a tag  

This is a default html document
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
        <h1> Hello, World </h1>
    </body>
</html>
```

- `<html>` ..... `</html>`
    - Everything between the tag is `html` language
    - `<head>` .... `</head>`
        - Contains information about the page
        - `<title>` `</title>`
            - Page title
        - `<meta charset="UTF-8>"`
            - Metadata, page uses UTF-8 Character Encoding
        - `<meta name = "viewport" content = "width=device-width, initial-scale=1"`
            - Metadata, page dimensions equals to the device dimensions
        - `<meta href="css/style.css" rel="stylesheet"`
            - Metadata, link to a `.css` file
    - `<body>` .... `</body>`
        - Actual page contents
        - `<h1>` Hello, World `</h1>`
            - Displays "Hello, World"

This structure represents a Tree, each tag is a node in that tree, with one or more children. This html structure is called [[CS50x HTML DOM]]

