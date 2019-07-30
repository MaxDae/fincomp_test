from zope import component
from zope.interface import classImplements

from interfaces.driver import IDriver


def registerDriver(iface, driver, class_implements=[]):
    """ Register driver adapter used by page object"""
    for class_item in class_implements:
        classImplements(class_item, iface)

    component.provideAdapter(factory=driver, adapts=[iface], provides=IDriver)
