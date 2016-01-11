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
        fabric_list = [_(u'шерсть'), _(u'шелк')]
        print 'start'
        Fabric_type.objects.all().delete()
        for f in fabric_list:
            ft = Fabric_type()
            ft.fabric_type = f
            ft.save()
            print '111'
#        for r in Radiation.objects.all():
#            b = Burning()
 #           b.id = r.id
  #          b.gid = r.gid
   #         b.gridcode = r.gridcode
    #        b.geom = r.geom
     #       b.save()
      #      print 'proccess.......%s' % b.gid
