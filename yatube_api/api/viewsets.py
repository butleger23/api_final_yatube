from rest_framework import viewsets, mixins


class ListCreateModelViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    A viewset that provides default `create()` and `list()` actions.
    """
    pass
