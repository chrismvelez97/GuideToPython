#                           How to use OrderedDict

'''
We mentioned before that dictionaries are not in order
but python actually has a built in module that helps to
order dictionaries in the order in which we add keys.

You would import from collections OrderedDict
'''
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages["chris"] = "python"
favorite_languages["joe"] = "swift"
favorite_languages["michael"] = "javaScript"

for name, language in favorite_languages.items():
    print ("{0}'s favorite language is {1}!".format(name.title(), language.title()))

'''
Results:
Chris's favorite language is Python!
Joe's favorite language is Swift!
Michael's favorite language is Javascript!
'''
