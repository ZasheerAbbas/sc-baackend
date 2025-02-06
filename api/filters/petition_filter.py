# from datetime import timedelta
# import django_filters as filters
# from api.models import Petition, Organization


# class PetitionFilter(filters.FilterSet):
#     status = filters.NumberFilter(field_name='status')
#     category = filters.NumberFilter(field_name='category')
#     created_at = filters.DateFilter(field_name='created_at__date', lookup_expr='exact')
#     army_prefix = filters.CharFilter(field_name='detail__army_prefix', lookup_expr='exact')
#     army_no = filters.CharFilter(field_name='detail__army_no', lookup_expr='exact')
#     cnic = filters.CharFilter(field_name='detail__cnic', lookup_expr='exact')
#     is_serving = filters.BooleanFilter(field_name='detail__is_serving')
#     created_by = filters.NumberFilter(field_name='created_by__id')
#     currently_marked = filters.NumberFilter(field_name='currently_marked__id')
#     organization = filters.NumberFilter(field_name='currently_marked__organization__id', method='filter_organization')
#     exceed_by_7_days = filters.DateFilter(field_name='created_at__date', method='filter_exceed_by_7_days')
#     exceed_by_24_hrs = filters.DateFilter(field_name='created_at__date', method='filter_exceed_by_24_hrs')

#     def filter_organization(self, queryset, name, value):
#         organization = Organization.objects.get(pk=value)
#         children = organization.descendants(include_self=True)
#         children_ids = [child.id for child in children]
#         return queryset.filter(currently_marked__organization__id__in=children_ids).distinct()

#     def filter_exceed_by_7_days(self, queryset, name, value):
#         return queryset.filter(created_at__lte=value-timedelta(days=7)).distinct()

#     def filter_exceed_by_24_hrs(self, queryset, name, value):
#         return queryset.filter(calls__call_at__lte=value-timedelta(hours=24)).distinct()

#     class Meta:
#         model = Petition
#         fields = [
#             'army_prefix',
#             'army_no',
#             'cnic',
#             'created_by',
#             'currently_marked',
#         ]
