#1. tokenizer (词法分析器)
"""
'_Helo,World_'-->tokenizer-->[UNDERSCORE, TEXT='Helo,World', UNDERSCORE]
-->PARSER-->#<EmphasisText 'Helo,World'>
-->CODEGEN--?<em>Helo,World</em>
"""
#A token is just a name for the basic building blocks of our language.

#That parser will give us a tree data-structure representing our tokens organized in certain way.

class Token():
    def __init__(self,tp,value):
        self.type = tp
        self.value = value




























        
