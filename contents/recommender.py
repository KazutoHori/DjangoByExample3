# import redis
# from django.conf import settings
# from .models import Content
#
# r=redis.Redis(host=settings.REDIS_HOST,
#                 port=settings.REDIS_PORT,
#                 db=settings.REDIS_DB)
#
# class Recommender(object):
#     def get_content_key(self, id):
#         return f'content:{id}:seen_with':
#     def contents_seen(self, contents):
#         contents_ids=[content.id for content in contents]
#         for content_id in contents_ids:
#             for with_id in contents_ids:
#                 if content_id != with_id:
#                     r.zincrby(self.get_content_key(content_id), 1, with_id)
#
#     def suggest_contents_for(self, contents, max_results=6):
#         contents_ids = [content.id for content in contents]
#         if len(contents) == 1:
#             # only 1 product
#             suggestions = r.zrange(
#                              self.get_product_key(contents_ids[0]),
#                              0, -1, desc=True)[:max_results]
#         else:
#             # generate a temporary key
#             flat_ids = ''.join([str(id) for id in contents_ids])
#             tmp_key = f'tmp_{flat_ids}'
#             # multiple products, combine scores of all products
#             # store the resulting sorted set in a temporary key
#             keys = [self.get_product_key(id) for id in contents_ids]
#             r.zunionstore(tmp_key, keys)
#             # remove ids for the products the recommendation is for
#             r.zrem(tmp_key, *contents_ids)
#             # get the product ids by their score, descendant sort
#             suggestions = r.zrange(tmp_key, 0, -1,
#                                    desc=True)[:max_results]
#             # remove the temporary key
#             r.delete(tmp_key)
#
#     suggested_contents_ids = [int(id) for id in suggestions]
#     # get suggested products and sort by order of appearance
#     suggested_contents = list(Product.objects.filter(id__in=suggested_products_ids))
#     suggested_contents.sort(key=lambda x: suggested_contents_ids.index(x.id))
#
#     return suggested_contents
