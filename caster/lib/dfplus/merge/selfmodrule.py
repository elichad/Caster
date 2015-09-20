'''
Created on Sep 6, 2015

@author: synkarius
'''
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.actions2 import NullAction
from dragonfly.grammar.elements import Dictation


class SelfModifyingRule(MergeRule):
    '''
    SelfModifyingRule is a kind of rule which gets its command set changed
    on-the-fly based on some kind of user interaction. Child classes
    must implement their own version of the `refresh` method.
    '''
    def __init__(self, name=None, mapping=None, extras=None, defaults=None, 
        exported=None, context=None):
        MergeRule.__init__(self, name, mapping, extras, defaults, exported, context)
        self.refresh()
    
    def refresh(self, *args):
        '''Does stuff to get mapping, then calls self.reset()'''
        self.reset({ "default record rule spec": NullAction() })
    
    def reset(self, mapping):
        grammar = self._grammar # save reference because Grammar.remove_rule nullifies it
        if grammar is not None:
            grammar.unload() 
            grammar.remove_rule(self)
            
        extras = self.extras.values() if self.extras is not None and len(self.extras)>0 else [IntegerRefST("n", 1, 50), Dictation("s")]
        defaults = self.defaults if self.defaults is not None and len(self.defaults)>0 else {"n":1}
        MergeRule.__init__(self, self.name, mapping, extras, defaults, self.exported, self.context)
        
        if grammar is not None:
            grammar.add_rule(self)
            grammar.load()