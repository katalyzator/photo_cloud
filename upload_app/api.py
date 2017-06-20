from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.contrib.gis.resources import ModelResource

from .models import *

api_object_folder = Folder.objects.all()
api_object_subfolder = SubFolder.objects.all()
api_object_images = FolderImage.objects.all()


class FolderResource(ModelResource):
    class Meta:
        queryset = api_object_folder
        name = 'Mainfolder'

        exclude = ['timestamp', 'updated']

        filtering = {
            "name": ('exact',),
            'id': ALL_WITH_RELATIONS

        }


class SubfolderResource(ModelResource):
    main_folder = fields.ForeignKey(FolderResource, 'main_folder', full=True, null=True)

    class Meta:
        queryset = api_object_subfolder
        name = 'Subfolder'
        allowed_methods = ['get']
        filtering = {
            'main_folder': ALL_WITH_RELATIONS,
            'name': ('exact',),
            'id': ALL_WITH_RELATIONS
        }

        exclude = ['timestamp', 'updated']


class FolderImageResource(ModelResource):
    subfolder = fields.ForeignKey(SubfolderResource, 'subfolder', full=True, null=True)

    class Meta:
        queryset = api_object_images
        name = 'folderimage'
        limit = 10000
        allowed_methods = ['get']
        filtering = {
            'subfolder': ALL_WITH_RELATIONS,
            'id': ALL_WITH_RELATIONS
        }

        exclude = ['timestamp', 'updated']
