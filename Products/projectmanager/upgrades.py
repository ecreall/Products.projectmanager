from Products.CMFCore.utils import getToolByName

from Products.projectmanager import logger


def reindex_actions(context):
    catalog = getToolByName(context, 'portal_catalog')
    actions = catalog.searchResults(portal_type='PM_Action')
    for action in actions:
        try:
            action_obj = action.getObject()
        except AttributeError:
            logger.error("%s action invalid", action.getPath())
            continue

        action_obj.reindexObject(idxs=['start', 'end'])