

#########
#规则
#########
class Rule:
    """"能识别自己适用于哪种块; 能对块进行转换"""
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True # 是否应该停止处理当前块


class HeadingRule(Rule):
    """
    A heading is a single line that is at most 70 characters and
    that doesn't end with a colon.
    """
    type = 'heading'
    def condition(self, block):
        return block.lstrip().startswith('#')
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block.strip()[1:])
        handler.end(self.type)
        return True
    
class H2Rule(Rule):
    type = 'h2'
    def condition(self, block):
        return block.lstrip().startswith('##')
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block.strip()[2:])
        handler.end(self.type)
        return True

    
class H3Rule(Rule):
    type = 'h3'
    def condition(self, block):
        return block.lstrip().startswith('###')
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block.strip()[3:])
        handler.end(self.type)
        return True
    

class TitleRule(HeadingRule):
    """
    The title is the first block in the document, provided that it is a heading.
    """
    type = 'title'
    def condition(self, block):
        return block.lstrip().startswith('{')
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block.strip()[1:-1])
        handler.end(self.type)
        return True

class ListItemRule(Rule):
    """
    A list item is a paragraph that begins with a hyphen. As part of
    the formatting, the hyphen is removed.
    """
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """
    A list begins between a block that is not a list item and a
    subsequent list item. It ends after the last consecutive list
    item.
    """
    type = 'list'
    inside = False
    def condition(self, block):
        return True
    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

    
class ParagraphRule(Rule):
    """
    A paragraph is simply a block that isn't covered by any of the
    other rules.
    """
    type = 'paragraph'
    def condition(self, block):
        return True

import html,pdb

class CodeRule(Rule):
    type = 'code'
    def condition(self, block):
        return block.startswith("```")
    def action(self, block, handler):
        handler.start(self.type)
        block.replace('\t', '    ')
        block = html.escape(block)
        #pdb.set_trace()
        handler.feed(block[3:-3].strip())
        handler.end(self.type)
        return True

