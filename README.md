# XmlEnglishTagCommenter
 A specialized tool I made to help with the Hebrew translation of Rimworld.

## What does it do?
The code takes an xml file (or any file with tags in it) and makes it so that any tag with english in it (<Tag>English in tag</Tag>) will have it's contents copied to a comment that will be made above it with a prefix of "EN: ".
### Example
file "Example.xml:"
```xml
<TagWithEnglish>English</TagWithEnglish>
<TagWithHebrew>עברית</TagWithHebrew>
<!-- EN: A comment-->
<TagWithAComment>A comment</TagWithAComment>
```
After the code has finished running, the file will look like this:
```xml
<!-- EN: English -->
<TagWithEnglish>English</TagWithEnglish>
<TagWithHebrew>עברית</TagWithHebrew>
<!-- EN: A comment-->
<TagWithAComment>A comment</TagWithAComment>
```

 ## Use:
- Ensure that you have python installed on your machine, it will not work otherwise.
- Open the Commenter.py file inside the repository.
 - You can open it in the cmd or through the file explorer, it doesn't matter.
- Input the file's path.
- For developers: You can call the function through python code by importing the file.

# General remarks:
As specified inside the code, I take no responsibility for any actions the code has done. *USE AT YOUR OWN RISK*.<br/>
I hope that it might help others, it surely helped me.<br/>

## Next
Perhaps I will make a version of it in another language so that Python would not be required to run it but I do not promise a thing.
