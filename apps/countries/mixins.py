
class AddMyBirthdayToContextMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday'] = "my birthday is January 4"
        return context
