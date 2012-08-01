# coding=utf-8
from zope.component import createObject
from zope.cachedescriptors.property import Lazy
from Products.Five import BrowserView
from zope.publisher.interfaces.browser import IBrowserPage
from zope.interface import implements

class SitePage(BrowserView):
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)

    @Lazy
    def siteInfo(self):
        retval = createObject('groupserver.SiteInfo', self.context)
        assert retval, 'Could not create the SiteInfo from %s' % self.context
        return retval

    @Lazy
    def loggedInUserInfo(self):
        retval = createObject('groupserver.LoggedInUser', self.context)
        assert retval, 'Could not create the user-info for the logged '\
            'in user from %s' % self.context
        return retval

