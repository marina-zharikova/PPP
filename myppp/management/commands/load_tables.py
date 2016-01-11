# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from myppp.models import *
from decimal import Decimal
from django.core.files import File

#logger = logging.getLogger(__name__)


class Command(BaseCommand):
#    accessory_list = ['шерсть', 'шелк']

    def handle(self, *args, **options):

############################
#Table Accessory_type
############################
        accessory_list = [_(u'шаль'), _(u'платок'), _(u'палантин'), _(u'шарф')]
        print 'start'
        Accessory_type.objects.all().delete()
        for f in accessory_list:
            ft = Accessory_type()
            ft.accessory_type = f
            ft.save()

############################
#Table Fringe_type
############################

        fringe_list = [_(u'шелковая'), _(u'шерстяная'), _(u'вискозная клетками'), _(u'без бахромы')]
        print 'start'
        Fringe_type.objects.all().delete()
        for f in fringe_list:
            ft = Fringe_type()
            ft.fringe_type = f
            ft.save()

############################
#Table Size_type
############################

        size_list = [_(u'148 на 148'), _(u'146 на 146'), _(u'125 на 125'), _(u'89 на 89'), _(u'130 на 130'), _(u'84 на 84'), _(u'65 на 65'), _(u'89 на 89'), _(u'70 на 200'), _(u'60 на 150'), _(u'43 на 150')]
        print 'start'
        Size_type.objects.all().delete()
        for f in size_list:
            ft = Size_type()
            ft.size_type = f
            ft.save()


#################################
#Tables Fabric_type, Fabric_subtype
##################################
        fabric_list = [_(u'шерсть'), _(u'шелк')]
#Subtypes for wool
        subtype_list1 = [_(u'уплотненная'), _(u'обычная'), _(u'трехниточная')]
#Subtypes for silk
        subtype_list2 = [_(u'крепдешин'), _(u'крепжоржет'), _(u'жаккард'), _(u'атлас')]
        print 'start'
        Fabric_type.objects.all().delete()
        Fabric_subtype.objects.all().delete()
        for f in fabric_list:
            ft = Fabric_type()
            ft.fabric_type = f
            ft.save()
            if f == fabric_list[0]:
                for s in subtype_list1:
                    fst=Fabric_subtype()
                    fst.fabric_type = ft
                    fst.fabric_subtype = s
                    fst.save()
            if f == fabric_list[1]:
                for s in subtype_list2:
                    fst=Fabric_subtype()
                    fst.fabric_type = ft
                    fst.fabric_subtype = s
                    fst.save()
       
            print '111'


############################
#Table Colors
############################

        color_list = [_(u'Красный'), _(u'Зеленый'), _(u'Синий'), _(u'Персиковый'), _(u'Белый'), _(u'Черный'), _(u'Бирюза'), _(u'Лимон'), _(u'Мята'), _(u'Фуксия'), _(u'Беж'), _(u'Оранж'), _(u'Розовый'), _(u'Коричневый'), _(u'Коралл'), _(u'Яркий коралл'), _(u'Горчица'), _(u'терракотовый'), _(u'Сиреневый'),]
        color_pic_list = ['#EE1E1E', '#358D2E', '#2068E2', '#E1B7BF','#F7F7F7', '#101010','#13EAE5','#E1EA13','#5FBB98','#E0256C','#EEF1B9','#F4AA0F','#EEAFAA','#83411E', '#E76F65', '#DF3E31', '#EC9931', '#CD2626', '#AB82FF']
        print 'start'
        Colors.objects.all().delete()
        n = 0
        for f in color_pic_list:
            ft = Colors()
            ft.color_pic = f
            ft.color = color_list[n]
            n = n + 1
            ft.save()





