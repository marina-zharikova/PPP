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
#    accessory_list = ['шаль', 'платок', 'вискозная клетками', 'без бахромы']

    def handle(self, *args, **options):
        accessory_list = [_(u'шаль'), _(u'платок'), _(u'палантин'), _(u'шарф')]
        print 'start'
        Accessory_type.objects.all().delete()
        for f in accessory_list:
            ft = Accessory_type()
            ft.accessory_type = f
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
