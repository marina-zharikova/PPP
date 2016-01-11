# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from myppp.models import *
from decimal import Decimal

#logger = logging.getLogger(__name__)


class Command(BaseCommand):
#    accessory_list = ['шерсть', 'шелк']

    def handle(self, *args, **options):
#Subtypes for wool
        subtype_list1 = [_(u'уплотненная'), _(u'обычная', _(u'трехниточная'))]
#Subtypes for silk
   #     subtype_list2 = [_(u'крепдешин'), _(u'крепжоржет'), _(u'жаккард'), _(u'атлас'))]
        print 'start'
        Fabric_subtype.objects.all().delete()
        for f in subtype_list1:
            ft = Fabric_subtype()
            ft.fabric_type = '5'
            ft.fabric_sybtype = f
            ft.save()
            print '111'
  #      for f in subtype_list2:
   #         ft = Fabric_subtype()
    #        ft.fabric_type = 6
     #       ft.fabric_sybtype = f
      #      ft.save()
       #     print '111'
#        for r in Radiation.objects.all():
#            b = Burning()
 #           b.id = r.id
  #          b.gid = r.gid
   #         b.gridcode = r.gridcode
    #        b.geom = r.geom
     #       b.save()
      #      print 'proccess.......%s' % b.gid
