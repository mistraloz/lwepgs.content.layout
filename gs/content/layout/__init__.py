# -*- coding: utf-8 -*-
from zope.i18nmessageid import MessageFactory
from AccessControl import ModuleSecurityInfo

GSMessageFactory = MessageFactory('gs.content.layout')

ModuleSecurityInfo('gs.content.layout').declarePublic('_')