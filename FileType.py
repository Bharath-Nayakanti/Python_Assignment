Filename = input('Input the Filename:')
extention = Filename.split('.')[-1]

Languagename = {

    "py": "Python",
    "cpp": "C++",
    "java": "Java",
    "js": "JavaScript",
    "rb": "Ruby",
    "php": "PHP",
    "html": "HTML",
    "css": "CSS",
    "c": "C",
    "h": "C",
    "pl": "Perl",
    "sh": "Bash",
    "go": "Go",
    "swift": "Swift",
    "kt": "Kotlin",
    "rs": "Rust",
    "scala": "Scala",
    "groovy": "Groovy",
    "ts": "TypeScript",
    "tsx": "TypeScript",
    "jsx": "JavaScript",
    "m": "Objective-C",
    "mm": "Objective-C++",
    "r": "R",
    "lua": "Lua",
    "perl": "Perl",
    "coffee": "CoffeeScript",
    "dart": "Dart",
    "json": "JSON",
    "yml": "YAML",
    "yaml": "YAML",
    "xml": "XML",
    "sh": "Bash",
    "bash": "Bash",
    "zsh": "Zsh",
    "fish": "Fish",
    "bat": "Batch",
    "cmd": "Batch",
    "ini": "INI",
    "toml": "TOML",
 }


if extention in Languagename :
    language = Languagename[extention] 
    print('The Extention of the file is : ', language)
else :
    print("Unkown FileType")

    # To define the extention to language name dictionary

